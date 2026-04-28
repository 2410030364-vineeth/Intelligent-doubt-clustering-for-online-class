$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Python = "C:\Users\vamsh\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$env:PYTHONPATH = @(
  (Join-Path $PSScriptRoot "pip_patch")
  (Join-Path $PSScriptRoot ".pydeps")
  $PSScriptRoot
) -join ";"

Set-Location $Root
& $Python -m uvicorn app.main:app --host 127.0.0.1 --port 8001
