# Indexación GSC — análisis completo · 2026-08-27 (v3, drilldowns cerrados)

Fuentes (todas del export del 27-ago, datos al 2026-08-20):

| Archivo | Contenido |
|---|---|
| `Coverage20260827.xlsx` | totales de cobertura |
| `CoverageDrilldown20260827.xlsx` | 663 URLs de "Descubierta: actualmente sin indexar" |
| `CoverageDrilldown20260827 1.xlsx` | 7 URLs de "Error de redirección" |
| `CoverageDrilldown20260827 2.xlsx` | 139 URLs de "Duplicada: otra canónica" |

---

## 1. Titular: el número real de páginas con problema no es 1193, es ~670

Con los tres drilldowns en la mano, los 1193 "sin indexar" se separan limpio:

| Motivo | URLs | Veredicto |
|---|---|---|
| Página con redirección | 358 | **Benigno.** Migración `/x/` → `/x` de julio. |
| Duplicada: otra canónica | 139 | **Benigno — confirmado con datos.** Ver §2. |
| Página alternativa con canónica | 5 | Benigno. Funcionamiento normal. |
| Rastreada: sin indexar | 21 | Menor. |
| **Error de redirección** | **7** | **🔴 Urgente. Ver §3.** |
| **Descubierta: sin indexar** | **663** | **🔴 Estructural. Ver §4.** |

**502 de las 1193 (42%) son residuo contable de la migración de julio y no requieren
ninguna acción.** Van a decaer solos. El problema real son 670 URLs, y de esas, 7 valen
más que las otras 663 juntas.

---

## 2. Las 139 "Duplicada": cerrado, no hay nada que hacer

Verificado sobre las 139 filas:

- **Las 139 terminan en barra final. Cero excepciones.**
- Ninguna tiene `.html`.
- Todas fueron rastreadas por última vez en julio (pico 13-18 de julio; ninguna después
  del 27-jul).
- **Ninguna de sus versiones canónicas (sin barra) está en la cola de 663.**

O sea: Google rastreó las URLs viejas `/x/`, eligió correctamente `/x` como canónica, y lo
está reportando. Es exactamente el comportamiento deseado. El gráfico lo confirma: 0 el
09-jul → 32 el 10-jul → **130 el 24-jul** (la ola de recrawl posterior al deploy del 19).

**Acción: ninguna.** No pedir indexación de estas URLs, no tocar `_redirects`, no
preocuparse. Es la migración funcionando.

---

## 3. Los 7 "Error de redirección": esto es lo importante del día

No son URLs marginales. Son **siete de los mejores listicles del sitio**, en su forma
canónica limpia:

| URL | Último rastreo |
|---|---|
| `/blog/libros-que-recomienda-satya-nadella` | **2026-07-14** |
| `/blog/libros-que-recomienda-reese-witherspoon` | 2026-07-13 |
| `/blog/libros-que-recomienda-sam-altman` | 2026-07-10 |
| `/blog/libros-que-recomienda-jordan-peterson` | 2026-07-08 |
| `/blog/libros-que-recomienda-elon-musk` | 2026-07-08 |
| `/blog/libros-que-recomienda-barack-obama` | 2026-07-05 |
| `/blog/libros-que-recomienda-warren-buffett` | 2026-07-05 |

Satya Nadella es **la página que mejor rankea del sitio (posición 5,0)** y Google no la
mira desde el 14 de julio. Elon Musk lo ampliaste el 16 de agosto y Google sigue viendo la
versión del 8 de julio. Barack Obama y Warren Buffett, seis semanas y media congelados.

### Qué es y por qué pasó

"Error de redirección" es Googlebot siguiendo una redirección y chocándose con algo: cadena
demasiado larga, bucle, o un `Location` vacío/malformado. Cuando eso pasa, Google **deja de
reintentar esa URL por un tiempo largo** — que es exactamente lo que muestran las fechas.

El gráfico dice 11 páginas el 09-jul, 8 el 10-jul, 7 desde el 14-ago. **Es anterior a la
migración del 19-jul**, no la causó. Encaja con el período en que el sitio todavía servía
con barra final y `/blog/x` redirigía a `/blog/x/`.

Hoy no debería pasar más: `astro.config.mjs` tiene `trailingSlash: "never"`, y revisé
`public/_redirects` completo — **no hay ninguna regla que toque `/blog/`**. Las 7 URLs
tienen que devolver 200 directo.

⚠ **Pero eso no lo pude verificar yo.** El shell del bridge no arrancó en esta sesión, y
WebFetch sigue redirecciones en silencio (la trampa que ya nos comió un diagnóstico en
agosto). Confianza en que hoy dan 200: ~85%, basada en leer la config y los redirects,
no en medirlo.

### Acción — dos pasos, hoy

```powershell
cd C:\Users\marce\ClaudeProjects\Monetizacion\Monetización\sitio-libros
.\check-indexacion.ps1
```

- **Si las 7 dan 200 directo** (lo esperable): el error es residuo de julio y Google
  simplemente no volvió. Pedir indexación de las 7 **hoy mismo** es el mejor uso de cuota
  de todo este plan: desbloquea el rastreo de tus mejores páginas y les entrega de una todo
  lo que escribiste desde julio.
- **Si alguna da 301/308**: hay un bug vivo. Pasame la salida y lo arreglamos antes de
  gastar un solo pedido.

Vale también, gratis: pasar las 7 por **Inspeccionar URL → Probar URL publicada**, que te
muestra qué ve Googlebot *ahora mismo* y te dice si sigue habiendo redirección.

---

## 4. Las 663 "Descubierta": el problema estructural (sin cambios)

Recordatorio del análisis anterior, que sigue en pie:

- **653 de 663 son fichas `/libros/` (98,5%).** 7 referentes, 3 listicles, cero hubs.
- Todas con último rastreo **1969-12-31** = epoch cero: **nunca fueron abiertas**.
- **65% del catálogo de fichas jamás fue rastreado.**
- La cola crece por lotes y no baja: 277 → 455 (24-jul) → 519 → 580 → 665 (14-ago) → 663.
  **En seis semanas salieron dos.**

La conclusión estratégica no cambia: **publicar más fichas hoy tiene ROI negativo**. Lo que
conviene producir es lo que Google sí rastrea y además rankea: más Best-of (faltan
filosofía, historia, memorias, espiritualidad) y ampliar listicles. Y la palanca grande
sigue siendo **podar el catálogo** (⚠ confianza ~70%, decisión de una sola vía, medir en un
subconjunto antes).

Y ahora se entiende mejor por qué: si 7 de tus mejores listicles llevan seis semanas sin
rastrearse, Google está gastando su presupuesto en otra cosa —o directamente lo redujo—.
Destrabar esas 7 puede tener un efecto de arrastre sobre las fichas que enlazan.

---

## 5. Las 50 URLs (v3)

Archivo: `indexacion-manual-2026-08-27-urls.txt`.

| Tanda | Qué | Por qué |
|---|---|---|
| **1** | 7 con error de redirección + 3 listicles nunca rastreados | Los 10 listicles ciegos. Máximo retorno por pedido de todo el plan. |
| **2** | 7 referentes nunca rastreados + Dune, Cien años, El principito | Los referentes son hubs de segundo nivel: cada uno enlaza decenas de fichas. |
| **3-5** | 30 fichas del cruce Best-of × cola | De los 119 títulos que enlazan los 5 Best-of, **58 están sin indexar**. Un Best-of con la mitad de sus links internos apuntando a páginas no indexadas es un Best-of debilitado. |

Las 25 fichas Best-of restantes quedan comentadas al final del `.txt` como reserva.

⚠ El orden dentro de las tandas de fichas es criterio de demanda estimada en español, no
dato de una herramienta de keywords.

**Cuota:** ~10-12 URLs/día por propiedad (⚠ no documentado oficialmente; parás cuando salte
el aviso). **Nunca pedir URLs con barra final ni `.html`.** La Indexing API de Google no
sirve acá: solo `JobPosting` y `BroadcastEvent`.

---

## 6. Cómo medir

- **Los 7 primero.** Volvé a exportar el drilldown de "Error de redirección" en 7-10 días.
  Si baja de 7 a 0, ganamos, y es la señal más rápida de todo el plan.
- **La cola de 663**: en 2-3 semanas. Si baja de 600, algo se destrabó. Si sigue en 660, los
  pedidos manuales no alcanzan y hay que ir por la poda del catálogo.
- **Páginas indexadas**: 706 → 750+ sería señal clara.
- **URLs únicas con ≥1 impresión semanal** (Rendimiento → Páginas, 7 días).

⚠ Proyección conservadora: de las 50, esperable que entren 35-45 en 2-3 semanas. Lo que
**no** es esperable es que arrastren a las otras 600 — eso es lo que decide la poda.
