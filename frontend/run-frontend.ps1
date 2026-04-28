$ErrorActionPreference = "Stop"

$Node = "C:\Program Files\nodejs\node.exe"
$Vite = Join-Path $PSScriptRoot "node_modules\vite\bin\vite.js"

Set-Location $PSScriptRoot
& $Node $Vite --host 127.0.0.1 --port 5173
