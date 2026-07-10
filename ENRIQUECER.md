# ENRIQUECER — mini-spec para subagente económico

Spec compacto y autosuficiente para enriquecer **fichas de libros** y **páginas de referentes**
con un modelo barato (Sonnet). Objetivo: bajar el costo en tokens vs hacerlo con Opus.
Es un extracto operativo de `CONTENIDO.md` (la fuente de verdad completa sigue siendo esa).

## Flujo (quién hace qué)

1. **Opus (1 vez, barato):** elige el lote (N slugs) desde `WORKLIST.md` y lanza el subagente.
2. **Subagente (Sonnet):** por cada slug, investiga con `WebSearch`, edita/escribe el `.md`
   con Read/Write, y anota la tanda en `PROGRESO.md`.
3. **Script (bash, ~0 tokens):** valida ASIN/integridad (ver "Verificación").
4. **Opus (spot-check):** revisa 1-2 fichas y el output del script.

## Regla de herramientas (obligatoria)

- Leer/editar SIEMPRE con **Read / Write / Edit**. NUNCA `cat`/`sed` de bash para contenido:
  el mount se desincroniza y muestra versiones viejas/truncadas.
- El `WebSearch` es lo caro: máximo **1-2 búsquedas por ítem**. Si no confirmás un dato, no lo inventes.

---

## MODO LIBRO (ficha en stub → enriquecida)

Frontmatter (mantener `categoria` y `recomendadoPor` existentes; no renombrar el archivo):

```yaml
---
titulo: "Título en español si hay edición; si no, el original"
autorLibro: "Autor del libro"
asin: "XXXXXXXXXX"          # ISBN-10 de la edición impresa, 10 chars alfanum. Ver regla de oro.
categoria: <slug existente>  # no cambiar salvo error claro
recomendadoPor:              # no tocar los que ya están
  - <slug-referente>
anio: 1949                   # opcional
resumen: "1-2 frases (meta/listados). Nombrá a quién lo recomienda."
destacado: false
fechaActualizado: <hoy, formato AAAA-MM-DD; confirmá con `date`>
---
```

**Regla de oro del ASIN:** nunca inventarlo. Buscar `"<título español>" <autor> edición español ISBN Amazon`,
tomar el ISBN-10 del `/dp/XXXXXXXXXX` de Amazon, verificar **10 caracteres**. Preferir edición en
español; si no existe, la inglesa. Si no se confirma un ASIN fiable, **dejar `asin` vacío** (el botón
usa el fallback de búsqueda). No scrapear portadas.

**Cuerpo** (~300-420 palabras, original, tono "amigo que sabe", castellano rioplatense):
intro que engancha + `## Por qué lo recomienda <Referente>` (una sección por referente listado) +
`## De qué trata` + `## <idea/concepto clave>` + `## Para quién es`. Última línea, en blockquote:
`> Edición en español: *Título*, Editorial (traducción de …).` — o si es solo inglés:
`> Por ahora disponible solo en inglés; el enlace lleva a la edición de <Editorial>.`

Nunca dejar el stub autogenerado ("*X*, de Y, figura entre las recomendaciones de Z.").

---

## MODO REFERENTE (bio genérica → real)

Los archivos `autores/<slug>.md` con bio genérica ya traen la **fuente** identificada en la línea
"…rastrearse a través de <FUENTE>". Usar esa fuente; no inventar otras.

```yaml
---
nombre: "Nombre Apellido"        # no tocar
profesion: "Rol principal"        # ajustar si es impreciso (ej: "Cofundador de Microsoft")
bio: "1 frase natural con su credencial principal; se usa como meta description."
foto: "/autores/<slug>.jpg"       # SOLO si ya existe el archivo; si no, NO agregar (hay monograma)
destacado: <mantener>
orden: <mantener>
---

<2-3 frases reales: quién es y por qué es relevante + por qué seguimos sus recomendaciones +
la FUENTE verificable de sus lecturas (la que ya estaba en el archivo). Sin datos inventados,
sin cifras dudosas. Tono cercano e informado.>
```

No inventar fotos ni URLs. Si la fuente parece vaga ("Entrevistas"), mantenerla tal cual pero
redactar la bio sin apoyarse en datos no verificables.

**Ojo con los cargos en presente:** las posiciones cambian (renuncias, cambios de empresa). Ante
la duda, usá framing atemporal o "ex-" ("exprofesor de…", "fundó…") en vez de afirmar un cargo
actual que puede estar desactualizado.

---

## Verificación (correr al terminar cada lote)

```bash
cd <repo>/src/content
# ASIN de 10 chars en las fichas tocadas:
for f in libros/<slug1>.md libros/<slug2>.md; do a=$(grep -m1 '^asin:' "$f"|sed 's/asin: //;s/"//g;s/ //g'); echo "${#a} $f"; done
# Integridad recomendadoPor -> autor existente:
for f in libros/*.md; do awk '/^recomendadoPor:/{g=1;next} g&&/^  - /{gsub(/  - /,"");print} g&&/^[^ ]/{exit}' "$f" | while read r; do [ -f "autores/$r.md" ] || echo "FALTA $r en $f"; done; done
```

Además: `npm run build` local antes del push (o confiar en Cloudflare, que buildea limpio).

---

## Prompt para lanzar el subagente (pegar en Agent, model: sonnet)

> Sos un editor de contenido del sitio "Los Imperdibles" (losimperdibles.com), libros que
> recomiendan referentes mundiales, en español (Argentina). Leé `ENRIQUECER.md` en la raíz del
> repo y seguilo al pie de la letra. Enriquecé estos ítems en `src/content/`:
> **LIBROS:** <lista de slugs>. **REFERENTES:** <lista de slugs>.
> Reglas duras: nunca inventes un ASIN (dejá vacío si no lo confirmás); usá Read/Write, nunca `cat`;
> máximo 1-2 WebSearch por ítem; contenido original en castellano. Al terminar, anotá la tanda en
> `PROGRESO.md` y devolveme una tabla: ítem | qué hiciste | ASIN | dudas.
