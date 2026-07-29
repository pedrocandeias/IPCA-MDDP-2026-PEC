#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const DIALECT_MAP = {
  "en-us": "American",
  "en-gb": "British",
  "en-au": "Australian",
  "en-ca": "Canadian",
  "en-in": "Indian",
};

const DEFAULT_LOCALE = "pt-PT";

function printUsage() {
  console.log(`Usage:
  node tools/harper_lint.mjs check <file> [options]
  node tools/harper_lint.mjs describe-rules

Options:
  --locale <code>         pt-PT (default), en-US, en-GB, en-AU, en-CA, en-IN
  --language <name>       markdown | plaintext | typst (default: inferred from file extension)
  --config <file>         JSON file with Harper rule toggles, passed to setLintConfig()
  --json                  Print machine-readable JSON output
  --summary               Print only counts by rule
  --ignore-link-title     Skip linting Markdown link titles
`);
}

function parseArgs(argv) {
  const args = argv.slice(2);
  if (args.length === 0 || args.includes("--help") || args.includes("-h")) {
    return { command: "help" };
  }

  const command = args[0];
  const rest = args.slice(1);
  const options = {
    locale: DEFAULT_LOCALE,
    language: null,
    configPath: null,
    json: false,
    summary: false,
    ignoreLinkTitle: false,
  };
  const positionals = [];

  for (let i = 0; i < rest.length; i += 1) {
    const token = rest[i];
    if (token === "--locale") {
      options.locale = rest[++i];
    } else if (token === "--language") {
      options.language = rest[++i];
    } else if (token === "--config") {
      options.configPath = rest[++i];
    } else if (token === "--json") {
      options.json = true;
    } else if (token === "--summary") {
      options.summary = true;
    } else if (token === "--ignore-link-title") {
      options.ignoreLinkTitle = true;
    } else if (token.startsWith("--")) {
      throw new Error(`Unknown option: ${token}`);
    } else {
      positionals.push(token);
    }
  }

  return { command, options, positionals };
}

function inferLanguage(filePath) {
  const extension = path.extname(filePath).toLowerCase();
  if (extension === ".md" || extension === ".markdown") {
    return "markdown";
  }
  if (extension === ".typ" || extension === ".typst") {
    return "typst";
  }
  return "plaintext";
}

function normalizeDialect(harper, locale) {
  const normalized = DIALECT_MAP[String(locale).toLowerCase()];
  if (!normalized || !(normalized in harper.Dialect)) {
    throw new Error(`Unsupported Harper locale: ${locale}`);
  }
  return harper.Dialect[normalized];
}

function localeSupport(locale) {
  const normalized = String(locale).toLowerCase();
  if (normalized in DIALECT_MAP) {
    return { supported: true, normalized };
  }
  if (normalized === "pt-pt") {
    return { supported: false, normalized, reason: "Harper ainda nao suporta portugues europeu (pt-PT)." };
  }
  if (normalized.startsWith("pt-")) {
    return { supported: false, normalized, reason: `Harper ainda nao suporta portugues (${locale}).` };
  }
  return { supported: false, normalized, reason: `Locale nao suportado pelo wrapper Harper: ${locale}.` };
}

async function createLinter(options) {
  let harper;
  try {
    harper = await import("harper.js");
  } catch (error) {
    throw new Error(
      "Missing dependency 'harper.js'. Run `npm install` in the repository root first."
    );
  }

  const linter = new harper.LocalLinter({
    binary: harper.binary,
    dialect: normalizeDialect(harper, options.locale),
  });
  await linter.setup();

  if (options.configPath) {
    const rawConfig = await fs.readFile(options.configPath, "utf-8");
    const config = JSON.parse(rawConfig);
    await linter.setLintConfig(config);
  }

  return linter;
}

function lintToObject(lint) {
  const span = lint.span();
  return {
    start: span.start,
    end: span.end,
    message: lint.message(),
    kind: lint.lint_kind(),
    kindPretty: lint.lint_kind_pretty(),
    problemText: lint.get_problem_text(),
    suggestions: lint.suggestions().map((suggestion) => ({
      replacement: suggestion.get_replacement_text(),
      kind: suggestion.kind(),
    })),
  };
}

function summarizeLints(lints) {
  const counts = {};
  for (const lint of lints) {
    const key = lint.lint_kind();
    counts[key] = (counts[key] ?? 0) + 1;
  }
  return counts;
}

function printHumanResults(filePath, lints, summaryOnly) {
  if (summaryOnly) {
    const counts = summarizeLints(lints);
    console.log(`${filePath}: ${lints.length} issues`);
    for (const [rule, count] of Object.entries(counts).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))) {
      console.log(`- ${rule}: ${count}`);
    }
    return;
  }

  if (lints.length === 0) {
    console.log(`${filePath}: no issues found`);
    return;
  }

  console.log(`${filePath}: ${lints.length} issues`);
  for (const lint of lints) {
    const item = lintToObject(lint);
    console.log(`- [${item.kind}] ${item.start}-${item.end}: ${item.message}`);
    if (item.problemText) {
      console.log(`  text: ${item.problemText}`);
    }
    if (item.suggestions.length > 0) {
      const rendered = item.suggestions
        .map((suggestion) => suggestion.replacement || "<remove>")
        .join(", ");
      console.log(`  suggestions: ${rendered}`);
    }
  }
}

function printUnsupportedLocale(filePath, locale, reason, json) {
  if (json) {
    const payload = {
      file: filePath,
      locale,
      skipped: true,
      reason,
      issueCount: 0,
      issues: [],
      summary: {},
    };
    console.log(JSON.stringify(payload, null, 2));
    return;
  }

  console.log(`${filePath}: skipped`);
  console.log(`- locale: ${locale}`);
  console.log(`- reason: ${reason}`);
  console.log(`- hint: use --locale en-GB or another supported English locale when you want Harper linting`);
}

async function runCheck(positionals, options) {
  const target = positionals[0];
  if (!target) {
    throw new Error("Missing file path for 'check'.");
  }

  const filePath = path.resolve(target);
  const support = localeSupport(options.locale);
  if (!support.supported) {
    printUnsupportedLocale(filePath, options.locale, support.reason, options.json);
    return;
  }

  const source = await fs.readFile(filePath, "utf-8");
  const language = options.language ?? inferLanguage(filePath);
  const linter = await createLinter(options);
  const lints = await linter.lint(source, {
    language,
    markdown: {
      IgnoreLinkTitle: options.ignoreLinkTitle,
    },
  });

  if (options.json) {
    const payload = {
      file: filePath,
      language,
      locale: options.locale,
      issueCount: lints.length,
      issues: lints.map(lintToObject),
      summary: summarizeLints(lints),
    };
    console.log(JSON.stringify(payload, null, 2));
  } else {
    printHumanResults(filePath, lints, options.summary);
  }
}

async function runDescribeRules(options) {
  const linter = await createLinter(options);
  const descriptions = await linter.getLintDescriptions();
  console.log(JSON.stringify(descriptions, null, 2));
}

async function main() {
  try {
    const parsed = parseArgs(process.argv);
    if (parsed.command === "help") {
      printUsage();
      return;
    }

    if (parsed.command === "check") {
      await runCheck(parsed.positionals, parsed.options);
      return;
    }

    if (parsed.command === "describe-rules") {
      await runDescribeRules(parsed.options);
      return;
    }

    throw new Error(`Unknown command: ${parsed.command}`);
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}

await main();
