---
description: 'Conventions for formatting and storing research notes and gathered source lists in this repository. Use when creating or editing research notes, source/link lists, bibliographies, or archived documentation.'
applyTo: '**/internet-docs/**/*.md, **/research/**/*.md, **/*.sources.md, **/*.research.md'
---

# Research Notes Conventions

Apply these rules when writing research notes or source lists (e.g. output from the `find-topic-sources` skill or files under `internet-docs/` and `research/`).

## Location & Naming

- Store curated source lists under `research/` at the workspace root.
- Store archived page/file content under `internet-docs/` (produced by the `fetch-internet-docs` skill).
- Use lowercase, hyphen-separated slugs: `vector-databases.sources.md`, `oauth-pkce.research.md`.
- One topic per file. Group multi-part research under a topic subfolder.

## File Structure

Every research/source file starts with this header, then the sources:

```markdown
# <Topic>

- **Focus**: <the specific angle or question, or "general overview">
- **Created**: <YYYY-MM-DD>
- **Last updated**: <YYYY-MM-DD>
- **Status**: draft | reviewed

## Sources

1. **<Title>** — <type: docs | spec | tutorial | paper | repo | file>
   <url>
   Why: <one-sentence relevance note>
   Verified: <YYYY-MM-DD>
```

## Content Rules

- Every URL must be a real, verified link — never fabricate or guess URLs.
- Record the verification date next to each link; re-verify before reusing links older than 6 months.
- Rank sources by authority and relevance (official docs and primary sources first).
- Keep the "Why" note to a single sentence; do not paste large excerpts here.
- When a source is archived locally, add `Archived: internet-docs/<filename>` under its entry.
- Note the type explicitly when a link points to a downloadable file rather than a web page.

## Maintenance

- Update **Last updated** whenever entries change and bump **Status** to `reviewed` once links are verified.
- Remove dead or superseded links rather than leaving broken references; note removals if context matters.
