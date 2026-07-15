# ENRIQUECER — mini-spec para subagente económico

Spec compacto y autosuficiente para enriquecer **fichas de libros** y **páginas de referentes**
con un modelo barato (Sonnet). Objetivo: bajar el costo en tokens vs hacerlo con Opus.
Es un extracto operativo de `CONTENIDO.md` (la fuente de verdad completa sigue siendo esa).

## Catálogo de acciones (índice rápido)

En una sesión alcanza con **nombrar la acción + el referente/categoría**; no hace falta
re-explicar el procedimiento (está en la sección que se indica). El modelo sugerido sale de la
Política de modelos. Toda acción respeta la **regla de propagación** (ver abajo).

| Acción | Qué hace | Entrada | Receta | Modelo |
| --- | --- | --- | --- | --- |
| **Enriquecer** | Ficha nueva o stub → ficha completa (reseña original + ASIN de edición ES) | slugs, o "los que consideres" | MODO LIBRO | Sonnet |
| **Discovery / barrido** | Encuentra más libros que recomienda un referente, extraídos de una fuente fetcheada → manifiesto | referente + su fuente | MODO DESCUBRIR | Haiku |
| **Reconciliar** | Clasifica un manifiesto vs el catálogo: YA-LINKED / CROSS-REF / REVISAR / NUEVO | ref-slug + manifiesto | `reconciliar.py` | script |
| **Cross-refs** | Suma un referente al `recomendadoPor` de fichas que ya existen (sube consenso) | salida CROSS-REF del reconciliar | MODO LIBRO (solo frontmatter) | Sonnet |
| **Profundizar** | Suma libros de un backlog YA sourceado (sin discovery nuevo) → reconciliar → enriquecer → regenerar listicle | referente con backlog en PROGRESO | Acción "Profundizar" | Sonnet |
| **Nuevo referente** | Pipeline completo desde cero: bio + discovery + reconciliar + enriquecer + listicle | nombre + fuente documentada | Acción "Nuevo referente" | Opus decide, Sonnet ejecuta |
| **Bio de referente** | Bio genérica autogenerada → bio real con fuente | slug del autor | MODO REFERENTE | Sonnet |
| **Listicle** | Post "Los libros que recomienda X" desde un manifiesto de fichas ya enriquecidas | referente | MODO LISTICLE | Sonnet |
| **Best-of de categoría** | Post "Mejores libros de \<categoría\>" (mismo formato que listicle) | categoría | MODO LISTICLE (variante) | Sonnet |
| **Verificar** | QA: duplicados + ASIN de 10 chars + integridad de `recomendadoPor` | — | Verificación | script |

**Regla transversal (propagación):** cualquier acción que cambie la lista de libros de un
referente que YA tiene listicle obliga a **regenerar ese listicle**. Ídem al sumar cross-refs.

## Política de modelos (qué tier para cada paso)

Regla base: **la inteligencia del motor vive en este spec y en los scripts, no en el orquestador.**
Por eso el hilo principal de producción NO necesita Opus. Elegí siempre el tier más barato que
haga el paso de forma confiable; si un tier barato se equivoca, el re-trabajo lo paga el tier caro.

- **Opus** — solo criterio y diseño: definir estrategia, elegir referente/lote, resolver casos
  `REVISAR` ambiguos, spot-check de los flags reportados, y debugging espinoso (git/mount). Bajo volumen.
- **Sonnet** — caballo de batalla: orquestar tandas de producción y, como subagente, la
  investigación + redacción (MODO LIBRO, MODO REFERENTE, MODO LISTICLE). Es el **piso de calidad**
  para cualquier cosa que escriba prosa o que decida ediciones/ASIN.
- **Haiku** — tareas mecánicas y de bajo juicio, como subagente o inline: MODO DESCUBRIR (extraer
  `título|autor` de una página YA fetcheada), pre-chequeo de ASINs (¿el ISBN-10 mapea al título en
  amazon.es?), redactar los `resumen` de una línea, clasificar `categoria`, proponer slugs.
  **NUNCA** para escribir reseñas ni para elegir el ASIN final (alucina más → costo neto mayor).
- **Scripts Python** (`reconciliar.py`, `detectar_duplicados.py`) — lo determinista, a **0 tokens**.
  Siempre que se pueda, preferí script sobre LLM.

Sesión de producción recomendada: abrí el chat principal en **Sonnet** (no Opus), que lee
`PENDIENTES.md` / `PROGRESO.md` / este spec y ejecuta una tanda despachando Haiku (manifiesto +
pre-chequeo) y Sonnet (redacción). Reservá sesiones Opus para criterio/diseño. **El handoff entre
sesiones son los archivos, no el chat** — por eso se mantienen al día religiosamente.

## Flujo (quién hace qué)

1. **Opus (criterio, 1 vez):** elige referente/lote y lanza. En descubrimiento, arma el manifiesto
   vía script (`reconciliar.py`) y decide los `REVISAR`.
2. **Haiku (mecánico):** MODO DESCUBRIR (extrae de la fuente fetcheada) y pre-chequeo de ASINs;
   devuelve manifiesto + excepciones. Barato y aislado.
3. **Sonnet (redacción):** por cada slug, investiga con `WebSearch`, edita/escribe el `.md` con
   Read/Write, y anota la tanda en `PROGRESO.md`.
4. **Script (bash/python, ~0 tokens):** valida ASIN / integridad / duplicados (ver "Verificación").
5. **Opus (spot-check):** revisa 1-2 fichas y las excepciones que le reportaron (no todo).

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

**Verificá que el libro EXISTA (antes que nada).** Confirmá que autor + título son una obra
publicada real (Amazon / Goodreads / Wikipedia / sitio del autor). Los stubs importados pueden
traer títulos erróneos o inexistentes. Si no lo confirmás, **NO escribas una reseña**: dejá la
ficha como stub y marcá la duda en la tabla de salida. Nunca inventes contenido alrededor de un
título que no se pudo verificar.

**Antes de declarar "solo inglés":** buscá con el probable título traducido (muchos libros de
negocios/psicología tienen edición en Conecta, Deusto, Empresa Activa, Paidós, etc.). Ej: "The
Culture Code" → "El código de la cultura". Solo usar la edición inglesa si de verdad no hay una ES.

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

> **Regla de propagación:** si enriquecés libros de un referente (o le sumás un vínculo por
> cruce) que **ya tiene listicle publicado**, hay que **regenerar ese listicle** (MODO LISTICLE)
> para que no quede desactualizado. Igual para los cruces: al agregar un vínculo referente↔libro,
> revisar si ese referente tiene listicle y refrescarlo.

---

## MODO REFERENTE (bio genérica → real)

Los archivos `autores/<slug>.md` con bio genérica ya traen la **fuente** identificada en la línea
"…rastrearse a través de <FUENTE>". Usar esa fuente; no inventar otras.

```yaml
---
nombre: "Nombre Apellido"        # no tocar
profesion: "Rol principal"        # ajustar si es impreciso (ej: "Cofundador de Microsoft")
bio: "1 frase natural con su credencial principal; se usa como meta description."
foto: "/referentes/<slug>.jpg"    # SOLO si ya existe el archivo; si no, NO agregar (hay monograma)
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

## MODO LISTICLE (post de blog "Los libros que recomienda X")

Se ejecuta **solo con un manifiesto** que provee Opus: una lista cerrada de fichas YA
enriquecidas para enlazar, con su `slug` y su `titulo` EXACTO. El subagente **no decide qué
enlazar ni inventa títulos**: usa el manifiesto tal cual. **Prohibido enlazar cualquier ficha
que no esté en el manifiesto** (así nunca se linkea un stub → regla dura del playbook §5).

Archivo nuevo: `src/content/blog/libros-que-recomienda-<slug-referente>.md`

Frontmatter:
```yaml
---
titulo: "Los libros que recomienda <Nombre> (guía 2026)"   # keyword + año
descripcion: "Meta ~150 chars con la keyword 'libros que recomienda <Nombre>'."
fecha: <hoy AAAA-MM-DD; confirmá con `date`>
fechaActualizado: <hoy>
autor: "Los Imperdibles"
keywords: ["libros que recomienda <Nombre>", "qué lee <Nombre>", "libros favoritos de <Nombre>"]
draft: false
---
```

Cuerpo (original, tono del sitio):
- Intro 2-4 frases: **keyword en la primera línea** + contexto real del referente y su fuente.
- **Organización (criterio ÚNICO): grupos TEMÁTICOS balanceados.** Todos los listicles se organizan
  por tema/género —**NUNCA** por año/mes—. La `categoria` de cada ficha es el punto de partida, pero
  la meta es el **balance**: ni un bloque gigante ni micro-secciones huérfanas. Reglas:
  - **Umbral:** con **8+ libros**, agrupá con `## <Grupo>`; con menos de 8, lista simple sin `##`.
  - **Apuntá a 3-6 grupos** de tamaño parejo (~3-8 libros c/u).
  - **Categoría dominante → subdividir:** si una `categoria` concentra muchos (p.ej. `ficcion` con
    20+), NO la dejes como un solo bloque: dividíla en **sub-temas editoriales** coherentes ("Novela
    histórica", "Identidad y diáspora", "Premiadas recientes", "Distopía y ciencia ficción"…), como
    ya hacen los listicles de Zuckerberg y Reese.
  - **Categoría mínima → fusionar:** si una `categoria` tiene 1-2 libros, metelos en un encabezado
    más amplio ("No ficción: memorias e historia") en vez de una sección minúscula.
  - **Lead opcional de conversión:** en listas largas, arriba un bloque `## Por dónde empezar` con
    3-4 destacados (los más fuertes / más vendidos); después, los grupos temáticos.
  - **Fecha del pick INLINE, nunca como eje** (book-clubs): "Pick de octubre 2023" dentro de la
    reseña. **Prohibido agrupar por año/mes.**
  - Nombres de grupo con keyword cuando se pueda; dentro de cada grupo, los más relevantes primero.
- Un ítem por libro del manifiesto: `### [<titulo EXACTO>](/libros/<slug>) — <autor>` + 2-3 frases
  (reescribí a partir del `resumen`/reseña de la ficha; no copies literal).
- Cierre con enlace a `/referentes` (y a `/categorias/<x>` si aplica).

Reglas duras:
- Enlazar SOLO los slugs del manifiesto, con el `titulo` EXACTO como texto del enlace.
- **Nunca** un link de afiliado en el post (solo internos: `/libros`, `/referentes`, `/categorias`).
- Keyword en título, H1 (=titulo) y primeras 1-2 líneas. Una sola página por keyword.
- `fecha` = hoy real. Contenido 100% original.

**Cómo arma Opus el manifiesto (determinístico, no alucinable):**
```bash
cd <repo>/src/content
REF=ryan-holiday   # slug del referente
for f in libros/*.md; do
  awk '/^recomendadoPor:/{g=1;next} g&&/^  - /{print} g&&/^[^ ]/{exit}' "$f" | grep -q -- "- $REF\$" || continue
  grep -q '^asin:' "$f" || continue   # SOLO fichas enriquecidas
  echo "slug=$(basename $f .md)"
  grep -m1 '^titulo:' "$f"; grep -m1 '^autorLibro:' "$f"; grep -m1 '^categoria:' "$f"; grep -m1 '^resumen:' "$f"
  echo "---"
done
```

## MODO DESCUBRIR (encontrar más libros de un referente)

Objetivo: dado un referente, encontrar **más libros reales** que recomienda, para agregarlos.
**Regla de oro:** el agente NO "recuerda" qué recomienda — **extrae de una fuente fetcheada**.
Recordar alucina; extraer de una página real casi no.

Reglas:
- Fetcheá fuentes reales: la lista/fuente oficial del referente (la línea "rastrearse a través
  de…" de su ficha en `autores/<slug>.md`) y/o artículos serios que la reproduzcan. Usá
  `WebSearch` para encontrarlas y `web_fetch` para leerlas.
- Extraé SOLO libros que aparezcan explícitamente en una fuente fetcheada. **Por cada libro,
  registrá la URL de la fuente.** Si no podés sourcear un libro, NO lo incluyas.
- **No escribas nada en el catálogo.** Devolvé solo un manifiesto: `título | autor | año | URL-fuente`.
- No inventes títulos, autores ni atribuciones. Ante la duda, omití. Es preferible una lista
  corta y 100% real que una larga con dudosos.

Después (lo hace Opus + un script, no el agente): **reconciliar** contra el catálogo con
`python3 tools/reconciliar.py <ref-slug> <manifiesto.txt> src/content/libros`. Clasifica cada
candidato en **YA-LINKED** (ya está, nada que hacer), **CROSS-REF** (el libro existe pero falta el
referente → agregar a `recomendadoPor`), **REVISAR** (el autor ya está pero el título no matchea →
Opus decide: ¿mismo libro traducido = cross-ref, o libro nuevo?) o **NUEVO** (crear ficha). El
match es por slug (el slug del catálogo deriva del título en inglés → resuelve el cross-idioma).
Opus verifica una muestra de atribuciones contra las URLs-fuente. Recién entonces se enriquece
(MODO LIBRO), y al terminar se corre el detector de duplicados (ver Verificación).

## Acción "Profundizar" (backlog ya sourceado)

Cuando un referente ya tiene un backlog de títulos sourceados (sección "Backlog" en su entrada de
`PROGRESO.md`), **no se hace discovery de nuevo** — ya están identificados. Flujo:

1. Extraé los títulos del backlog a un manifiesto `título|autor` (completá el autor con una
   búsqueda si el backlog trae solo el título).
2. `python3 tools/reconciliar.py <ref-slug> <manifiesto.txt> src/content/libros` → CROSS-REF
   (sumar el referente a la ficha existente) y NUEVO (crear ficha).
3. Enriquecé los NUEVO con MODO LIBRO. **Ojo:** los títulos recientes pueden no tener edición ES
   todavía → NO los cargues; dejalos en una lista aparte "solo-inglés / a decidir" (el sitio
   prioriza amazon.es, físico en español).
4. `detectar_duplicados.py`.
5. **Regenerá el listicle** del referente (MODO LISTICLE) — la lista cambió.
6. Asentá la tanda en `PROGRESO.md`.

## Acción "Nuevo referente" (pipeline completo)

Sumar un referente desde cero (así se hizo Dua Lipa). Requiere una **fuente documentada y
fetcheable** de sus recomendaciones (club de lectura, lista oficial, blog). Sin fuente sólida, no
se agrega (riesgo de alucinación).

1. **Bio:** creá `autores/<slug>.md` (MODO REFERENTE), `orden: 50`, profesión y bio reales con la
   fuente. Sumá su ámbito en `src/lib/ambitos.ts`.
2. **Discovery:** MODO DESCUBRIR sobre la fuente → manifiesto `título|autor|año|URL`.
3. **Reconciliar:** `reconciliar.py <slug> <manifiesto>` → CROSS-REF + REVISAR + NUEVO.
4. **Presentá el manifiesto reconciliado** antes de enriquecer en masa (decisión de Opus/usuario:
   cuántos y cuáles, priorizando ediciones ES confirmadas).
5. **Enriquecé** los NUEVO por tandas de ~8 (MODO LIBRO) + los CROSS-REF (frontmatter).
6. **Verificá:** `detectar_duplicados.py` + spot-check de 1-2 fichas.
7. **Listicle** del referente (MODO LISTICLE).
8. **Asentá** cada tanda en `PROGRESO.md` y actualizá los conteos en `PENDIENTES.md`
   (referentes, libros, blog).

## Verificación (correr al terminar cada lote)

```bash
cd <repo>/src/content
# ASIN de 10 chars en las fichas tocadas:
for f in libros/<slug1>.md libros/<slug2>.md; do a=$(grep -m1 '^asin:' "$f"|sed 's/asin: //;s/"//g;s/ //g'); echo "${#a} $f"; done
# Integridad recomendadoPor -> autor existente:
for f in libros/*.md; do awk '/^recomendadoPor:/{g=1;next} g&&/^  - /{gsub(/  - /,"");print} g&&/^[^ ]/{exit}' "$f" | while read r; do [ -f "autores/$r.md" ] || echo "FALTA $r en $f"; done; done
```

Detector de duplicados (correr **después de cada barrido de descubrimiento**):
```bash
python3 tools/detectar_duplicados.py src/content/libros
```
Reporta `[DUP]` (mismo autor+título → duplicado casi seguro, corregir) y `[REV]` (autores con 2+
libros, informativo). Casos conocidos aceptados en `[REV]`: las dos ediciones de las cartas de
Séneca (Cartas de un estoico / Cartas a Lucilio) y Foundation / The Foundation Trilogy.

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
