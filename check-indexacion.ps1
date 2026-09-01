<#
  check-indexacion.ps1 — Verifica la lista de URLs antes de gastar cuota de GSC.

  Por qué existe: "Solicitar indexación" en Search Console tiene una cuota diaria
  muy baja (~10-12 URLs). Pedir una URL que devuelve 308, 301 o 404 es cuota
  tirada a la basura y encima le confirma a Google que esa URL no es canónica.
  Este script exige 200 INMEDIATO, sin redirecciones. Si algo no da 200, se
  corrige el sitio primero y recién después se pide la indexación.

  Uso:
      .\check-indexacion.ps1
      .\check-indexacion.ps1 -Lista ".\indexacion-manual-2026-08-27-urls.txt"
      .\check-indexacion.ps1 -SoloFallas      # imprime solo lo que hay que revisar

  Exit code 1 si alguna URL no devuelve 200 directo.
#>

[CmdletBinding()]
param(
    [string]$Lista = ".\indexacion-manual-2026-08-27-urls.txt",
    [switch]$SoloFallas
)

if (-not (Test-Path $Lista)) {
    Write-Host "No encuentro la lista: $Lista" -ForegroundColor Red
    exit 1
}

$urls = Get-Content $Lista -Encoding UTF8 |
        Where-Object { $_ -match '^\s*https?://' } |
        ForEach-Object { $_.Trim() }

Write-Host "Verificando $($urls.Count) URLs (se exige 200 directo, 0 redirecciones)`n"

$fallas = 0
$i = 0

foreach ($url in $urls) {
    $i++
    $code = 0
    $loc  = ""
    try {
        $r = Invoke-WebRequest -Uri $url -Method Head -MaximumRedirection 0 `
                               -ErrorAction Stop -TimeoutSec 20
        $code = [int]$r.StatusCode
    }
    catch {
        $resp = $_.Exception.Response
        if ($resp) {
            $code = [int]$resp.StatusCode
            $loc  = $resp.Headers['Location']
        }
    }

    $ok = ($code -eq 200)
    if (-not $ok) { $fallas++ }

    if ($ok -and $SoloFallas) { continue }

    $color = if ($ok) { 'Green' } else { 'Red' }
    $extra = if ($loc) { "  ->  $loc" } else { "" }
    Write-Host ("{0,3}. [{1}] {2}{3}" -f $i, $code, $url, $extra) -ForegroundColor $color
}

Write-Host ""
if ($fallas -eq 0) {
    Write-Host "OK: las $($urls.Count) URLs devuelven 200 directo. Listo para pedir indexacion." -ForegroundColor Green
    exit 0
}
else {
    Write-Host "$fallas URL(s) NO devuelven 200. Corregilas ANTES de gastar cuota." -ForegroundColor Red
    exit 1
}
