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
  → RESUELTO: ambas enriquecidas el 2026-07-09.
- **2026-07-09 (3er pase)** — 2 vínculos nuevos verificados:
  - Sam Walton: Made in America → + Warren Buffett (antes solo Bezos). Ficha además enriquecida
    (era stub) → edición ES "Made in America: Mi Historia", asin 0525564896.
  - El inversor inteligente → + Naval Ravikant (antes solo Buffett).
  Descartados por falta de fuente (rigor): El comienzo del infinito ↔ Bezos (no verificado);
  Autobiografía de Franklin ↔ Musk (lo documentado es la biografía de Isaacson, otro libro).
  Efecto: libros con 2+ referentes pasaron de 19 a **21**. **Global fichas: 71/142.**
- **2026-07-09 (4º pase)** — 2 vínculos nuevos verificados (cluster Dostoievski):
  - Crimen y castigo → + Lex Fridman (antes solo Peterson).
  - Los hermanos Karamázov → + Jordan Peterson (antes solo Lex Fridman). Ficha además
    enriquecida (era stub) → edición ES Penguin Clásicos, asin 8491050051.
  Descartados por rigor: Man's Search for Meaning ↔ Taleb (solo afinidad temática, sin rec
  explícita); Thinking Fast and Slow ↔ Naval (Naval lo criticó, no lo recomienda).
  Efecto: libros con 2+ referentes pasaron de 21 a **23**. **Global fichas: 72/142.**

## Artículos de blog

### Listicles de referente (arquetipo 1)

- **≤ 2026-07-05** — Bill Gates, Barack Obama, Warren Buffett, Elon Musk, Jordan Peterson,
  Tim Ferriss.
- **2026-07-09** — Ray Dalio (`/blog/libros-que-recomienda-ray-dalio`).
- **2026-07-09** — Mark Zuckerberg (`/blog/libros-que-recomienda-mark-zuckerberg`).

- **2026-07-10** — Ryan Holiday (`/blog/libros-que-recomienda-ryan-holiday`).
  4 libros: Meditaciones, Cartas de un estoico, El obstáculo es el camino, La guerra del arte.
  Grupos: "Los clásicos estoicos" y "Estoicismo aplicado".
- **2026-07-10 — REFRESH** de los 6 listicles viejos, regenerados desde su manifiesto completo
  (con los cruces incorporados) vía subagente + `fechaActualizado: 2026-07-10`:
  Bill Gates (1 → **9** libros; estaba muy desactualizado), Barack Obama (→12, +El ferrocarril
  subterráneo), Warren Buffett (→6, +Sam Walton), Elon Musk (→7, +Dune y De cero a uno),
  Jordan Peterson (→5, +Los hermanos Karamázov), Tim Ferriss (→5, +Meditaciones).
  Verificado: solo enlaces internos a fichas enriquecidas, títulos exactos, `fecha` original intacta.

### Best-of por categoría (arquetipo 2)

- **2026-07-09** — Negocios e Inversión (`/blog/mejores-libros-de-negocios-e-inversion`).
  11 libros enlazados, ordenados por consenso; agrupa Inversión / Estrategia / Economía.

### Listicles de referente habilitados (fichas 100%, falta escribir el post)

Sam Altman, James Clear, Peter Thiel, Angela Duckworth, Yuval Noah Harari, Daniel Kahneman,
Ryan Holiday, Naval Ravikant, Andrew Ng.

---

## Bios de referentes

- **2026-07-09** — Reemplazadas bios genéricas autogeneradas por bios reales en:
  - `autores/elon-musk.md`: profesión actualizada a "Fundador de SpaceX y CEO de Tesla";
    bio y cuerpo reescritos con quién es, por qué seguir sus lecturas y fuente (X/Twitter +
    entrevistas). 2-3 frases originales en castellano rioplatense.
  - `autores/jordan-peterson.md`: profesión actualizada a "Psicólogo clínico, profesor y autor";
    bio y cuerpo reescritos con credencial (Harvard/Toronto, 12 reglas), por qué seguir sus
    lecturas y fuente verificable (jordanbpeterson.com/blog/book-list/). Enlace incluido en
    el cuerpo.
- **2026-07-09** — Reemplazadas bios genéricas autogeneradas por bios reales en (tanda de 8):
  - `autores/tim-ferriss.md`: bio y cuerpo reescritos. Fuente: The Tim Ferriss Show (tim.blog).
  - `autores/ray-dalio.md`: bio y cuerpo reescritos. Fuente: Principles (principles.com).
  - `autores/mark-zuckerberg.md`: profesión ajustada a "Cofundador de Meta"; bio y cuerpo
    reescritos con detalle del club "A Year of Books" (2015, 23 títulos). Fuente: Facebook.
  - `autores/naval-ravikant.md`: profesión ajustada a "Cofundador de AngelList e Inversor";
    bio y cuerpo reescritos. Fuente: Naval Podcast (naval.app).
  - `autores/yuval-noah-harari.md`: profesión ajustada a "Historiador y Escritor"; bio y
    cuerpo reescritos. Fuente: ynharari.com (Reading List).
  - `autores/daniel-kahneman.md`: bio y cuerpo reescritos; se indica fallecimiento el
    27/03/2024 a los 90 años. Fuente: Ensayos académicos y Entrevistas.
  - `autores/sam-altman.md`: bio y cuerpo reescritos con trayectoria YC + OpenAI.
    Fuente: Blog personal (blog.samaltman.com).
  - `autores/andrew-ng.md`: profesión ajustada a "Fundador de DeepLearning.AI y Cofundador
    de Coursera"; bio y cuerpo reescritos. Fuente: The Batch Newsletter (DeepLearning.AI).
- **2026-07-10** — Reemplazadas bios genéricas autogeneradas por bios reales en (tanda de 10):
  - `autores/peter-thiel.md`: profesión ajustada a "Cofundador de PayPal e Inversor"; bio y
    cuerpo reescritos con trayectoria PayPal/Palantir/Facebook y perfil intelectual. Fuente:
    Zero to One / Entrevistas universitarias.
  - `autores/ryan-holiday.md`: profesión ajustada a "Autor y Divulgador de Filosofía Estoica";
    bio y cuerpo reescritos con datos verificados (10M+ copias, serie estoica). Fuente: The
    Daily Stoic (dailystoic.com).
  - `autores/james-clear.md`: profesión ajustada a "Autor y Experto en Hábitos"; bio y cuerpo
    reescritos con datos verificados (25M copias, 60 idiomas, 3M+ suscriptores newsletter).
    Fuente: jamesclear.com (Newsletter 3-2-1).
  - `autores/angela-duckworth.md`: profesión ajustada a "Psicóloga e Investigadora de la
    Universidad de Pennsylvania"; bio y cuerpo reescritos (UPenn, Character Lab, Grit 5M).
    Fuente: Character Lab / Grit Book Resources.
  - `autores/jeff-bezos.md`: profesión "Fundador de Amazon" mantenida; bio y cuerpo reescritos
    con detalle de Blue Origin, WaPo y uso de libros como herramienta de gestión. Fuente:
    Cartas a Accionistas y Biografías.
  - `autores/oprah-winfrey.md`: profesión ajustada a "Conductora, Productora y Empresaria";
    bio y cuerpo reescritos con historia del Book Club desde 1996 y el "efecto Oprah". Fuente:
    Oprah's Book Club (oprahdaily.com).
  - `autores/nassim-nicholas-taleb.md`: profesión ajustada a "Ensayista, Estadístico y
    Exoperador de Riesgo"; bio y cuerpo reescritos con serie Incerto y credencial Sunday Times.
    Fuente: Fooled by Randomness Notes.
  - `autores/neil-degrasse-tyson.md`: profesión "Astrofísico y Divulgador Científico" mantenida;
    bio y cuerpo reescritos con Hayden Planetarium, StarTalk y AMA viral de Reddit 2011. Fuente:
    StarTalk Radio / Reddit AMA.
  - `autores/malcom-gladwell.md`: profesión "Periodista y Autor" mantenida; bio y cuerpo
    reescritos con 8 bestsellers NYT y perfil The New Yorker / Revisionist History. Fuente:
    Revisionist History Podcast.
  - `autores/lex-fridman.md`: profesión ajustada a "Investigador de IA y Podcaster"; bio y
    cuerpo reescritos con trayectoria MIT y podcast de largo aliento. Fuente: Lex Fridman
    Podcast (lexfridman.com/reading-list).
- **2026-07-10** — Reemplazadas bios genéricas autogeneradas por bios reales en (tanda de 16):
  - `autores/adam-grant.md`: profesión mantenida; bio y cuerpo reescritos con credencial
    Wharton y enfoque en psicología organizacional. Fuente: Think Again newsletter / adamgrant.net.
  - `autores/brene-brown.md`: profesión ajustada a "Investigadora, Profesora y Autora"; bio y
    cuerpo reescritos con charla TED, U. de Houston y libros clave. Fuente: Unlocking Us Podcast (brenebrown.com).
  - `autores/emma-watson.md`: profesión ajustada a "Actriz y Activista Feminista"; bio y cuerpo
    reescritos con ONU Mujeres, HeForShe y Our Shared Shelf (2016-2019, en pasado). Fuente: Our Shared Shelf (Goodreads).
  - `autores/garry-kasparov.md`: profesión ajustada a "Gran Maestro de Ajedrez, Autor y Activista";
    bio y cuerpo reescritos con récord mundial, Deep Blue y libros publicados. Fuente: kasparov.com / Entrevistas.
  - `autores/gwyneth-paltrow.md`: profesión ajustada a "Actriz y Fundadora de Goop"; bio y cuerpo
    reescritos con historia de Goop (2008) y criterio del Goop Book Club. Fuente: Goop Book Club (goop.com).
  - `autores/j-k-rowling.md`: profesión "Escritora" mantenida; bio y cuerpo reescritos con
    origen de Harry Potter, 500M ejemplares y influencias literarias. Fuente: jkrowling.com / Entrevistas.
  - `autores/malala-yousafzai.md`: profesión ajustada a "Activista por la Educación y Premio Nobel
    de la Paz"; bio y cuerpo reescritos con atentado, Nobel 2014 y Malala Fund. Fuente: Fearless Book Club (malala.org).
  - `autores/marc-andreessen.md`: profesión ajustada a "Cofundador de Andreessen Horowitz e Inversor";
    bio y cuerpo reescritos con Mosaic/Netscape y a16z (Airbnb, Twitter, Coinbase). Fuente: a16z Podcast / Blog Andreessen.
  - `autores/natalie-portman.md`: profesión ajustada a "Actriz, Directora y Activista"; bio y
    cuerpo reescritos con Harvard, Oscar y club de lectura en Instagram. Fuente: Instagram oficial.
  - `autores/paul-graham.md`: profesión ajustada a "Fundador de Y Combinator, Programador y
    Ensayista"; bio y cuerpo reescritos con YC (Airbnb, Dropbox, Stripe) y ensayos. Fuente: paulgraham.com.
  - `autores/reese-witherspoon.md`: profesión ajustada a "Actriz, Productora y Empresaria"; bio y
    cuerpo reescritos con Hello Sunshine y efecto bestseller del club. Fuente: Reese's Book Club (hello-sunshine.com).
  - `autores/richard-branson.md`: profesión "Fundador de Virgin Group" mantenida; bio y cuerpo
    reescritos con Virgin Records, 400+ empresas y defensa del hábito lector. Fuente: Virgin Blog (virgin.com).
  - `autores/satya-nadella.md`: profesión "CEO de Microsoft" mantenida (cargo confirmado); bio y
    cuerpo reescritos con Azure, mentalidad de crecimiento y Hit Refresh. Fuente: Microsoft Blog / Hit Refresh.
  - `autores/simon-sinek.md`: profesión ajustada a "Autor y Conferencista de Liderazgo"; bio y
    cuerpo reescritos con charla TED 2009, Círculo Dorado y libros clave. Fuente: simonsinek.com.
  - `autores/stephen-king.md`: profesión "Escritor" mantenida; bio y cuerpo reescritos con
    60+ novelas, 80 libros/año y lista anual en X. Fuente: stephenking.com / Cuenta oficial X.
  - `autores/vitalik-buterin.md`: profesión ajustada a "Cofundador de Ethereum"; bio y cuerpo
    reescritos con whitepaper a los 19 años y perfil interdisciplinario. Fuente: vitalik.ca (Blog oficial).
- **2026-07-10** — Enriquecimiento de fichas (tanda de 10 stubs → completas):
  - `libros/give-and-take.md`: "Dar y recibir", Gestión 2000, ASIN 8498753449. Adam Grant.
  - `libros/think-again.md`: "Piénsalo otra vez", Deusto, ASIN 8423432904. Adam Grant.
  - `libros/the-culture-code.md`: "The Culture Code", Crown Business (sin ES), ASIN 0804176981. Adam Grant.
  - `libros/start-with-why.md`: "Empieza con el porqué", Empresa Activa, ASIN 8492921889. Simon Sinek.
  - `libros/the-infinite-game.md`: "El juego infinito", Empresa Activa, ASIN 8416997233. Simon Sinek.
  - `libros/turn-the-ship-around.md`: "¡Cambia el barco de rumbo!", Conecta, ASIN 8416029598. Simon Sinek.
  - `libros/becoming.md`: "Mi historia", Plaza & Janés, ASIN 8401021758. Oprah Winfrey.
  - `libros/the-handmaid-s-tale.md`: "El cuento de la criada", Salamandra, ASIN 8498388015. Emma Watson.
  - `libros/where-the-crawdads-sing.md`: "La chica salvaje", Vintage Español, ASIN 0593081617. Reese Witherspoon.
  - `libros/the-body-keeps-the-score.md`: "El cuerpo lleva la cuenta", Eleftheria, ASIN 8494759205. Gwyneth Paltrow.
  Nota: The Culture Code no tiene edición en español confirmada; se usa edición inglesa con nota.
  **Global fichas enriquecidas: ~82/142.**
