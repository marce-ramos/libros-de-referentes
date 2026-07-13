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

- **2026-07-10** — Tanda de 10 (subagente Sonnet) para completar 5 referentes: Empresas que
  perduran + Los restos del día (Bezos 4/4); Una nueva tierra + Hola, preciosa (Oprah 5/5);
  El maestro y Margarita + Winter Is Coming [ed. inglesa, asin 1610397193] (Kasparov 3/3);
  El método/Las herramientas (Paltrow); Americanah + Tiene que ser aquí (Malala 3/3).
  ⚠️ **`an-unblemished-mind` (Paltrow): el subagente ALUCINÓ una reseña — el libro NO existe**
  (Sarah Manguso nunca lo escribió; título erróneo heredado del import).
  → **RESUELTO (2026-07-10):** `an-unblemished-mind.md` eliminada y reemplazada por **Hamnet**
  de Maggie O'Farrell (pick REAL del Goop Book Club, verificado; edición ES Libros del Asteroide,
  asin 8417977589). Gwyneth Paltrow queda **3/3**. Global fichas: 92/142.
  (Regla nueva en ENRIQUECER.md: verificar que el libro exista antes de reseñarlo.)
- **2026-07-10 — Auditoría de entradas dudosas.** Revisados los ~50 stubs restantes (título+autor
  vs libros reales): **todos existen y están bien atribuidos**; "An Unblemished Mind" fue la ÚNICA
  fabricación. Las enriquecidas (~92) están verificadas por construcción (ASIN de edición real).
  Pendiente opcional: auditar *atribuciones* (si cada referente recomendó cada libro) al enriquecer
  cada stub. Señal de fidelidad del import: las 4 de Neil deGrasse Tyson = su lista real del AMA 2011.

- **2026-07-10** — Tanda de 9 (subagente) que completó 3 referentes de tech/ideas:
  **Marc Andreessen 3/3, Paul Graham 3/3, Nassim Taleb 3/3.** Emprender y liderar una startup
  (Andreessen); High Output Management [EN], Revoluciones tecnológicas y capital financiero;
  Hackers & Painters [EN], Autobiografía (Franklin), The Dream Machine [sin ASIN → fallback]
  (Graham); Ficciones, El desierto de los tártaros, Information [sin ASIN → fallback] (Taleb).
  Spot-check sin correcciones. Global: ~101/142 (99 con ASIN real + 2 con fallback).

- **2026-07-10** — Tanda de 10 (subagente) que completó 3 referentes: **Satya Nadella 4/4,
  Malcolm Gladwell 3/3, Brené Brown 4/4.** Comunicación No Violenta, Remando como un solo hombre,
  Competing in the Age of AI [EN] (Nadella); Psicoanálisis la profesión imposible, The Blind Side
  [EN], The Person and the Situation [EN] (Gladwell); Libera tu magia, Atrévete a liderar [fallback],
  El acto de crear, Los dones de la imperfección (Brown). Corrección de Opus: The Boys in the Boat →
  título ES real "Remando como un solo hombre" (Nórdica) + ASIN de imprenta (el agente había puesto
  un ASIN Kindle, que no comisiona). Catálogo: 162 libros.

- **2026-07-10** — Tanda de 10 (subagente) que completó 3 referentes: **Neil deGrasse Tyson 4/4,
  Reese Witherspoon 4/4, Vitalik Buterin 4/4.** Los viajes de Gulliver, El origen de las especies,
  La Biblia (Reina-Valera), The System of the World [EN] (Tyson); Todos quieren a Daisy Jones,
  Pequeños fuegos por todas partes, La red de Alice (Reese); Mercados radicales, Stubborn
  Attachments [EN], The Network State [sin ASIN, solo web] (Vitalik). 0 dups. Ajuste de Opus:
  de-quoteé una paráfrasis presentada como cita textual de Tyson en La Biblia. Catálogo: 162.

- **2026-07-10** — Tanda de 10 (subagente) que completó 3 referentes: **Lex Fridman 6/6,
  Stephen King 3/3, J.K. Rowling 4/4.** Trilogía de la Fundación, El idiota, El principito (Lex);
  El señor de las moscas, The Bleeding Heart [EN], The Hair of Harold Roux [EN] (King); Emma,
  La Ilíada, El pequeño caballo blanco, Team of Rivals [EN] (Rowling). 0 dups. Corrección de Opus:
  The Bleeding Heart no tiene edición ES confirmada → revertido a inglés (el agente había puesto un
  ASIN/título ES sin verificar). Catálogo: 162 libros, ~151 con ASIN.

- **2026-07-10** — Tanda de 11 (subagente) que completó los ÚLTIMOS 3 referentes: **Emma Watson
  4/4, Natalie Portman 4/4, Richard Branson 4/4.** Monólogos de la vagina, Persépolis, Los
  argonautas (Watson); Pechos y huevos, En manos de las furias, La amiga estupenda, Trilogía de
  Copenhague (Portman); Pensamiento Caja Negra, El legado de Mandela, Donde viven los monstruos,
  Cisnes salvajes (Branson). El agente corrigió 3 títulos ES (En manos de las furias, Pensamiento
  Caja Negra, El legado de Mandela). 0 correcciones de Opus, 0 dups.
  **🎉 HITO: 39/39 referentes al 100%. 162 libros, todos con reseña, 0 stubs (3 con ASIN vacío →
  fallback de búsqueda: The Bleeding Heart, Dare to Lead, The Network State).**

- **2026-07-12 (Dua Lipa — tanda 1/varias)** — 8 fichas nuevas (subagente Sonnet), todas
  recomendadas por Dua Lipa (Service95 Book Club), todas con edición ES verificada y ASIN
  impreso (0 B0, 0 ASIN vacío): Cien años de soledad [8497592204] (García Márquez), Pachinko
  [8494716964] (Min Jin Lee), Mil soles espléndidos [8498381223] (Hosseini), Éramos unos niños
  [8499894453] (Patti Smith, memorias), La mala costumbre [8432242128] (Alana S. Portero, nativo
  ES), En la Tierra somos fugazmente grandiosos [8433980599] (Ocean Vuong), Medio sol amarillo
  [8439720696] (Adichie), No digas nada [8417910557] (Radden Keefe, historia). Spot-check Opus:
  3 ASIN reverificados en amazon.es (Cien años, Pachinko, On Earth) → resuelven OK; sin citas
  inventadas de Dua Lipa; 0 dups. Suma densidad de autor a Adichie (+Medio sol amarillo) y a
  Keefe (+No digas nada). **Pendiente Dua Lipa: 24 fichas nuevas + listicle.**

- **2026-07-12 (Dua Lipa — tanda 2/varias)** — Manifiesto completo re-derivado (el de la tanda 1
  se había reconciliado en el chat pero nunca se commiteó): refetch de
  booknotification.com/book-clubs/service95-book-club (34 picks totales, jun-2023 a jun-2026) →
  reconciliar.py sobre los 24 pendientes: **23 NUEVO + 1 REVISAR** (The Trees de Percival Everett
  vs. James, ya en catálogo por Obama → confirmado libro distinto, mismo autor → NUEVO).
  Enriquecidas **10 fichas nuevas** (subagente Sonnet): Shuggie Bain [8418342366] (Douglas
  Stuart), The Vanishing Half [8439738641] (Brit Bennett), The Guest [8433927221] (Emma Cline),
  Lágrimas en H-Mart / Crying in H Mart [1984898957, sin ES impresa confirmada] (Michelle
  Zauner), Nadar en la oscuridad / Swimming in the Dark [8412292596] (Tomasz Jedrowski), Blanco y
  negro / Noughts and Crosses [849250675X] (Malorie Blackman), Lincoln en el Bardo [8432235342]
  (George Saunders), Sobre los huesos de los muertos [8416638802] (Olga Tokarczuk), La picadura
  de abeja [8433929607] (Paul Murray), There There [0525436146, sin ES] (Tommy Orange).
  Verificación Opus: ASIN 10 chars OK en las 10, integridad recomendadoPor OK, 0 [DUP] nuevos,
  spot-check de 2 fichas (Crying in H Mart, There There) sin citas inventadas de Dua Lipa.
  **Dua Lipa: 20/34. Pendiente: 14 fichas nuevas + listicle** (Grief Is the Thing with Feathers,
  Still Born, Widow Basquiat, Small Boat, This House of Grief, The Trees, Flesh, Brightly
  Shining, Night People, The Son of Man, Bad Feminist, Jerusalem, So Late in the Day, Having
  Spent Life Seeking — manifiesto con fuente en `manifiesto_dua_lipa.txt`, no commiteado, para
  no ensuciar el repo con un archivo de trabajo; regenerar con reconciliar.py si se pierde).
  Catálogo: 180 libros.

- **2026-07-12 (Dua Lipa — tanda 3/3, ÚLTIMA)** — Enriquecidas las **14 fichas finales**
  (subagente Sonnet): Grief Is the Thing with Feathers [8439741502] (Max Porter); La hija única
  / Still Born [8433999060] (Guadalupe Nettel, **novela nativa en español** — Anagrama, el pick
  del club usa el título de la traducción al inglés); Widow Basquiat [6073132832] (Jennifer
  Clement, memorias); Small Boat [1913109372, sin ES] (Vincent Delecroix); This House of Grief
  [1399606808, sin ASIN ES confirmado — ES existe como "La casa de los lamentos", Libros del
  K.O.] (Helen Garner); Los árboles / The Trees [8417375783] (Percival Everett — **verificado
  como novela distinta de `james.md`**, mismo autor, sin cruce indebido); Flesh [198212279X, sin
  ES] (David Szalay); Brightly Shining [0802163491, sin ES] (Ingvild H. Rishøi); Night People
  [1538741113, sin ES] (Mark Ronson, memorias); The Son of Man [0802160905, sin ES] (Jean-
  Baptiste Del Amo); Mala feminista / Bad Feminist [8418966106] (Roxane Gay, Capitán Swing);
  Jerusalem [1848420501, sin ES — obra de teatro] (Jez Butterworth); Bien tarde en el día / So
  Late in the Day [8412846230] (Claire Keegan, Eterna Cadencia); Una vida buscando / Having
  Spent Life Seeking [8439745958] (Kae Tempest, Literatura Random House).
  Verificación Opus: ASIN 10 chars OK en las 14, integridad recomendadoPor OK, categorías
  existentes OK, 0 `[DUP]` nuevos (detector solo reporta `[REV]` informativos, incluye
  correctamente Percival Everett con James + Los árboles como dos obras distintas). Spot-check
  de 2 fichas (Still Born, The Trees): sin errores, buena disambiguación de ediciones y de
  Percival Everett vs. James.
  **🎉 HITO: Dua Lipa 34/34 — referente #40 al 100%.** Catálogo: 194 libros.

### Referentes con cobertura 100% (fichas listas) — LOS 39 ✅

Barack Obama, Warren Buffett, Elon Musk, Bill Gates, Ray Dalio, Mark Zuckerberg,
Jordan Peterson, Tim Ferriss, Sam Altman, James Clear, Peter Thiel, Angela Duckworth,
Yuval Noah Harari, Daniel Kahneman, Ryan Holiday, Naval Ravikant, Andrew Ng,
Jeff Bezos, Oprah Winfrey, Garry Kasparov, Malala Yousafzai, Gwyneth Paltrow,
Marc Andreessen, Paul Graham, Nassim Nicholas Taleb, Satya Nadella, Malcolm Gladwell, Brené Brown,
Neil deGrasse Tyson, Reese Witherspoon, Vitalik Buterin, Lex Fridman, Stephen King, J.K. Rowling,
Emma Watson, Natalie Portman, Richard Branson. **(= los 39 referentes, catálogo 100% enriquecido.)**
**+ Dua Lipa** (referente #40, completado 2026-07-12: 34/34 fichas + listicle).

---

## Descubrimiento (expansión del catálogo)

Mecanismo `MODO DESCUBRIR` (ver ENRIQUECER.md): un agente fetchea la fuente REAL del referente y
extrae candidatos con URL-fuente (nunca de memoria) → Opus reconcilia contra el catálogo (cruce vs
stub nuevo) → se enriquece (MODO LIBRO).

- **2026-07-10 — Piloto: Barack Obama (profundizar).** El agente de descubrimiento extrajo
  **32 candidatos** de sus listas anuales en Medium (2021-2025), cada uno con URL-fuente.
  Reconciliados: ninguno colisionaba. Enriquecidos **10** (fichas nuevas): Klara y el Sol,
  Proyecto Hail Mary, Fortuna (Trust/Hernán Díaz), Los náufragos del Wager, Ciudad de las nubes,
  El imperio del dolor, El pacto del agua, El mar de la tranquilidad, La inmensidad del mundo,
  Intermezzo. → **Obama 12 → 22 libros**; catálogo 142 → 152. Correcciones de Opus: The Wager sí
  tenía ES ("Los náufragos del Wager") que el agente no halló; Trust decía "finalista del Booker"
  (falso, ganó el Pulitzer 2023).
  **Backlog (22 candidatos sourceados, para enriquecer):** The Anthropologists, Stolen Pride,
  In Ascension, Someone Like Us, The Work of Art, There's Always This Year, The Ministry of Time,
  Martyr!, The God of the Woods, Help Wanted, The Heaven and Earth Grocery Store, The MANIAC,
  Poverty by America, How to Say Babylon, Chip War, The Vaster Wilds, King: A Life, How the Word
  Is Passed, The Lincoln Highway, Abundance, Who is Government?, The Sirens' Call.
  **Propagación:** el listicle de Obama se regeneró a los 22 libros (Ficción/No ficción,
  `fechaActualizado` 07-10). Su página de autor `/autores/barack-obama` se actualiza sola (query
  dinámica sobre la colección) — solo el blog necesita regeneración manual.
- **2026-07-12 — Profundizar: Barack Obama (backlog cerrado).** `reconciliar.py` sobre los 22
  candidatos del backlog: **18 NUEVO** directos + **3 REVISAR** resueltos como NUEVO (mismo autor,
  libro distinto: The Vaster Wilds vs. fates-and-furies/matrix de Lauren Groff; The Lincoln
  Highway vs. a-gentleman-in-moscow de Amor Towles; Who is Government? vs. the-blind-side/the-
  undoing-project de Michael Lewis) + **1 CROSS-REF** (Abundance, ya en catálogo por Bill Gates →
  se sumó Obama, confirmado en su lista de verano 2025 con cita real: "lectura obligada para
  progresistas..."). Enriquecidos los 21 NUEVO con MODO LIBRO: The Anthropologists, Stolen Pride,
  In Ascension, Someone Like Us, The Work of Art, There's Always This Year, Un puente sobre el
  tiempo (Ministry of Time), ¡Mártir!, El dios de los bosques, Help Wanted, Una tienda en Chicken
  Hill, MANIAC, Pobreza made in USA, How to Say Babylon, La guerra de los chips, La tierra más
  salvaje, King: A Life, El legado de la esclavitud, La autopista Lincoln, Who is Government?,
  The Sirens' Call. De estas, 11 quedaron solo-inglés por no tener edición ES todavía (todas muy
  recientes, 2023-2025): The Anthropologists, Stolen Pride, In Ascension, Someone Like Us, The
  Work of Art, There's Always This Year, Help Wanted, How to Say Babylon, King: A Life, Who is
  Government?, The Sirens' Call. Las otras 10 sí tienen edición ES confirmada: Un puente sobre el
  tiempo, ¡Mártir!, El dios de los bosques, Una tienda en Chicken Hill, MANIAC, Pobreza made in
  USA, La guerra de los chips, La tierra más salvaje, El legado de la esclavitud, La autopista
  Lincoln.
  `detectar_duplicados.py`: 0 dups exactos (Amor Towles y Lauren Groff ahora con 2-3 libros cada
  uno, todos títulos distintos verificados). **Obama 22 → 44 libros**; catálogo 205 → 226 (0
  stubs). Listicle de Obama regenerado a 44 (grupos Ficción / No ficción sin cambios de
  estructura). Backlog de Obama queda en 0.
- **2026-07-10 — Tooling de reconciliación.** Creados y probados `tools/reconciliar.py` (clasifica
  candidatos de un barrido: YA-LINKED / CROSS-REF / REVISAR / NUEVO; matchea por slug derivado del
  título EN → resuelve cross-idioma) y `tools/detectar_duplicados.py` (red de seguridad post-barrido;
  0 duplicados exactos en el catálogo actual). Documentados en ENRIQUECER.md.
- **2026-07-10 — Barrido: Bill Gates (flujo completo estrenado con tooling).** Discovery: 25
  candidatos sourceados (GatesNotes vía CNBC/Forbes/Kirkus, 2019-2025). `reconciliar.py`:
  **4 CROSS-REF** (An American Marriage, Un caballero en Moscú, Klara y el Sol, Proyecto Hail Mary
  → se sumó Gates; ahora Gates+Obama = 2 referentes), 20 nuevos, 1 REVISAR (Upheaval = libro
  distinto de Diamond → nuevo). Enriquecidos **10 nuevos**: Una tierra prometida, Por qué dormimos,
  Amplitud (Range), El código de la vida, La armonía de las células, Mañana y mañana y mañana,
  Prohibido nacer, El clamor de los bosques, Crisis (Upheaval), Cómo funciona el mundo.
  → **Gates 9 → 23**; catálogo 152 → 162. `detectar_duplicados.py`: 0 dups. Listicle de Gates
  regenerado a 23. Correcciones de Opus: 0 (el agente autocorrigió "La armonía de las células").
  Backlog (11 sourceados): These Truths, The Great Influenza, The Splendid and the Vile, The Spy
  and the Traitor, The Ministry for the Future, Born in Blackness, Not the End of the World,
  How to Know a Person, The Women, Personal History, Abundance.
- **2026-07-12 — Profundizar: Bill Gates (backlog cerrado).** `reconciliar.py` sobre los 11
  títulos del backlog: **11 NUEVO** (0 cross-ref, 0 revisar). Enriquecidos los 11 con MODO LIBRO:
  These Truths (solo inglés, W. W. Norton), La gran gripe (Capitán Swing), Esplendor y vileza
  (Ariel), Espía y traidor (Crítica), El Ministerio del Futuro (Minotauro), Born in Blackness
  (solo inglés, Liveright/Norton), El mundo no se acaba (Anagrama), Cómo conocer a una persona
  (Océano), Las mujeres de la guerra (Suma), Historia personal (Vintage Español), Abundancia
  (HarperCollins Español). `detectar_duplicados.py`: 0 dups exactos. **Gates 23 → 34**;
  catálogo 194 → 205 (0 stubs). Listicle de Gates regenerado a 34 (nuevo grupo "Psicología y
  relaciones" para *Cómo conocer a una persona*, único de esa categoría). Backlog de Gates
  queda en 0 — cerrado hasta el próximo barrido de descubrimiento.

- **2026-07-12/13 — Discovery + Profundizar: Reese Witherspoon (backlog masivo, en tandas).**
  Discovery: reesesbookclub.com/the-complete-list solo devolvió picks parciales (nov-2022 a
  jul-2026, ~50 de 129, por lazy-load JS) → cruzado con beyondthebookends.com (archivo completo
  2017-2026, verificado por match exacto en el rango solapado antes de confiar en los años más
  viejos). **129 picks totales** encontrados; Reese ya tenía 4/4 (Daisy Jones, Pequeños fuegos,
  La red de Alice, La chica salvaje) del enriquecimiento del 2026-07-10 → quedaban 125 candidatos.
  Decisión de Marcelo (vía pregunta): incluir también los picks YA y del sub-sello "Sunnie"
  (2026) → 121 candidatos netos tras excluir duplicados de fuente; y priorizar los más recientes
  (2023-2026, 52 libros) antes que el backlog 2017-2022 (~73), para no bloquear la tanda con un
  volumen inmanejable. `reconciliar.py` sobre los 52 priorizados: **51 NUEVO + 1 REVISAR**
  (The Nightingale vs. The Women, ya en catálogo por Bill Gates → confirmado libro **distinto**
  del mismo autor, Kristin Hannah → NUEVO). Enriquecidos los **52 NUEVO** con MODO LIBRO, en
  varias tandas de subagentes Sonnet (algunas cortadas por límite de sesión y relanzadas sin
  duplicar trabajo, verificando primero qué archivos ya existían): The House in the Pines, The
  House of Eve, El ruiseñor (The Nightingale), Comedia romántica, Did You Hear About Kitty Karr?,
  Cassandra in Reverse, Yellowface, Tom Lake, Mother-Daughter Murder Night, La mansión Starling,
  Maybe Next Time, Before We Were Innocent, La primera mentira gana, Redwood Court, Anita de
  Monte ríe la última, Nunca fuimos tan felices, Cómo terminar una historia de amor, The
  Unwedding, Noche de caballeros (Twelfth Knight), The Cliffs, Bailar lento (Slow Dance), The
  Comfort of Crows [memorias], Looking for Smoke, La sociedad de las mentiras, Seremos jaguares
  [memorias], City of Night Birds, Throwback, Las tres vidas de Cate Kay, Isola, Broken Country,
  Heiress Takes All, All That Life Can Afford, Una vida maravillosa, Stuck Up and Stupid, La
  compañía de lapiceras fénix, Spectacular Things, Once Upon a Time in Dollywood, To the Moon
  and Back, Wild Dark Shore, The Heir Apparent, The First Time I Saw Him, Beth is Dead, In Her
  Defense, Lady Tremaine, In Time with You, Into the Blue, The Fine Art of Lying, That Which
  Feeds Us, A Pair of Aces, A Founding Mother, The Winged Game, Gone Before Goodbye (coescrita
  por la propia Reese con Harlan Coben — única ficha con "Por qué la escribió" en vez de "Por
  qué la recomienda"). De estas, 52 quedaron mayormente solo-inglés (2025-2026 muy recientes),
  con ediciones ES confirmadas en las más añejas (2023-2024): Tom Lake, La primera mentira gana,
  Nunca fuimos tan felices, Cómo terminar una historia de amor, Anita de Monte ríe la última, La
  sociedad de las mentiras, Seremos jaguares, La compañía de lapiceras fénix, Una vida
  maravillosa, entre otras — detalle completo en cada ficha. `detectar_duplicados.py`: 0 `[DUP]`
  exactos (Kristin Hannah queda con 2 libros distintos, El ruiseñor + Las mujeres de la guerra,
  caso [REV] legítimo). Verificación de ASIN (10 caracteres, las 52) e integridad
  `recomendadoPor` → autor existente: OK. **Reese Witherspoon 4 → 56 libros**; catálogo 226 →
  278. Listicle regenerado de cero con las 56 fichas, agrupado por tipo de historia (Thrillers y
  misterio, Novela histórica, Ficción contemporánea y literaria, Romance, Fantástico y
  reimaginaciones, Juvenil YA, No ficción) en vez de por año, dado el volumen.
  **Backlog pendiente: ~73 candidatos de 2017-2022** (sourceados en el discovery, sin enriquecer
  todavía) — queda para una futura tanda de "Profundizar Reese Witherspoon".

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
- **2026-07-12 (piloto Dua Lipa)** — Nuevo referente europeo con fuente documentada: **Dua Lipa**
  (Service95 Book Club, pick mensual desde jun/2023). Bio creada en `autores/dua-lipa.md`.
  Descubrimiento de 34 picks (fuente: booknotification.com/book-clubs/service95-book-club,
  server-rendered) → reconciliado con `reconciliar.py`: 2 cross-ref, 3 REVISAR (mismo autor/otro
  libro → nuevos) y 29 nuevos. **2 cross-refs hechos:**
  - Trust / *Fortuna* (Hernán Díaz) → + Dua Lipa (ya tenía Obama → 2 referentes).
  - The Handmaid's Tale / *El cuento de la criada* (Atwood) → + Dua Lipa (ya tenía Watson → 2).
  Pendiente: enriquecer las **32 fichas nuevas** por tandas + listicle de Dua Lipa. Manifiesto
  reconciliado en el chat (no commiteado).

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
- **2026-07-10** — 3 listicles nuevos (vía manifiesto + subagente, spot-check sin correcciones):
  Sam Altman (4 libros), Naval Ravikant (8), Yuval Noah Harari (3).
  `/blog/libros-que-recomienda-{sam-altman,naval-ravikant,yuval-noah-harari}`.
- **2026-07-12** — Dua Lipa (`/blog/libros-que-recomienda-dua-lipa`), escrito directamente (sin
  subagente) con el manifiesto completo de las 34 fichas ya enriquecidas. Agrupado por año
  (2023-2026, 6/10/12/6 libros) en vez de por tema, ya que el club es un pick mensual fechado y
  esa estructura cuenta mejor la evolución de la selección. Verificación con script: 34/34 links
  con `titulo` exacto, `slug` existente, `dua-lipa` en `recomendadoPor`, ASIN presente; 0 links
  duplicados; 0 menciones de Amazon/afiliados en el cuerpo. **Dua Lipa queda con las 34 fichas +
  el listicle: referente #40 al 100%.**

### Best-of por categoría (arquetipo 2)

- **2026-07-09** — Negocios e Inversión (`/blog/mejores-libros-de-negocios-e-inversion`).
  11 libros enlazados, ordenados por consenso; agrupa Inversión / Estrategia / Economía.

### Listicles de referente habilitados (fichas 100%, falta escribir el post)

James Clear, Peter Thiel, Angela Duckworth, Daniel Kahneman, Andrew Ng, Adam Grant, Simon Sinek.
(Ya escritos: Ryan Holiday, Sam Altman, Naval Ravikant, Yuval Noah Harari — además de los 8 previos.)

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
