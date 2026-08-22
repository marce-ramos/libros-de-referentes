<#
  check-urls.ps1 — Verificación de URLs canónicas post-deploy.

  Para qué sirve: después de cada deploy (y sobre todo después de renombrar un
  slug, mover una ruta o tocar astro.config.mjs / _redirects), comprueba que
  cada URL devuelva el código HTTP correcto y termine en la URL canónica.

  Lo más valioso son los tres últimos casos: piden URLs que NO existen y exigen
  un 404. Si alguna devuelve 200, Cloudflare está sirviendo un "soft 404" y
  Google la va a indexar como contenido válido. Así se detectó en agosto de 2026
  que /referentes/malcom-gladwell/ estaba devolviendo 200 sin tener archivo.

  Uso:
      .\check-urls.ps1
      .\check-urls.ps1 -Base "https://<hash>.losimperdibles.pages.dev"   # preview

  Salida: una línea por caso. Termina con exit code 1 si algo falló, para poder
  encadenarlo en un script de deploy.
#>

[CmdletBinding()]
param(
    [string]$Base = "https://losimperdibles.com"
)

# Status = código HTTP inmediato esperado (sin seguir redirecciones).
# Final  = ruta final esperada tras seguir todas las redirecciones.
#          $null = no se controla el destino, solo el código.
$casos = @(
    # --- Infraestructura -----------------------------------------------------
    @{ Path = "/";                                          Status = 200; Final = "/" }
    @{ Path = "/robots.txt";                                Status = 200; Final = $null }
    @{ Path = "/sitemap-index.xml";                         Status = 200; Final = $null }

    # --- Forma canónica: sin barra final y sin .html -------------------------
    @{ Path = "/libros/mindset";                            Status = 200; Final = "/libros/mindset" }
    @{ Path = "/libros/mindset/";                           Status = 308; Final = "/libros/mindset" }
    @{ Path = "/libros/mindset.html";                       Status = 308; Final = "/libros/mindset" }

    # --- Ruta vieja /autores -> /referentes ----------------------------------
    @{ Path = "/autores/peter-thiel";                       Status = 301; Final = "/referentes/peter-thiel" }
    @{ Path = "/autores/peter-thiel/";                      Status = 301; Final = "/referentes/peter-thiel" }

    # --- Typo de slug malcom -> malcolm, las 4 variantes ---------------------
    @{ Path = "/autores/malcom-gladwell";                   Status = 301; Final = "/referentes/malcolm-gladwell" }
    @{ Path = "/autores/malcom-gladwell/";                  Status = 301; Final = "/referentes/malcolm-gladwell" }
    @{ Path = "/referentes/malcom-gladwell";                Status = 301; Final = "/referentes/malcolm-gladwell" }
    @{ Path = "/referentes/malcom-gladwell/";               Status = 301; Final = "/referentes/malcolm-gladwell" }
    @{ Path = "/referentes/malcolm-gladwell";               Status = 200; Final = "/referentes/malcolm-gladwell" }

    # --- Páginas que más tráfico traen ---------------------------------------
    @{ Path = "/blog/libros-que-recomienda-bill-gates";     Status = 200; Final = $null }
    @{ Path = "/blog/libros-que-recomienda-satya-nadella";  Status = 200; Final = $null }
    @{ Path = "/referentes";                                Status = 200; Final = $null }
    @{ Path = "/categorias";                                Status = 200; Final = $null }

    # --- Detector de soft 404 (lo más importante) ----------------------------
    # Estas URLs no existen. Tienen que devolver 404, no 200.
    @{ Path = "/libros/url-que-no-existe-jamas";            Status = 404; Final = $null }
    @{ Path = "/libros/url-que-no-existe-jamas/";           Status = 404; Final = $null }
    @{ Path = "/referentes/url-que-no-existe-jamas/";       Status = 404; Final = $null }
)

Write-Host ""
Write-Host "Verificando $Base" -ForegroundColor Cyan
Write-Host ("-" * 100)

$fallos = 0

foreach ($caso in $casos) {
    $url = $Base + $caso.Path

    # Código inmediato, sin seguir redirecciones.
    $statusInmediato = curl.exe -s -o NUL -w '%{http_code}' $url

    # Destino final, siguiendo toda la cadena.
    $seguido   = curl.exe -s -o NUL -L -w '%{url_effective}|%{num_redirects}|%{http_code}' $url
    $partes    = $seguido -split '\|'
    $urlFinal  = $partes[0]
    $saltos    = [int]$partes[1]
    $statusFin = $partes[2]

    $problemas = @()

    if ($statusInmediato -ne [string]$caso.Status) {
        $problemas += "esperaba $($caso.Status), devolvio $statusInmediato"
    }

    if ($null -ne $caso.Final) {
        $esperado = ($Base + $caso.Final).TrimEnd('/')
        if ($caso.Final -eq "/") { $esperado = $Base + "/" }
        if ($urlFinal.TrimEnd('/') -ne $esperado.TrimEnd('/')) {
            $problemas += "termino en $urlFinal"
        }
    }

    # Una redireccion que termina en algo que no es 200 es una cadena rota.
    if ($caso.Status -ne 404 -and $statusFin -ne "200") {
        $problemas += "la cadena termina en $statusFin"
    }

    # Mas de un salto funciona, pero diluye señal y gasta presupuesto de rastreo.
    if ($saltos -gt 1) {
        $problemas += "$saltos saltos (deberia ser 1)"
    }

    if ($problemas.Count -eq 0) {
        Write-Host ("  OK    {0,-52} {1}" -f $caso.Path, $statusInmediato) -ForegroundColor Green
    }
    else {
        Write-Host ("  FALLA {0,-52} {1}" -f $caso.Path, ($problemas -join " | ")) -ForegroundColor Red
        $fallos++
    }
}

Write-Host ("-" * 100)

if ($fallos -eq 0) {
    Write-Host "Todo OK: $($casos.Count) casos verificados." -ForegroundColor Green
    exit 0
}
else {
    Write-Host "$fallos de $($casos.Count) casos fallaron." -ForegroundColor Red
    Write-Host ""
    Write-Host "Recordatorio: en public/_redirects el matcheo es literal respecto de la" -ForegroundColor Yellow
    Write-Host "barra final, Cloudflare aplica solo la PRIMERA regla que coincide y no" -ForegroundColor Yellow
    Write-Host "encadena. Los casos particulares van arriba de los genericos." -ForegroundColor Yellow
    exit 1
}
