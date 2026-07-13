# build.ps1 — limpia cachés de build y vuelve a compilar el sitio
Set-Location -Path $PSScriptRoot

Write-Host "Limpiando .astro, dist y node_modules\.astro..." -ForegroundColor Cyan
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .astro, dist, node_modules\.astro

Write-Host "Corriendo npm run build..." -ForegroundColor Cyan
npm run build
