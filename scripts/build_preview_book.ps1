$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$VenvActivate = Join-Path (Split-Path -Parent $RepoRoot) "venv\Scripts\Activate.ps1"

if (-not (Test-Path $VenvActivate)) {
    Write-Host "Could not find venv activation script at: $VenvActivate" -ForegroundColor Red
    Write-Host "Expected the venv as a sibling folder to the repo, e.g. ..\venv (see README.md dev setup)." -ForegroundColor Red
    exit 1
}

Write-Host "Activating venv..." -ForegroundColor Cyan
. $VenvActivate

function Build-Book {
    param(
        [string]$Name,
        [string]$ContentDir,
        [string[]]$ConfigArgs,
        [string]$OutputDir
    )

    Write-Host "Building $Name book..." -ForegroundColor Cyan
    Push-Location $ContentDir
    try {
        jupyter-book build . @ConfigArgs --path-output $OutputDir
        if ($LASTEXITCODE -ne 0) {
            throw "$Name book build failed with exit code $LASTEXITCODE"
        }
    } finally {
        Pop-Location
    }
}

Build-Book -Name "English" -ContentDir "content\en" -ConfigArgs @() -OutputDir "..\..\english"
Build-Book -Name "Spanish" -ContentDir "content\es" -ConfigArgs @("--config", "es_config.yml", "--toc", "es_toc.yml") -OutputDir "..\..\spanish"
Build-Book -Name "French"  -ContentDir "content\fr" -ConfigArgs @("--config", "fr_config.yml", "--toc", "fr_toc.yml") -OutputDir "..\..\french"

Write-Host "Combining language builds into one local preview site..." -ForegroundColor Cyan

$SitePath = Join-Path $RepoRoot "_site"
if (Test-Path $SitePath) {
    Remove-Item $SitePath -Recurse -Force
}

New-Item -ItemType Directory -Path "$SitePath\en" -Force | Out-Null
New-Item -ItemType Directory -Path "$SitePath\es" -Force | Out-Null
New-Item -ItemType Directory -Path "$SitePath\fr" -Force | Out-Null
New-Item -ItemType Directory -Path "$SitePath\content" -Force | Out-Null

function Copy-BuildOutput {
    param([string]$Source, [string]$Destination)

    robocopy $Source $Destination /MIR | Out-Null
    if ($LASTEXITCODE -ge 8) {
        throw "robocopy failed copying $Source to $Destination (exit code $LASTEXITCODE)"
    }
}

Copy-BuildOutput -Source "english\_build\html" -Destination "$SitePath\en"
Copy-BuildOutput -Source "spanish\_build\html" -Destination "$SitePath\es"
Copy-BuildOutput -Source "french\_build\html" -Destination "$SitePath\fr"

@"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=en/">
    <title>GIS Training Resource Center (local preview)</title>
    <link rel="canonical" href="en/">
  </head>
  <body>
    <p>Redirecting to <a href="en/">English version</a>.</p>
  </body>
</html>
"@ | Set-Content -Path "$SitePath\index.html" -Encoding utf8

@"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=../en/intro.html">
    <title>Redirecting to English introduction</title>
    <link rel="canonical" href="../en/intro.html">
  </head>
  <body>
    <p>Redirecting to <a href="../en/intro.html">the English introduction page</a>.</p>
  </body>
</html>
"@ | Set-Content -Path "$SitePath\content\intro.html" -Encoding utf8

New-Item -ItemType File -Path "$SitePath\.nojekyll" -Force | Out-Null

Write-Host "Preview site built at: $SitePath" -ForegroundColor Green
Write-Host "  English: /en/" -ForegroundColor Green
Write-Host "  Spanish: /es/" -ForegroundColor Green
Write-Host "  French:  /fr/" -ForegroundColor Green

$Port = 8080
Write-Host ""
Write-Host "Starting local server at http://localhost:$Port (press Ctrl+C to stop) ..." -ForegroundColor Cyan

Push-Location $SitePath
try {
    Start-Process "http://localhost:$Port"
    python -m http.server $Port
} finally {
    Pop-Location
}
