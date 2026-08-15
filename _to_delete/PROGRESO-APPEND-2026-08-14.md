
- **2026-08-14 — Auditoría del catálogo + tanda de saneado (7 frentes) + sincronización de la
  bitácora.** Sesión de criterio (Opus) con 6 subagentes Sonnet en paralelo para la ejecución.

  **0. Corte auditado del catálogo (contado sobre `src/content/**`, no estimado).**
  **974 fichas · 44 referentes · 45 posts de blog (43 listicles de referente + 2 best-of) ·
  9 categorías · 1.133 vínculos libro↔referente · 108 fichas con 2+ referentes (11%) ·
  347 fichas marcadas "solo en inglés" (36%) · 0 stubs · 0 fichas sin `resumen` o sin
  `recomendadoPor`.** Distribución por categoría: ficcion 395, negocios 115, memorias 106,
  psicologia 102, ciencia 87, historia 81, filosofia 49, cienciaficcion 26, espiritualidad 13.
  Podio de consenso: Sapiens (7); El hombre en busca de sentido, Meditaciones, Cien años de
  soledad, Pensar rápido pensar despacio y De cero a uno (5 c/u).

  **⚠️ Deriva de documentación detectada.** `PENDIENTES.md` venía declarando **556 libros / 35
  posts** — el catálogo real era 974 / 45. Las tandas del **2026-08-06 al 2026-08-10** se
  ejecutaron sin asentarse acá: por fechas de archivo y por las memorias de sesión corresponden a
  Marc Andreessen (32 libros, listicle 08-07), Ryan Holiday (39, listicle 08-06), Brené Brown
  (24, listicle 08-08), Lex Fridman (17, listicle 08-08), Paul Graham (34, listicle 08-09),
  Neil deGrasse Tyson (14, listicle 08-09), Simon Sinek (15, listicle 08-09), Nassim Taleb
  (11, listicle 08-09), Garry Kasparov (13, listicle 08-10), Gwyneth Paltrow (14, listicle 08-10)
  y el **best-of de psicología** (25 títulos, 08-09). **Confianza en esta reconstrucción: media** —
  los conteos del catálogo son exactos, la atribución de qué tanda sumó qué libro no se puede
  recuperar. Los detalles por ficha de esas tandas se perdieron.

  **1. `src/lib/ambitos.ts` — Dua Lipa.** Faltaba su entrada desde el alta del 2026-07-12: un
  referente de 34 libros quedaba fuera del filtro de `/referentes`. Agregada como
  `"dua-lipa": "Entretenimiento"`. Ámbitos ahora: Tecnología 9 · Negocios e Inversión 10 ·
  Escritores 8 · Entretenimiento 7 · Psicología 5 · Política y Sociedad 3 · Ciencia 2 (44/44).

  **2. Listicles desfasados por cross-refs no propagados.** Detectados comparando, por referente,
  el `recomendadoPor` del catálogo contra los slugs enlazados en su post.
  - **Brené Brown 20 → 24:** sumados *Los dones de la imperfección* y *Atrévete a liderar* (libros
    propios, según la decisión "los libros del propio referente se dejan como recomendación") y
    creado un grupo nuevo **"Creatividad y coraje para crear"** con *Libera tu magia* (Elizabeth
    Gilbert) y *El acto de crear* (Rick Rubin), que no entraban en ningún grupo existente.
  - **Simon Sinek 13 → 15:** sumados *Empieza con el porqué* (en "Liderazgo real, contado desde
    adentro") y *El juego infinito* (en "Filosofía del largo plazo y del sentido", justo después de
    *Juegos finitos y juegos infinitos* de Carse, que es su fuente declarada).
  - **Ryan Holiday: NO se tocó, y es correcto.** Le "falta" *El obstáculo es el camino*, pero la
    intro del post dice explícitamente "no vas a encontrar acá *El obstáculo es el camino* ni el
    resto de sus propios libros". Es una decisión editorial declarada, no un desfasaje. **Dejar
    así**: sumarlo contradiría el texto del propio post.

  **3. Listicle de Malala Yousafzai — nuevo.** Era el único referente sin post. Con 3 libros va en
  **lista simple sin grupos** (umbral de MODO LISTICLE = 8): *Americanah*, *Tiene que ser aquí* y
  *El alquimista*. Fuente citada: su club Fearless, ligado al Malala Fund (la misma que ya estaba
  en `autores/malala-yousafzai.md`); no se inventaron picks nuevos. **Blog: 45 → 46 artículos.
  Los 44 referentes tienen listicle.**

  **4. ASINs faltantes: 36 fichas, no 12.** El chequeo anterior contaba `asin: ""` como campo
  presente; el conteo real de fichas sin ASIN usable era 36 (algunas con `asin: ""`, otras sin la
  línea `asin:` directamente). **29 resueltos** vía 5 subagentes Sonnet en paralelo (búsqueda del
  ISBN-10 con fuente por ítem) + 2 resueltos a mano (`lost-and-found` 0525512462 Random House,
  `mr-putin` 0815723768 Brookings) = **31 de 36. Catálogo: 970/974 fichas con ASIN de 10
  caracteres (99,6%).** Los ASIN puestos: a-very-expensive-poison 1783350946 · apollo-s-arrow
  0316628212 · be-the-boss-everyone-wants-to-work-for 1626566259 · benjamin-franklin-an-american-life
  074325807X · china-room 0670095079 · culture-renovation 1260464369 · dvoretsky-s-endgame-manual
  1888690194 · founders-at-work 1590597141 · from-galileo-to-newton 0486242277 ·
  how-much-of-these-hills-is-gold 0525537201 · i-want-to-be-a-mathematician 0883854457 ·
  in-the-plex 1416596585 · information-the-new-language-of-science 0674013875 · maker-of-patterns
  0871403862 · more-money-than-god 1594202559 ·
  structure-and-interpretation-of-computer-programs 0262510871 · the-bleeding-heart 067144784X ·
  the-british-industrial-revolution-in-global-perspective 0521687853 · the-complete-calvin-and-hobbes
  0740748475 · the-dream-machine 1732265119 · the-launch-pad 1591845297 · the-man-who-knew-infinity
  0671750615 · the-mighty-red B0DRSSKVWG (ed. Kindle ES de Siruela — el impreso usa prefijo
  ISBN-13 979, sin equivalente ISBN-10) · the-network-state B09VPKZR3G (sin edición impresa) ·
  the-origins-of-the-second-world-war 014013672X · the-power-of-starting-something-stupid
  1609070097 · the-secret-lives-of-church-ladies 1949199738 · the-soul-of-a-new-machine 0316491977 ·
  the-startup-way 1101903201 · the-velvet-rage 0738210110 · lost-and-found 0525512462 · mr-putin
  0815723768.
  **4 quedan sin ASIN a propósito** (regla de oro: nunca inventar):
  - `a-history-of-medieval-europe` — el título aparece en Amazon atribuido a R.H.C. Davis, no a
    John H. Mundy como dice la ficha. **Hay que resolver la autoría antes de poner un ASIN.**
  - `dare-to-lead` — solo aparecen packs de 4 libros y "resúmenes" de terceros; no se encontró
    ficha individual con ISBN propio de la edición Vergara.
  - `in-defense-of-food` — no se confirmó ISBN-10 de una edición española real.
  - `the-planiverse` — **es correcto que quede vacío**: la nota de la ficha dice explícitamente que
    el enlace va a la búsqueda de Amazon porque la edición ES de 2000 es poco difundida.

  **5. Actualizar Best-of Negocios e Inversión.** El post se había escrito con ~362 libros en el
  catálogo; se re-curó contra las **112 fichas de `categoria: negocios` con ASIN** de hoy, con
  manifiesto determinístico (`consenso|slug|titulo|autor|referentes`). Resultado: **24 libros en 5
  grupos** — Los más recomendados (5), Fundar y escalar (5), Invertir y entender el dinero (5),
  Liderazgo y cultura (5), Estrategia poder y decisiones (4). **Sumados (9):** the-lean-startup,
  the-e-myth-revisited, only-the-paranoid-survive, the-psychology-of-money, good-to-great,
  the-culture-code, how-to-win-friends-and-influence-people,
  originals-how-non-conformists-move-the-world, the-48-laws-of-power. **Sacados (2):**
  security-analysis y growth (ambos sin edición ES y fuera del ángulo del post). Excluidos a
  propósito pese a tener 2 referentes: the-mythical-man-month y the-score-takes-care-of-itself
  (sin edición ES y muy de nicho). `fechaActualizado` → 2026-08-14, `fecha` original intacta.

  **6. Documentación.** Se crearon dos archivos nuevos en la raíz de `sitio-libros/`:
  - **`ESTADO-CONTENIDO.md`** — el corte auditado (números, tabla de los 44 referentes con
    libros/listicle/backlog, gaps por costo-beneficio, riesgos, estado de monetización). **A partir
    de ahora es la fuente de verdad de los conteos**, por encima de `PENDIENTES.md`.
  - **`NUEVOS-REFERENTES.md`** — runbook de alta de referente para sesiones Sonnet: pipeline de 9
    pasos, cola priorizada (del Toro 26 → Almodóvar 6 → Huberman 36 → Cowen 10, los cuatro con
    manifiesto ya sourceado en la raíz; Malala necesita sourcing propio), checklist de cierre y
    sección de errores conocidos.
  - `ACCIONES.md` ahora apunta a los dos.

  **Estado al cierre: 974 fichas · 44 referentes · 46 posts (44 listicles + 2 best-of) ·
  970 fichas con ASIN válido.**
  **Pendiente para Marcelo en Windows:** `python tools\detectar_duplicados.py src\content\libros`,
  `python tools\auditar_fichas.py src\content\libros src\content\autores`, `npm run build`,
  `git commit && push`, y pedir indexación en GSC del listicle de Malala y del best-of de negocios
  actualizado.
