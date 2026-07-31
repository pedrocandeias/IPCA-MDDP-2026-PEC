# Elicit Library Organization

This project uses a local folder hierarchy as the source of truth and mirrors it in Elicit Library with Collections and Tags.

## Principle

- Local folders keep the real hierarchy, files, notes, and downloaded reports.
- Elicit Library keeps papers and bibliography organized in a parallel but flatter structure.
- Collections should mimic subsection scope.
- Tags should capture source, use status, and topic.

## Collection Naming

Use one collection per working subsection.

Recommended format:

- `capitulo-6`
- `capitulo-6__6.1`
- `capitulo-6__6.2`
- `capitulo-6__6.3`

If Elicit displays slashes cleanly and supports that style well in the UI, this alternative is also acceptable:

- `Capítulo 6`
- `Capítulo 6 / 6.1`
- `Capítulo 6 / 6.2`
- `Capítulo 6 / 6.3`

Prefer one naming convention only. Do not mix both.

## Tag System

Use a small stable set of tags.

Scope tags:

- `chapter-6`
- `6.1`
- `6.2`
- `6.3`

Source tags:

- `search`
- `report`

Use tags:

- `anchor-paper`
- `cite`
- `read-next`
- `background`

Topic tags:

- `parametric`
- `anthropometry`
- `human-in-the-loop`
- `decision-support`
- `validation-gap`
- `3d-printing`

## Mapping from Local Structure

Local folder:

- `material/investigacao/elicit/capitulo-6/6.1/searches/`
  Elicit: collection `capitulo-6__6.1` + tag `search`

- `material/investigacao/elicit/capitulo-6/6.1/reports/`
  Elicit: collection `capitulo-6__6.1` + tag `report`

- anchor references extracted from notes or reports
  Elicit: same collection + tags `anchor-paper` and `cite`

- papers that should feed the next subsection
  Elicit: same collection + tag `read-next`

## Working Rule

When a paper is added to Elicit for a subsection, assign:

1. one collection
2. one source tag (`search` or `report`)
3. one use tag (`anchor-paper`, `cite`, `read-next`, or `background`)
4. topic tags only when they help retrieval

Avoid over-tagging. If a tag does not improve retrieval or writing decisions, do not add it.
