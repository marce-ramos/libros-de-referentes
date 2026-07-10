# Bitácora de avance — Los Imperdibles

Registro **append-only** del avance de contenido: cada tanda de enriquecimiento de fichas
y cada artículo de blog queda asentado acá con fecha. **No se sobrescribe**: solo se agregan
entradas nuevas al final de cada sección. El estado resumido (conteos, pendientes) vive en
`PENDIENTES.md`; acá queda el historial detallado.

Formato de entrada: `- AAAA-MM-DD — <qué> (<detalle>). Global: <fichas con ASIN>/142.`

---

## Enriquecimiento de fichas

- **Hasta 2026-07-05** — Base inicial cargada (39 referentes, 142 libros, 9 categorías).
  Primeras tandas de enriquecimiento: top de consenso (Gates/Obama/Buffett), bestsellers de
  alta demanda, y por referente Musk, Jordan Peterson y Tim Ferriss. Global: ~30/142.
- **2026-07-09** — Ray Dalio ×4: Principios, El héroe de las mil caras, El río del Edén,
  Lecciones de la Historia. → Ray Dalio 4/4.
- **2026-07-09** — Mark Zuckerberg ×4: El problema de los tres cuerpos, Por qué fracasan los
  países, El fin del poder, Creatividad S.A. → Zuckerberg 4/4.
- **2026-07-09** — "Remates" ×5 (cada uno completó un referente): Factfulness (Gates 8/8),
  The Making of the Atomic Bomb (Altman 4/4), Rituales cotidianos (Clear 4/4), El misterio de
  nuestro mundo (Thiel 3/3), Fluir/Flow (Duckworth 3/3).
- **2026-07-09** — Harari ×2 (Armas gérmenes y acero, Historia y cronología del mundo),
  Kahneman ×2 (Un pequeño empujón, Deshaciendo errores), Ryan Holiday ×2 (El obstáculo es el
  camino, Cartas de un estoico). → Harari 3/3, Kahneman 3/3, Ryan Holiday 4/4.
- **2026-07-09** — Naval Ravikant ×3 (Siddhartha, Seis piezas fáciles, El optimista racional),
  Andrew Ng ×2 (IA: un enfoque moderno, Vida 3.0). → Naval 4/4, Andrew Ng 3/3.
  **Global: 68/142.**
- **2026-07-09** — Enriquecidas por consenso (salieron de stub al llegar a 2 referentes vía el
  cruce): The Black Swan / El cisne negro (Bezos + Naval), The Underground Railroad / El
  ferrocarril subterráneo (Oprah + Obama). **Global: 70/142.**

### Referentes con cobertura 100% (fichas listas)

Barack Obama, Warren Buffett, Elon Musk, Bill Gates, Ray Dalio, Mark Zuckerberg,
Jordan Peterson, Tim Ferriss, Sam Altman, James Clear, Peter Thiel, Angela Duckworth,
Yuval Noah Harari, Daniel Kahneman, Ryan Holiday, Naval Ravikant, Andrew Ng.

---

## Cruces referente↔libro (relaciones nuevas)

Pase de detección: libros ya existentes a los que un referente del roster también recomienda,
pero no estaban acreditados. **Solo se agregan vínculos verificados con fuente.** Cada uno sube
el consenso del libro y mejora el interlinking.

- **2026-07-09 (1er pase)** — 5 vínculos nuevos verificados:
  - Dune → + Elon Musk (antes solo Ferriss).
  - Meditaciones → + Tim Ferriss (antes solo Ryan Holiday).
  - Poor Charlie's Almanack → + Naval Ravikant (antes solo Buffett).
  - El alquimista → + Oprah Winfrey (antes solo Malala).
  - Sapiens → + Naval Ravikant (ya tenía Gates, Obama, Clear → ahora 4).
  Efecto: libros con 2+ referentes pasaron de 13 a **17**.
  Candidatos pendientes de verificar (2º pase): De cero a uno ↔ Musk, El inversor inteligente ↔
  Naval, The Black Swan ↔ Naval, Autobiografía de Franklin ↔ Munger/Buffett/Musk,
  Pensar rápido pensar despacio ↔ otros, El comienzo del infinito ↔ Bezos.
- **2026-07-09 (2º pase)** — 4 vínculos nuevos verificados:
  - Superinteligencia → + Bill Gates (ya tenía Musk y Altman → 3).
  - De cero a uno → + Elon Musk (ya tenía Thiel y Andrew Ng → 3).
  - The Black Swan → + Naval Ravikant (antes solo Bezos). ⚠️ ficha aún STUB → enriquecer.
  - The Underground Railroad → + Barack Obama (antes solo Oprah). ⚠️ ficha aún STUB → enriquecer.
  Nota: *Una educación* (educated.md) ya tenía Gates + Obama, sin cambios.
  Efecto: libros con 2+ referentes pasaron de 17 a **19**.
  Aún por verificar (3er pase): El inversor inteligente ↔ Naval, Autobiografía de Franklin ↔
  Buffett/Musk, Pensar rápido pensar despacio ↔ otros, El comienzo del infinito ↔ Bezos,
  1984 ↔ otros. **Pendiente: enriquecer The Black Swan y The Underground Railroad** (ahora
  con 2 referentes pero todavía en stub → aparecen así en "Los más recomendados").

## Artículos de blog

### Listicles de referente (arquetipo 1)

- **≤ 2026-07-05** — Bill Gates, Barack Obama, Warren Buffett, Elon Musk, Jordan Peterson,
  Tim Ferriss.
- **2026-07-09** — Ray Dalio (`/blog/libros-que-recomienda-ray-dalio`).
- **2026-07-09** — Mark Zuckerberg (`/blog/libros-que-recomienda-mark-zuckerberg`).

### Best-of por categoría (arquetipo 2)

- **2026-07-09** — Negocios e Inversión (`/blog/mejores-libros-de-negocios-e-inversion`).
  11 libros enlazados, ordenados por consenso; agrupa Inversión / Estrategia / Economía.

### Listicles de referente habilitados (fichas 100%, falta escribir el post)

Sam Altman, James Clear, Peter Thiel, Angela Duckworth, Yuval Noah Harari, Daniel Kahneman,
Ryan Holiday, Naval Ravikant, Andrew Ng.
