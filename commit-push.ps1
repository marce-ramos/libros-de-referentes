# commit-push.ps1 — git add + commit (con mensaje pedido por pantalla) + push
Set-Location -Path $PSScriptRoot

git add .

$mensaje = Read-Host "Mensaje del commit"
if ([string]::IsNullOrWhiteSpace($mensaje)) {
    Write-Host "Mensaje vacío, cancelando commit." -ForegroundColor Red
    exit 1
}

git commit -m "$mensaje"
git push
