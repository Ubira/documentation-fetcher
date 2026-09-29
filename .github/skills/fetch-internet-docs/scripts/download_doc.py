#!/usr/bin/env python3
"""Download a file from a URL into the /internet-docs/ directory.

Cross-platform helper (Windows, macOS, Linux) that fetches a downloadable
resource and saves it verbatim. The filename is derived (in priority order)
from: an explicit --out-file, the server's Content-Disposition header, or the
last segment of the URL path.

Use this for concrete downloadable assets (PDF, zip, md, json, csv, images...).
For HTML/web pages that should be captured as structured Markdown, do NOT use
this script -- capture the content as Markdown per the skill's standard template.

Standard library only; no third-party dependencies required.

Examples:
    python download_doc.py "https://example.com/spec.pdf"
    python download_doc.py "https://example.com/data" --out-file api-schema.json
    python download_doc.py "https://example.com/spec.pdf" --out-dir internet-docs
"""
from __future__ import annotations

import argparse
import cgi
import os
import sys
from datetime import datetime
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

USER_AGENT = "fetch-internet-docs/1.0 (+https://code.visualstudio.com)"


def safe_filename(name: str) -> str:
    """Strip characters that are invalid in filenames across platforms."""
    invalid = '<>:"/\\|?*\0'
    cleaned = "".join("-" if c in invalid else c for c in name)
    return cleaned.strip().strip(".") or "download"


def derive_filename(url: str, headers) -> str:
    """Determine a filename from Content-Disposition, then the URL path."""
    disposition = headers.get("Content-Disposition")
    if disposition:
        _, params = cgi.parse_header(disposition)
        filename = params.get("filename*") or params.get("filename")
        if filename:
            # filename* may be RFC 5987 encoded: UTF-8''name
            if "''" in filename:
                filename = filename.split("''", 1)[1]
            return safe_filename(unquote(filename))

    path_name = os.path.basename(urlparse(url).path)
    if path_name:
        return safe_filename(unquote(path_name))

    return f"download-{datetime.now():%Y%m%d-%H%M%S}"


def download(url: str, out_dir: str, out_file: str | None) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Only http/https URLs are supported. Got: {parsed.scheme or 'none'}")

    os.makedirs(out_dir, exist_ok=True)

    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request) as response:  # noqa: S310 - scheme validated above
        filename = out_file or derive_filename(response.geturl(), response.headers)
        filename = safe_filename(filename)
        destination = os.path.join(out_dir, filename)

        print(f"Downloading: {url}")
        print(f"        -> : {destination}")

        with open(destination, "wb") as fh:
            chunk_size = 64 * 1024
            total = 0
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                fh.write(chunk)
                total += len(chunk)

    print(f"Done. Saved {total} bytes to {destination}")
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Download a file from a URL into the /internet-docs/ directory."
    )
    parser.add_argument("url", help="The URL of the file to download.")
    parser.add_argument(
        "--out-dir",
        default="internet-docs",
        help="Target directory (default: internet-docs).",
    )
    parser.add_argument(
        "--out-file",
        default=None,
        help="Explicit filename (not a full path). Overrides derived names.",
    )
    args = parser.parse_args(argv)

    try:
        destination = download(args.url, args.out_dir, args.out_file)
    except Exception as exc:  # noqa: BLE001 - surface a clean message to the CLI
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    # Emit the final path so callers can capture it.
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
