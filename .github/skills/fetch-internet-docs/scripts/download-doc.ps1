<#
.SYNOPSIS
    Download a file from a URL into the /internet-docs/ directory.

.DESCRIPTION
    Fetches the resource at the given URL and saves it verbatim. The filename is
    derived (in priority order) from: an explicit -OutFile, the server's
    Content-Disposition header, or the last segment of the URL path. Use this for
    concrete downloadable assets (PDF, zip, md, json, csv, images, etc.).

    For HTML/web pages that should be captured as structured Markdown, do NOT use
    this script — capture the content as Markdown per the skill's standard template.

.PARAMETER Url
    The URL of the file to download. Required.

.PARAMETER OutDir
    Target directory. Defaults to "internet-docs" in the current location.

.PARAMETER OutFile
    Optional explicit filename (not a full path). Overrides derived names.

.EXAMPLE
    ./download-doc.ps1 -Url "https://example.com/spec.pdf"

.EXAMPLE
    ./download-doc.ps1 -Url "https://example.com/data" -OutFile "api-schema.json"
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Url,

    [Parameter(Position = 1)]
    [string]$OutDir = "internet-docs",

    [Parameter(Position = 2)]
    [string]$OutFile
)

$ErrorActionPreference = 'Stop'

function Get-SafeFileName {
    param([string]$Name)
    $invalid = [System.IO.Path]::GetInvalidFileNameChars() -join ''
    $pattern = "[{0}]" -f [regex]::Escape($invalid)
    ($Name -replace $pattern, '-').Trim()
}

# Validate URL scheme (only http/https).
try {
    $uri = [System.Uri]$Url
} catch {
    throw "Invalid URL: $Url"
}
if ($uri.Scheme -notin @('http', 'https')) {
    throw "Only http/https URLs are supported. Got: $($uri.Scheme)"
}

# Ensure the output directory exists.
if (-not (Test-Path -LiteralPath $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}

# Resolve the target filename.
$fileName = $null

if ($OutFile) {
    $fileName = $OutFile
} else {
    # Try a HEAD-like request to read Content-Disposition without downloading fully.
    try {
        $head = Invoke-WebRequest -Uri $Url -Method Head -MaximumRedirection 5 -ErrorAction Stop
        $disposition = $head.Headers['Content-Disposition']
        if ($disposition -and $disposition -match 'filename\*?=(?:UTF-8'''')?"?([^";]+)"?') {
            $fileName = [System.Uri]::UnescapeDataString($Matches[1])
        }
    } catch {
        # HEAD not supported; fall through to URL-based naming.
    }

    if (-not $fileName) {
        $fileName = [System.IO.Path]::GetFileName($uri.LocalPath)
    }
    if (-not $fileName) {
        $fileName = "download-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    }
}

$fileName = Get-SafeFileName -Name $fileName
$destination = Join-Path -Path $OutDir -ChildPath $fileName

Write-Host "Downloading: $Url"
Write-Host "        -> : $destination"

Invoke-WebRequest -Uri $Url -OutFile $destination -MaximumRedirection 5

$size = (Get-Item -LiteralPath $destination).Length
Write-Host "Done. Saved $size bytes to $destination"

# Emit the final path so callers can capture it.
$destination
