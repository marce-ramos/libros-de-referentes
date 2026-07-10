# Los Imperdibles — Estado y pendientes

Punto de retomada. Última actualización: 2026-07-05.

---

## ✅ Hecho

- **Sitio en vivo:** losimperdibles.com (Astro + Tailwind, Cloudflare Pages, auto-deploy en cada `git push`).
- **Dominio propio** comprado en Cloudflare y conectado.
- **Diseño "Estantes claros"** (lavanda + serif Fraunces): home con *Los más recomendados*
  (ranking por consenso) arriba y *Explorá por tema* (estantes por categoría) abajo.
  Pill "N referentes" (2+), orden por cantidad de referentes, portadas placeholder inteligentes.
- **Contenido:** 39 referentes, 142 libros, 9 categorías. **68 libros con ASIN real + reseña/intro**
  (tandas 2026-07-09: Ray Dalio, Mark Zuckerberg, 5 "remates" [Gates, Altman, Clear, Thiel,
  Duckworth], Harari 3/3, Kahneman 3/3, Ryan Holiday 4/4, + Naval 4/4, Andrew Ng 3/3).
- **Blog:** 8 artículos (Gates, Obama, Buffett, Musk, Jordan Peterson, Tim Ferriss, Ray Dalio,
  Mark Zuckerberg), con las fichas que enlazan saneadas.
- **Google Search Console:** verificado + sitemap enviado (el reloj del SEO ya corre).
- **Imagen OG** con la marca.
- **Playbook** `CONTENIDO.md`: convenciones de contenido + estrategia editorial + calendario.

---

## ⏭️ Pendientes / próximos pasos

1. **Amazon Afiliados (monetización).** Darse de alta *cuando haya algo de tráfico* (regla:
   3 ventas en 180 días o cierran la cuenta). Poner el **tag real** en `src/config.ts`
   (hoy placeholder `turef-20`). Activar **OneLink**. Cargar el **bounty de Audible** real
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
3. **Enriquecer más fichas** de a tandas (quedan ~110 en stub/placeholder): ASIN real +
   reseña/intro, siguiendo el playbook.
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
- Programa: **Amazon.com (US)** como base + OneLink; cobro desde Argentina vía Payoneer.
- Diseño: **Estantes claros** (lavanda + Fraunces).
- Consenso: **pill "N referentes"** (no badge sobre la portada) + **orden por cantidad**.
- Libros escritos por el propio referente: se dejan como recomendación.
- Solo referentes de **fuente verificable**.

---

## ⚠️ A verificar / flags abiertos

- **Cobro desde Argentina** (Payoneer/cuenta USD) — confianza media, confirmar condiciones.
- **Comisión de eBooks Kindle = 0** — verificar en el panel de Amazon.
- **Tag de afiliado** real pendiente (hoy `turef-20` placeholder).
- **Poor Charlie's Almanack** — linkea a edición inglesa (la española de Valor Editions
  no se confirmó en Amazon).
- **Gotcha de herramientas:** el filesystem de `bash` puede desincronizarse y mostrar
  versiones viejas/truncadas → verificar contenido con Read/Write, no con `cat`.
