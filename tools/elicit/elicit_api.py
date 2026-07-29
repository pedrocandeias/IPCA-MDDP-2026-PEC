#!/usr/bin/env python3
"""Minimal CLI for the Elicit API using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE_URL = "https://elicit.com"
DEFAULT_REPORT_DIR = Path("sources/elicit/reports")
ENV_FILES = (Path(".env.local"), Path(".env"))


class ElicitError(RuntimeError):
    pass


def load_local_env() -> None:
    for env_file in ENV_FILES:
        if not env_file.exists():
            continue
        for raw_line in env_file.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            os.environ.setdefault(key, value)


def get_api_key(explicit_key: str | None) -> str:
    key = explicit_key or os.environ.get("ELICIT_API_KEY")
    if not key:
        raise ElicitError(
            "Missing API key. Set ELICIT_API_KEY, use .env.local/.env, or pass --api-key."
        )
    return key


def request_json(
    method: str,
    path: str,
    api_key: str,
    payload: dict[str, Any] | None = None,
    query: dict[str, str] | None = None,
) -> tuple[dict[str, Any], dict[str, str]]:
    url = urllib.parse.urljoin(BASE_URL, path)
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"

    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "mestrado-elicit-cli/1.0",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body), dict(response.headers.items())
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            error_data = json.loads(raw)
        except json.JSONDecodeError:
            error_data = {"error": {"message": raw}}
        message = error_data.get("error", {}).get("message") or error_data.get(
            "message", raw
        )
        raise ElicitError(f"HTTP {exc.code}: {message}") from exc
    except urllib.error.URLError as exc:
        raise ElicitError(f"Network error: {exc.reason}") from exc


def download_file(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"Accept": "*/*"})
    with urllib.request.urlopen(req) as response, destination.open("wb") as handle:
        handle.write(response.read())


def sanitize_report_manifest(data: dict[str, Any]) -> dict[str, Any]:
    sanitized = json.loads(json.dumps(data))
    local_assets: dict[str, str] = {}
    for field, filename in (("docxUrl", "report.docx"), ("pdfUrl", "report.pdf")):
        if field in sanitized:
            sanitized.pop(field, None)
            local_assets[field] = filename
    if local_assets:
        sanitized["downloadedAssets"] = local_assets
    return sanitized


def print_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def truncate(text: str, width: int) -> str:
    compact = " ".join(text.split())
    if len(compact) <= width:
        return compact
    return compact[: width - 1] + "..."


def terminal_width(default: int = 100) -> int:
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default


def print_papers(papers: list[dict[str, Any]]) -> None:
    if not papers:
        print("No papers found.")
        return

    width = terminal_width()
    for index, paper in enumerate(papers, start=1):
        title = paper.get("title") or "(untitled)"
        year = paper.get("year") or "n/a"
        authors = ", ".join(paper.get("authors") or [])
        venue = paper.get("venue") or ""
        doi = paper.get("doi") or ""
        abstract = paper.get("abstract") or ""

        print(f"{index}. {truncate(title, width - 8)} ({year})")
        meta = " | ".join(part for part in (authors, venue) if part)
        if meta:
            print(f"   {truncate(meta, width - 3)}")
        if abstract:
            print(f"   {truncate(abstract, width - 3)}")
        if doi:
            print(f"   https://doi.org/{doi}")
        print()


def print_report_status(report: dict[str, Any], verbose: bool = True) -> None:
    status = report.get("status", "unknown")
    result = report.get("result") or {}
    title = report.get("title") or result.get("title") or report.get("reportId", "")
    print(f"[{status}] {title}")
    if report.get("url"):
        print(f"  {report['url']}")
    if verbose and status == "completed" and result.get("summary"):
        wrapped = textwrap.fill(result["summary"], width=max(60, terminal_width() - 2))
        print(f"\n{wrapped}")
    print()


def command_search(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    payload: dict[str, Any] = {
        "query": args.query,
        "maxResults": args.max_results,
        "searchMode": args.search_mode,
        "corpus": args.corpus,
    }
    filters: dict[str, Any] = {}
    if args.min_year is not None:
        filters["minYear"] = args.min_year
    if args.max_year is not None:
        filters["maxYear"] = args.max_year
    if args.type_tag:
        filters["typeTags"] = args.type_tag
    if args.max_quartile is not None:
        filters["maxQuartile"] = args.max_quartile
    if args.pubmed_only:
        filters["pubmedOnly"] = True
    if args.include_keyword:
        filters["includeKeywords"] = args.include_keyword
    if args.exclude_keyword:
        filters["excludeKeywords"] = args.exclude_keyword
    if filters and args.search_mode == "keyword":
        raise ElicitError("Filters are not supported with --search-mode keyword.")
    if filters:
        payload["filters"] = filters

    data, headers = request_json("POST", "/api/v1/search", api_key, payload=payload)
    if args.json:
        print_json(data)
    else:
        print_papers(data.get("papers", []))
    rate_headers = {
        key: value
        for key, value in headers.items()
        if key.lower().startswith("x-ratelimit-")
    }
    if rate_headers:
        print("\nRate limit headers:", file=sys.stderr)
        for key, value in sorted(rate_headers.items()):
            print(f"{key}: {value}", file=sys.stderr)
    return 0


def command_report(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    payload: dict[str, Any] = {
        "researchQuestion": args.question,
        "isPublic": args.public,
    }
    if args.title:
        payload["title"] = args.title
    if args.search_papers is not None:
        payload["maxSearchPapers"] = args.search_papers
    if args.extract_papers is not None:
        payload["maxExtractPapers"] = args.extract_papers

    data, _ = request_json("POST", "/api/v1/reports", api_key, payload=payload)
    if args.no_wait:
        print_json(data) if args.json else print_report_status(data, verbose=False)
        return 0

    report_id = data["reportId"]
    final_report = wait_for_report(api_key, report_id, args.poll_seconds)
    if args.json:
        print_json(final_report)
    else:
        print_report_status(final_report)
    if final_report.get("status") == "failed":
        return 1
    return 0


def command_get_report(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    query = {"include": "reportBody"} if args.include_body else None
    data, _ = request_json(
        "GET",
        f"/api/v1/reports/{args.report_id}",
        api_key,
        query=query,
    )
    print_json(data)
    return 0


def command_list_reports(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    query: dict[str, str] = {"limit": str(args.limit)}
    if args.cursor:
        query["cursor"] = args.cursor
    if args.source:
        query["source"] = args.source
    if args.status:
        query["status"] = args.status
    data, _ = request_json("GET", "/api/v1/reports", api_key, query=query)
    if args.json:
        print_json(data)
    else:
        reports = data if isinstance(data, list) else data.get("reports", [])
        for report in reports:
            print_report_status(report, verbose=False)
    return 0


def wait_for_report(api_key: str, report_id: str, poll_seconds: int) -> dict[str, Any]:
    while True:
        data, _ = request_json("GET", f"/api/v1/reports/{report_id}", api_key)
        status = data.get("status")
        print(f"status={status} url={data.get('url')}", file=sys.stderr)
        if status in {"completed", "failed", "unknown"}:
            return data
        time.sleep(poll_seconds)


def command_wait_report(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    data = wait_for_report(api_key, args.report_id, args.poll_seconds)
    print_json(data)
    return 0


def command_download_report(args: argparse.Namespace) -> int:
    api_key = get_api_key(args.api_key)
    data, _ = request_json("GET", f"/api/v1/reports/{args.report_id}", api_key)
    status = data.get("status")
    if status != "completed":
        raise ElicitError(
            f"Report {args.report_id} is not completed. Current status: {status}"
        )

    output_dir = Path(args.output_dir or DEFAULT_REPORT_DIR / args.report_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = output_dir / "report.json"
    manifest_path.write_text(
        json.dumps(sanitize_report_manifest(data), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    downloaded = []
    for field, filename in (("docxUrl", "report.docx"), ("pdfUrl", "report.pdf")):
        url = data.get(field)
        if url:
            destination = output_dir / filename
            download_file(url, destination)
            downloaded.append(str(destination))

    print_json(
        {
            "reportId": args.report_id,
            "outputDir": str(output_dir),
            "files": downloaded,
            "manifest": str(manifest_path),
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Elicit API helper CLI")
    parser.add_argument("--api-key", help="Override ELICIT_API_KEY for this run")

    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="Search academic papers")
    search.add_argument("query", help="Natural-language or keyword query")
    search.add_argument("--max-results", type=int, default=10)
    search.add_argument(
        "--search-mode", choices=("semantic", "keyword"), default="semantic"
    )
    search.add_argument("--corpus", choices=("elicit", "pubmed"), default="elicit")
    search.add_argument("--min-year", type=int)
    search.add_argument("--max-year", type=int)
    search.add_argument("--type", dest="type_tag", action="append", default=[])
    search.add_argument("--max-quartile", type=int, choices=(1, 2, 3, 4))
    search.add_argument("--pubmed-only", action="store_true")
    search.add_argument(
        "--include-keyword", action="append", default=[], help="Repeatable filter"
    )
    search.add_argument(
        "--exclude-keyword", action="append", default=[], help="Repeatable filter"
    )
    search.add_argument("--json", action="store_true")
    search.set_defaults(func=command_search)

    create_report = subparsers.add_parser(
        "report", aliases=["create-report"], help="Create an asynchronous Elicit report"
    )
    create_report.add_argument("question")
    create_report.add_argument("--title")
    create_report.add_argument("--search-papers", type=int)
    create_report.add_argument("--extract-papers", type=int)
    create_report.add_argument("--public", action="store_true")
    create_report.add_argument("--poll-seconds", type=int, default=30)
    create_report.add_argument("--no-wait", action="store_true")
    create_report.add_argument("--json", action="store_true")
    create_report.set_defaults(func=command_report)

    get_report = subparsers.add_parser("get-report", help="Fetch one report")
    get_report.add_argument("report_id")
    get_report.add_argument("--include-body", action="store_true")
    get_report.set_defaults(func=command_get_report)

    list_reports = subparsers.add_parser(
        "reports", aliases=["list-reports"], help="List reports"
    )
    list_reports.add_argument("--limit", type=int, default=10)
    list_reports.add_argument("--cursor")
    list_reports.add_argument("--source", choices=("api", "user"), default="user")
    list_reports.add_argument("--status")
    list_reports.add_argument("--json", action="store_true")
    list_reports.set_defaults(func=command_list_reports)

    wait_report = subparsers.add_parser(
        "wait-report", help="Poll until a report finishes"
    )
    wait_report.add_argument("report_id")
    wait_report.add_argument("--poll-seconds", type=int, default=30)
    wait_report.set_defaults(func=command_wait_report)

    download_report = subparsers.add_parser(
        "download-report", help="Download completed report assets"
    )
    download_report.add_argument("report_id")
    download_report.add_argument(
        "--output-dir",
        help="Override output directory. Default: sources/elicit/reports/<report_id>",
    )
    download_report.set_defaults(func=command_download_report)

    return parser


def main() -> int:
    load_local_env()
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except ElicitError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
