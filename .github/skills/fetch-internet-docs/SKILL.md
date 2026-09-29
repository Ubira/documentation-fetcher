---
name: fetch-internet-docs
description: 'Fetch documentation or reference material from the internet and save it into a topic subfolder under the /internet-docs/ directory. Use when asked to download, archive, save, capture, or fetch docs, guides, API references, articles, specs, or web pages for offline/local use. Files are always organized by topic (up to two nested topic levels). Downloadable files (PDF, zip, etc.) are saved as-is; web content is captured as a structured Markdown file with a meaningful title.'
argument-hint: 'URL(s) or topic to fetch, plus optional filename'
---

# Fetch Internet Documentation

Download documentation from the internet into a local `/internet-docs/` directory, always organized under a topic subfolder for easier search. Direct file assets are saved as-is; everything else is captured as a well-structured Markdown file.

## Folder Layout

Every file MUST live inside a topic subfolder — never directly in `/internet-docs/`. At most **two** nested topic levels are allowed:

```
internet-docs/
├── <topic>/                 # required first level
│   ├── <file>.md
│   └── <subtopic>/          # optional second level (max depth)
│       └── <file>.md
```

- Topic folders use lowercase, hyphen-separated slugs: `react/`, `stripe-api/`.
- Use a second-level subtopic only when it meaningfully groups related pages (e.g. `react/hooks/`). Do **not** nest deeper than two levels.
- If no topic is given, derive one from the source (library name, domain, or subject).

## When to Use

- "Download the docs for <library/API> and save them locally"
- "Fetch this page/spec/guide and archive it"
- "Save this PDF/reference to internet-docs"
- "Capture the content at <URL> as markdown"
- Building a local, offline reference library of external documentation

## Inputs

- One or more URLs, OR a topic/library name to locate documentation for.
- Optional: a preferred topic/subtopic folder name or filename.

If given a topic instead of a URL, first locate the authoritative source (official docs preferred). Confirm the URL with the user if ambiguous. If no topic folder is provided, infer one from the source before saving.

## Procedure

1. **Determine the topic folder and ensure it exists.**
   - All output goes under `/internet-docs/<topic>/` at the workspace root — never directly in `/internet-docs/`.
   - Pick a concise, hyphenated topic slug from the user's request or the source (library, domain, or subject).
   - Optionally add one more level `/internet-docs/<topic>/<subtopic>/` when grouping related pages. Never go deeper than two topic levels.
   - Create the topic (and optional subtopic) directory if it does not already exist.

2. **Classify the resource.** Decide whether the URL points to:
   - **A downloadable file** — the URL ends in or serves a concrete asset (`.pdf`, `.zip`, `.md`, `.txt`, `.json`, `.csv`, `.docx`, images, etc.), OR
   - **Web content** — an HTML page, doc site, article, or API reference rendered as a webpage.

3. **If it is a downloadable file:** save it verbatim into the topic folder `/internet-docs/<topic>/` (or `/internet-docs/<topic>/<subtopic>/`).
   - Use a helper script to fetch it deterministically. Both create the target directory, derive the filename from the `Content-Disposition` header or URL, and save the file as-is. Pass the full topic path to `-OutDir`/`--out-dir`.
     - **PowerShell** (Windows): [download-doc.ps1](./scripts/download-doc.ps1)
       ```powershell
       ./.github/skills/fetch-internet-docs/scripts/download-doc.ps1 -Url "<url>" -OutDir "internet-docs/<topic>"
       ```
     - **Python** (cross-platform, stdlib only): [download_doc.py](./scripts/download_doc.py)
       ```bash
       python ./.github/skills/fetch-internet-docs/scripts/download_doc.py "<url>" --out-dir "internet-docs/<topic>"
       ```
     Pass `-OutFile`/`--out-file "<name.ext>"` to override the filename.
   - Preserve the original filename and extension when sensible; otherwise give it a clear, descriptive name.
   - Do not convert or reformat the file.

4. **If it is web content:** capture it as a Markdown file.
   - Fetch the page content.
   - Create `/internet-docs/<topic>/<meaningful-title>.md` (or under `/internet-docs/<topic>/<subtopic>/`) using the standard structure below.
   - Fill in every metadata field you can determine; use `Unknown` only when genuinely unavailable.
   - Preserve important code blocks, tables, and links from the source.

5. **Name files meaningfully.**
   - Use lowercase, hyphen-separated, descriptive slugs: `react-hooks-reference.md`, `stripe-webhooks-guide.md`.
   - Avoid generic names like `page.md`, `doc1.md`, or `untitled.md`.
   - Related pages of the same topic share the topic folder; use one optional subtopic level to group them further (e.g. `/internet-docs/react/hooks/`).

6. **Avoid duplicates.** Before writing, check whether a file for the same source already exists. If so, update it rather than creating a near-duplicate, and note the refresh date.

7. **Confirm.** Report each saved path and whether it was stored as a raw file or a generated Markdown capture.

## Standard Markdown Structure

Use this structure for every generated Markdown capture. The full template is in [doc-template.md](./assets/doc-template.md).

```markdown
# <Meaningful Title>

> **Source:** <original URL>
> **Fetched:** <YYYY-MM-DD>
> **Author / Publisher:** <name or Unknown>
> **Type:** <guide | API reference | article | spec | tutorial | changelog>
> **Tags:** <comma-separated keywords>

## Summary

One or two paragraphs describing what this document covers and why it is useful.

## Key Concepts

- Bullet points capturing the most important ideas, definitions, or takeaways.

## Details

The main body of the documentation, organized with the source's own headings where practical.

## Code Examples

Relevant code snippets preserved from the source, in fenced code blocks with language tags.

## References

- Links to related pages, official docs, or cited sources.

---
_Captured from <URL> on <YYYY-MM-DD>. Content belongs to its original author(s)._
```

## Quality Checklist

- [ ] File saved under a topic subfolder `/internet-docs/<topic>/` — never directly in `/internet-docs/`.
- [ ] No more than two nested topic levels (`<topic>/<subtopic>/`).
- [ ] Topic and filename are descriptive, hyphenated slugs — not generic.
- [ ] Raw files saved verbatim; web content saved as structured Markdown.
- [ ] Metadata block filled in (source, fetch date, type).
- [ ] Source URL and attribution preserved.
- [ ] Code blocks and tables retained with correct formatting.
- [ ] No unintended duplicate of an existing capture.

## Notes

- Only fetch URLs the user provided or that resolve to authoritative documentation. Do not guess or fabricate URLs.
- Respect the source: keep attribution and links intact; this skill archives references, it does not claim authorship.

## Resources

- [scripts/download-doc.ps1](./scripts/download-doc.ps1) — PowerShell helper that downloads a file into `/internet-docs/`, deriving the filename from the `Content-Disposition` header or URL.
- [scripts/download_doc.py](./scripts/download_doc.py) — Cross-platform Python helper (stdlib only) with the same behavior for Windows/macOS/Linux.
- [assets/doc-template.md](./assets/doc-template.md) — the standard Markdown template used to capture web content.
