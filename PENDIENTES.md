# Los Imperdibles — Estado y pendientes

Punto de retomada. Última actualización: 2026-07-12 (Profundizar Bill Gates: backlog de 11
cerrado, Gates 23 → 34 libros, listicle regenerado).

**Acciones/comandos disponibles:** `ACCIONES.md` (referencia rápida de una línea) · `ENRIQUECER.md` (detalle + reglas).

---

## ✅ Hecho

- **Sitio en vivo:** losimperdibles.com (Astro + Tailwind, Cloudflare Pages, auto-deploy en cada `git push`).
- **Dominio propio** comprado en Cloudflare y conectado.
- **Diseño "Estantes claros"** (lavanda + serif Fraunces): home con *Los más recomendados*
  (ranking por consenso) arriba y *Explorá por tema* (estantes por categoría) abajo.
  Pill "N referentes" (2+), orden por cantidad de referentes, portadas placeholder inteligentes.
- **Contenido:** **40 referentes al 100%** (los 39 originales + **Dua Lipa**, completado
  2026-07-12), **205 libros, 9 categorías**. Bill Gates profundizado 2026-07-12: backlog de 11
  libros cerrado (23 → 34). Detalle de todas las tandas y barridos en `PROGRESO.md`.
- **Rutas:** la sección de referentes se renombró de `/autores` a **`/referentes`** (2026-07-12),
  con redirects 301 en `public/_redirects` (`/autores/*` → `/referentes/:splat`) para preservar
  las URLs ya indexadas. (Una futura sección de autores del libro debe ir en `/escritores`, no
  `/autores` — ver Decisiones.)
- **Blog:** 14 artículos — 13 listicles de referente (Gates, Obama, Buffett, Musk, Jordan
  Peterson, Tim Ferriss, Ray Dalio, Mark Zuckerberg, Ryan Holiday, Sam Altman, Naval Ravikant,
  Yuval Noah Harari, Dua Lipa) + 1 best-of de categoría (Negocios e Inversión). Todas las fichas
  enlazadas están saneadas.
- **Bitácora de avance:** `PROGRESO.md` (append-only) — historial fechado de cada tanda de
  enriquecimiento y cada listicle. Actualizar SIEMPRE ahí al enriquecer o publicar.
- **Google Search Console:** verificado + sitemap enviado (el reloj del SEO ya corre).
- **Imagen OG** con la marca.
- **Playbook** `CONTENIDO.md`: convenciones de contenido + estrategia editorial + calendario.

---

## ⏭️ Pendientes / próximos pasos

1. **Amazon Afiliados (monetización).** Programa **BASE: amazon.es** (España) — es donde
   está el tráfico (ver GSC) y las ediciones en español son nativas. Comisión **libros = 7%**
   (vs. 4,5% en EE.UU.), verificado en el schedule oficial (afiliados.amazon.es, oct/2025).
   Darse de alta *cuando haya algo de tráfico* (regla: **3 ventas en 180 días** o cierran la
   cuenta, por programa). Poner el **tag real** de .es en `src/config.ts` (hoy placeholder
   `losimperdibles-21`; los tags de España terminan en `-21`). El código ya apunta a
   `www.amazon.es` de base (`src/lib/amazon.ts`). Luego activar **OneLink** para derivar el
   goteo internacional (US/MX) a su tienda local. Cobro desde Argentina: **Takenos** (0% punta
   a punta, umbral 10 EUR) o **Belo** (0,5%); a mayor volumen, **Wallbit + Santander** vía
   **Factura E** (exportación de servicios, 1% tasa plana). Cargar el **bounty de Audible** real
   en `BloqueAudible.astro`.
2. **Blog — seguir el calendario (§10 de CONTENIDO.md).** Fase 1: listicles de referentes
   → hechos: Musk, Jordan Peterson, Tim Ferriss, **Ray Dalio, Mark Zuckerberg** (2026-07-09).
   **Listos para listicle (fichas 100% enriquecidas, falta escribir el post): Sam Altman 4/4,
   James Clear 4/4, Peter Thiel 3/3, Angela Duckworth 3/3, Yuval Noah Harari 3/3,
   Daniel Kahneman 3/3, Ryan Holiday 4/4, Naval Ravikant 4/4, Andrew Ng 3/3.**
   Próximos a enriquecer (empezados a medias): Adam Grant, Simon Sinek, Satya Nadella,
   Lex Fridman, Vitalik Buterin, Malala, Kasparov; sin arrancar: Jeff Bezos, Nassim Taleb,
   Neil deGrasse Tyson, Malcolm Gladwell, Oprah, etc.
   Después: best-of por categoría, cola larga (referente × tema), y estacional.
   *Enriquecer las fichas antes de enlazarlas.*
3. ~~**Enriquecer más fichas**~~ ✅ **HECHO (2026-07-10): catálogo 100% enriquecido, 0 stubs.**
   Además se construyó el motor de subagente barato (`ENRIQUECER.md`, `tools/`) y se corrieron
   barridos de descubrimiento (Obama, Gates) que sumaron libros nuevos. Gates profundizado por
   completo el 2026-07-12 (backlog en 0). Backlog sourceado pendiente en `PROGRESO.md`:
   **Obama ~12**.
4. **Imágenes de referentes.** ✅ Monogramas hechos (`AvatarReferente.astro`, fallback
   automático). Próximo: sumar **fotos de Wikimedia Commons (CC)** donde existan, con
   página de créditos (setear `foto` en cada autor). Opcional: set de **ilustraciones**.
   (Ojo derecho de imagen: uso editorial, no endorsement.)
5. **Newsletter.** Elegir ESP (MailerLite o Kit) → generar **PDF lead magnet** desde el
   catálogo → componente de formulario (footer + fin de artículos + `/newsletter`) →
   automatización de bienvenida + **RSS-to-email**. Regla: **sin links de afiliado en emails**
   (linkear al sitio).
6. **PA-API (Product Advertising API).** Cuando lleguen las 3 ventas: portadas reales +
   precios actualizados automáticos. Ahí las estanterías/tarjetas "florecen" (el título se
   muda a la etiqueta; se puede sumar badge de consenso en la esquina).
7. **Search Console (continuo).** Pedir indexación de URLs nuevas; vigilar **impresiones**
   (KPI temprano); mejorar posts en posición 5-15.
8. ~~**"Los más recomendados" — capar + página propia.**~~ ✅ **Hecho (2026-07-09).**
   Home ahora muestra solo el **top 6** + link **"Ver el ranking completo (N) →"**. Nueva
   página **`/mas-recomendados`** lista TODOS los libros de 2+ referentes, agrupados por
   tramos ("Recomendados por N referentes", de mayor a menor). Card extraída a componente
   reusable **`TarjetaRecomendado.astro`** (home + ranking). SEO: H1, meta description,
   JSON-LD ItemList + BreadcrumbList, interlinking a fichas. Link **"Más recomendados"**
   agregado al nav del header (1er ítem) y a una fila de links en el footer (internal linking
   sitewide). Cada tramo tiene **paginado progresivo "Ver más"** (revela de a 8, todo el HTML
   se renderiza igual → SEO-safe).
9. **Diversificación (más adelante).** Display ads (AdSense/Mediavine) con tráfico; sponsors
   de newsletter; producto digital propio; micro-SaaS en Azure/.NET.

---

## 🧭 Decisiones tomadas (no re-discutir salvo que cambie algo)

- Marca: **Los Imperdibles** · dominio losimperdibles.com.
- Stack: **Astro + Tailwind + Cloudflare Pages**.
- Programa: **Amazon.es (España) como base** (ahí está el tráfico y las ediciones en español;
  libros **7%** > 4,5% de US) + **OneLink** para el goteo internacional. Lo opera **Amazon
  Europe Core Sàrl (Luxemburgo)**, así que como no residente **no se tributa en España**;
  la obligación fiscal vive en **Argentina** (exportación de servicios / Factura E). Cobro:
  **Takenos** (0%) o **Belo** (0,5%), umbral 10 EUR; a mayor escala Wallbit + Santander.
  *(Antes se había asumido Amazon.com US como base — se cambió tras ver el tráfico en GSC.)*
- Diseño: **Estantes claros** (lavanda + Fraunces).
- Consenso: **pill "N referentes"** (no badge sobre la portada) + **orden por cantidad**.
- Libros escritos por el propio referente: se dejan como recomendación.
- Solo referentes de **fuente verificable**.
- Ruta de referentes: **`/referentes`** (renombrada desde `/autores` con 301 permanente el
  2026-07-12; `public/_redirects`). ⚠️ **Una futura sección de autores del libro (escritores) NO
  debe colgar de `/autores`:** el redirect catch-all `/autores/*` → `/referentes/:splat` la
  secuestraría, y los 301 quedan cacheados de forma persistente. Para esa sección usar una ruta
  distinta, **`/escritores`** (recomendada: separa "quién recomienda" de "quién escribió", y suma
  la keyword "libros de <escritor>"). Modelo de datos: derivarla de los `autorLibro` distintos.

---

## ⚠️ A verificar / flags abiertos

- ~~**Cobro desde Argentina**~~ ✅ Resuelto (2026-07-12): **Takenos** (IBAN europeo virtual,
  0% punta a punta, umbral 10 EUR) como opción principal; **Belo** (0,5%) alternativa; a
  volumen alto **Wallbit + Santander** con Factura E (1%). Cheque físico descartado.
- ~~**Comisión de eBooks Kindle = 0**~~ ✅ Resuelto (2026-07-12): en **amazon.es**, tanto los
  **libros físicos como los eBooks Kindle DE PAGO comisionan al 7%** (schedule oficial, tabla de
  categorías). El **0% solo aplica** a afiliados de instituciones educativas o a quienes
  promocionan principalmente **eBooks Kindle GRATIS** (regla anti-spam) — ninguno es el caso.
- ~~**Tag de afiliado** real pendiente~~ Pendiente el alta, pero el placeholder ya es de .es
  (`losimperdibles-21`, tags de España terminan en `-21`); el código apunta a `www.amazon.es`.
- ~~**Poor Charlie's Almanack** — linkea a edición inglesa~~ ✅ Resuelto (2026-07-10): la
  edición española de Valor Editions ya está en Amazon (asin B0F8J6F85F); la ficha ahora la
  linkea y la nota quedó en formato estándar.
- **Gotcha de herramientas:** el filesystem de `bash` puede desincronizarse y mostrar
  versiones viejas/truncadas → verificar contenido con Read/Write, no con `cat`.
