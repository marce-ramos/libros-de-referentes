# Playbook de contenido — Los Imperdibles

Guía de convenciones para agregar y mantener contenido del sitio con consistencia.
Léela antes de crear o enriquecer libros, referentes o artículos. Es la fuente de
verdad de "cómo se hace acá".

> Marca: **Los Imperdibles** · dominio: losimperdibles.com · idioma: español (Argentina).
> Tono: cercano pero informado ("un amigo que sabe"). Nada de promesas de dinero fácil.

---

## 1. Modelo de datos

Cuatro colecciones en `src/content/` (esquemas en `src/content.config.ts`):

- **autores** — los referentes (Gates, Obama, etc.). 1 archivo `.md` por referente.
- **libros** — 1 archivo `.md` por libro.
- **categorias** — 1 archivo `.md` por categoría.
- **blog** — artículos editoriales.

Las páginas se generan solas desde el contenido. Para sumar contenido casi nunca hay
que tocar código: se agregan archivos `.md`.

### Slugs

El nombre del archivo (sin `.md`) es el slug y la URL. Regla: minúsculas, sin acentos,
espacios y símbolos → guiones. Ej: "Un caballero en Moscú" → `un-caballero-en-moscu`
(pero si el archivo ya existe con otro slug, **no lo renombres**: rompe URLs indexadas).

### Categorías vigentes (slug → nombre)

`historia` → Historia · `negocios` → Negocios e Inversión · `ciencia` → Ciencia y
Tecnología · `memorias` → Memorias y Biografías · `ficcion` → Ficción · `psicologia` →
Psicología y Hábitos · `filosofia` → Filosofía y Estoicismo · `cienciaficcion` →
Ciencia Ficción · `espiritualidad` → Espiritualidad.

Si un libro no encaja, preferí la categoría más cercana antes de crear una nueva
(categorías con 1 solo libro se ven pobres).

---

## 2. Ficha de libro (`src/content/libros/<slug>.md`)

### Frontmatter

```yaml
---
titulo: "Título en español (o inglés si no hay edición en español)"
autorLibro: "Autor del libro"          # no confundir con el referente
asin: "XXXXXXXXXX"                       # 10 caracteres alfanuméricos. Opcional.
categoria: negocios                      # slug de una categoría existente
recomendadoPor:                          # slugs de autores existentes
  - warren-buffett
anio: 1949                               # opcional
resumen: "1-2 frases para meta y listados."
destacado: false                         # true solo para libros muy fuertes (home)
fechaActualizado: 2026-07-05
---
```

### Cuerpo (dos niveles de calidad)

- **Reseña completa** (libros top / muy buscados): intro que engancha + secciones
  `## Por qué lo recomienda X` · `## De qué trata` · `## <idea/concepto clave>` ·
  `## Para quién es` · (opcional `## Veredicto`). ~350-500 palabras, original.
- **Intro breve** (el resto): 3 secciones cortas — intro + `## Por qué lo recomienda X`
  + `## De qué trata`. ~120-180 palabras.

Nunca dejar el stub auto-generado ("*X*, de Y, figura entre las recomendaciones de Z.").

### Nota de edición (última línea del cuerpo, en blockquote)

- Con edición en español: `> Edición en español: *Título*, Editorial (traducción de …).`
- Sin edición en español: `> Por ahora disponible solo en inglés; el enlace lleva a la edición de <Editorial>.`

---

## 3. ASIN y edición (regla de oro)

1. **Nunca inventar un ASIN.** Un ASIN equivocado linkea a un producto incorrecto
   (malo para el lector y contra la política de Amazon).
2. Preferir **edición en español** si existe; si no, la inglesa.
3. Buscar en la web: `"<título español>" <autor> edición español ISBN Amazon`.
   El ASIN suele ser el **ISBN-10** de la edición impresa y aparece en las URLs de
   Amazon (`/dp/XXXXXXXXXX`). Verificar que tenga **10 caracteres** alfanuméricos.
4. Si no se consigue un ASIN confiable, **dejar `asin` vacío**: el botón usa el
   fallback de búsqueda (`urlAfiliado` en `src/lib/amazon.ts`), que siempre funciona
   y lleva el tag. Reemplazar por el ASIN real cuando se pueda.
5. Las **portadas reales** solo se muestran vía la PA-API de Amazon (se habilita tras
   3 ventas). Hasta entonces, placeholders. No scrapear ni hotlinkear portadas.

---

## 4. Referente (`src/content/autores/<slug>.md`)

```yaml
---
nombre: "Nombre Apellido"
profesion: "Rol principal, ej: Cofundador de Microsoft"
bio: "1 frase (se usa en la meta description)."
foto: "/autores/<slug>.jpg"    # opcional; imágenes de referentes: ver §7
destacado: false               # true para figuras grandes (aparece en la home)
orden: 50
---

<2-3 frases sobre el referente y por qué seguimos sus recomendaciones,
con la fuente de sus listas (blog, book club, cartas, etc.).>
```

**Solo referentes con fuente verificable** (book club oficial, blog/reading list,
newsletter, fundación, cartas a accionistas). Evitar los de fuente vaga
("entrevistas/redes") salvo que la recomendación esté bien documentada.

`recomendadoPor` en los libros usa el **slug del autor** (nombre-apellido). Si un
libro lo recomiendan varios, se listan todos (relación muchos-a-muchos → interlinking).

Al agregar un referente, sumá su slug + **ámbito** en `src/lib/ambitos.ts` (Tecnología,
Negocios e Inversión, Escritores, Psicología, Entretenimiento, Política y Sociedad, Ciencia).
Es lo que alimenta el buscador y los filtros de `/autores` (client-side sobre tarjetas ya
renderizadas → SEO-safe; nada de búsqueda por API ni paginación que oculte contenido del HTML).

---

## 5. Blog y estrategia editorial

El blog es el motor de tráfico de cola larga. Cada artículo apunta a una búsqueda con
intención y enlaza a fichas internas (nunca directo a Amazon).

### Frontmatter (todos los posts)

```yaml
---
titulo: "Título con la keyword (y el año en las listas: … 2026)"
descripcion: "Meta description con la keyword (~150 caracteres)."
fecha: 2026-07-05
fechaActualizado: 2026-07-05
autor: "Los Imperdibles"
keywords: ["keyword principal", "variante", "…"]
draft: false
---
```

### Reglas de SEO comunes a todo artículo

- **Fechas reales:** `fecha` = el día real en que se publica el post; `fechaActualizado` =
  el día del último cambio real. No inventar ni reciclar fechas viejas (Google las muestra y
  usa como señal de frescura). Confirmar el día de hoy con `date` si hace falta.
- **Keyword principal** en el título, en el H1 (= `titulo`) y en las primeras 1-2 líneas.
- Estructura **escaneable**: un `##` por sección/ítem, párrafos cortos, respuesta arriba.
- **Enlaces internos** a fichas (`/libros/<slug>`), referentes (`/autores/<slug>`) y
  categorías (`/categorias/<slug>`). **Nunca** un link de afiliado directo en el post.
- **Una sola página por tema** (evitar canibalización: no dos posts peleando la misma keyword).
- Contenido **100% original**; el título del enlace debe coincidir con el `titulo` de la ficha.

> ⛔ **Regla dura — nunca publicar una entrada de blog hacia fichas sin enriquecer.**
>
> Un artículo **solo** puede enlazar a fichas **enriquecidas**. Publicar un post que apunte
> a stubs manda tráfico a páginas flojas y rompe el embudo (blog → ficha → Amazon).
>
> **Orden obligatorio:** primero se **enriquecen las fichas**, después se escribe el artículo
> que las enlaza. Al elegir sobre qué referente/tema escribir, priorizar aquellos cuyas fichas
> ya estén enriquecidas (o enriquecerlas antes). Verificar cada ficha enlazada contra el
> checklist (§8) **antes** de publicar el post.
>
> - **Ficha enriquecida** = cuerpo con reseña completa o intro real (no el stub
>   auto-generado) **y** `asin` real de 10 caracteres (o, si no hay ASIN confiable, edición
>   identificada + nota de edición).
> - **Stub** = cuerpo de una sola línea ("*X*, de Y, figura entre las recomendaciones de Z")
>   y/o sin `asin`. No se enlaza desde el blog hasta enriquecerlo.

### Arquetipos de artículo

1. **Listicle de referente** — "Los libros que recomienda <X>". El más importante.
   Intro + contexto del referente + un `### [Título](/libros/<slug>) — Autor` por libro
   (2-3 frases). Agrupar por tipo si son muchos (Ficción / No ficción). Cierre → `/autores`.
2. **Best-of por categoría** — "Los mejores libros de <tema> según los referentes".
   Selecciona los top de una categoría (los de más consenso primero); enlaza a la
   categoría y a cada ficha.
3. **Guía estacional / de regalo** — "Libros para regalar 2026", "Mejores libros en
   oferta este Black Friday". Publicar **semanas antes** para que Google lo indexe a
   tiempo. Alta intención de compra.
4. **Reseña individual en profundidad** — artículo editorial largo sobre un solo libro
   (ángulo, contexto, por qué importa) que enlaza a su ficha. Para libros muy buscados.
5. **Cola larga (referente × tema)** — "El mejor libro de inversión según Warren Buffett",
   "Qué libros de IA recomienda Sam Altman". Baja competencia, alta intención: ideal para
   un sitio nuevo. Producir muchos, chicos.
6. **Comparativa** — "<Libro A> vs <Libro B>: cuál leer primero". Nicho, buena conversión.

### Cadencia y frescura

- Lanzamiento: priorizar arquetipos 1 y 5 (bajan competencia).
- Ritmo sostenible: 2-3 posts/semana al crecer; 1-2 al madurar + actualizar viejos.
- **Refresco anual (cada enero):** actualizar las listas de referentes con los libros del
  año nuevo, cambiar el año del título y `fechaActualizado`. Suele rendir más que un post
  nuevo (Google premia la frescura).
- Revisar en Search Console los posts en **posición 5-15** y mejorarlos para empujarlos al
  top 3 (ahí está casi todo el tráfico).

---

## 6. Reglas de Amazon / SEO (no romper)

- **Disclosure** de afiliados visible (ya está en el footer del sitio).
- **Sin precios a mano** (cambian; solo vía PA-API).
- **Contenido original** con análisis propio (Amazon 2026 + Helpful Content de Google).
  No pegar sinopsis del editor ni repetir la misma reseña en varias páginas.
- Links de afiliado con `rel="sponsored nofollow noopener"` (ya lo hace `BotonAfiliado`).
- eBooks Kindle sueltos **no comisionan**: monetización = libro físico + bounties de
  Audible/Kindle Unlimited. El link de Kindle es conveniencia + cookie de 24 h.

---

## 7. Componentes y diseño (para no romper la estética)

- `PortadaLibro.astro` — cover. Placeholder muestra el **título en el lomo**; con
  `showTitle={false}` el lomo va limpio (usar cuando el título ya está al lado).
  Con portada real (`portada`), muestra la imagen. Tamaños: `card`, `feat`, `full`, `shelf`.
- `LibroEstante.astro` — celda de estante: portada + repisa + etiqueta. Con placeholder,
  el título va en el lomo; con portada real, se muda a la etiqueta (autor y pill siempre abajo).
- **Badge de consenso**: no se pone sobre la portada (tapa). Se comunica con el
  **pill "N referentes"** (solo 2+) y ordenando las listas por cantidad de referentes.
- Home: sección **"Los más recomendados"** (2+ referentes, ranking) arriba, luego
  **"Explorá por tema"** (estantes por categoría).
- Paleta: lavanda/púrpura (`--brand #6c5ce7`), serif **Fraunces** para títulos.
- **Imágenes de referentes**: `AvatarReferente.astro` muestra la `foto` si existe, o un
  **monograma** (iniciales) como fallback automático. No usar fotos de Amazon. Para fotos
  reales: Wikimedia Commons (CC, con atribución) — solo setear `foto: "/autores/<slug>.jpg"`.

---

## 8. Checklist de verificación (antes de publicar)

- [ ] `categoria` apunta a una categoría existente.
- [ ] Cada `recomendadoPor` es un slug de autor existente.
- [ ] `asin` (si hay) tiene 10 caracteres alfanuméricos.
- [ ] El cuerpo no es un stub (tiene reseña o intro real).
- [ ] Título en español si existe edición; nota de edición al pie.
- [ ] Los enlaces internos del blog apuntan a fichas saneadas.
- [ ] `npm run build` compila sin errores.

### Gotcha de herramientas

El filesystem que ve `bash` (mnt) puede quedar **desincronizado** y mostrar versiones
viejas/truncadas. Para verificar el contenido real de un archivo, usar las herramientas
**Read/Write/Edit** (operan sobre los archivos reales), no `cat` de bash.

---

## 9. Flujo para agregar/enriquecer un libro (resumen)

1. Elegir el libro y el/los referente(s) que lo recomiendan (fuente verificable).
2. Buscar edición en español + ASIN (§3). Verificar 10 chars.
3. Asignar categoría (§1).
4. Escribir cuerpo (reseña completa o intro, §2), original y en el tono del sitio.
5. Nota de edición al pie.
6. Correr el checklist (§8) y `npm run build`.
7. **Asentar la tanda en `PROGRESO.md`** (bitácora append-only): fecha, qué se enriqueció o
   publicó, y el global de fichas. Actualizar también los conteos en `PENDIENTES.md`.
8. `git add . && git commit && git push` (deploy automático en Cloudflare).

---

## 10. Calendario editorial (plan de arranque)

Orden de producción sugerido, de mayor a menor retorno para un sitio nuevo. Antes de
cada listicle, enriquecer las fichas que va a enlazar (§8) — nunca publicar hacia stubs.

**Fase 1 — Listicles de referentes (base).** Un post por referente grande (arquetipo 1).
- Hechos: Bill Gates, Barack Obama, Warren Buffett.
- Próximos: Elon Musk, Naval Ravikant, Tim Ferriss, Jordan Peterson, Ray Dalio,
  Sam Altman, Andrew Ng. (~2-3 por semana.)

**Fase 2 — Best-of por categoría (arquetipo 2).** Uno por categoría fuerte:
"Los mejores libros de negocios / psicología / ciencia según los referentes".
Reutiliza fichas ya enriquecidas.

**Fase 3 — Cola larga (arquetipo 5).** Combinaciones referente × tema: muchos posts
chicos, baja competencia ("El mejor libro de X según Y").

**Estacional (todo el año, con anticipación):**
- Oct-Nov: Black Friday / Cyber Monday ("mejores libros en oferta").
- Dic-Ene: "Libros para regalar" + listas anuales ("Todos los libros que recomendaron
  los referentes en 2026").
- Abril: Día del Libro (23/4) y vuelta a clases.

**KPI de contenido:** el termómetro temprano no son los ingresos sino las **impresiones
en Search Console**. Si suben mes a mes, el contenido funciona y los ingresos vienen detrás.
