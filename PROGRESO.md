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

- **2026-07-13 — Profundizar: Bill Gates (sin backlog previo → discovery nuevo).** El backlog de
  Gates había quedado en 0 el 2026-07-12, así que esta vez la acción "Profundizar" arrancó con un
  barrido de descubrimiento chico: GatesNotes vía WebSearch (CNBC, Forbes, Kirkus — la página
  gatesnotes.com/books/reading-lists es JS-renderizada y no se pudo fetchear directo). Se
  cubrieron las dos listas más recientes no capturadas antes: **verano 2025** (5 memorias) y
  **fin de año 2025** (5 libros). `reconciliar.py` sobre 10 candidatos: **4
  YA-LINKED** (Personal History/Historia personal, Educated/Una educación, Born a Crime/Prohibido
  nacer y Abundance/Abundancia ya estaban) + **1 REVISAR** (Clearing the Air vs. Not the End of
  the World, mismo autor Hannah Ritchie → confirmado libro real y distinto, publicado 2025 por MIT
  Press, distinto del de 2024 → NUEVO) + **5 NUEVO** directos. Enriquecidos los **6 NUEVO** con
  MODO LIBRO (escritas directamente, sin subagente, por ser lote chico): Chasing Hope: A
  Reporter's Life [solo inglés, Knopf, asin 0593536568] (Nicholas D. Kristof); Surrender: 40
  canciones, una historia [ES, Reservoir Books, asin 8418897600] (Bono); Criaturas luminosas /
  Remarkably Bright Creatures [ES, Grijalbo, asin 1644738643] (Shelby Van Pelt); Clearing the Air
  [solo inglés, MIT Press, asin 0262052741] (Hannah Ritchie); Who Knew [solo inglés, Simon &
  Schuster, asin 1668096870] (Barry Diller); Cuando todos saben que todos lo saben / When
  Everyone Knows That Everyone Knows [ES, Paidós, asin 8449345103] (Steven Pinker).
  `detectar_duplicados.py`: 0 `[DUP]` exactos (Hannah Ritchie queda con 2 libros distintos, caso
  `[REV]` legítimo). ASIN 10 caracteres OK en los 6, integridad `recomendadoPor` OK. **Gates 34 →
  40 libros**; catálogo 278 → 284. Listicle de Gates regenerado a 40 (Clearing the Air a "Ciencia
  y tecnología"; Chasing Hope, Surrender y Who Knew a "Historia, memorias y negocios"; Cuando
  todos saben que todos lo saben a "Psicología y relaciones"; Criaturas luminosas a "Ficción").
  No se encontró todavía una lista de verano 2026 publicada — backlog de Gates vuelve a 0 hasta
  que GatesNotes publique una lista nueva.

- **2026-07-13 — Profundizar: Barack Obama (sin backlog previo → discovery nuevo).** Mismo caso
  que Gates: el backlog había quedado en 0 el 2026-07-12. Discovery vía WebSearch (Obama
  Foundation, Medium, Book Riot, Lit Hub — su propio Medium está indexado pero varias notas
  agregadoras dan más detalle de título/autor por libro) sobre las dos listas más recientes:
  **verano 2025** (10 libros) y **fin de año 2025** ("favoritos de libros, películas y música").
  Manifiesto de 19 candidatos → `reconciliar.py`: **2 YA-LINKED** (The Sirens' Call, Who is
  Government?, ya estaban del backlog cerrado en 2026-07-12) + **2 REVISAR** (We the People vs.
  These Truths, misma autora Jill Lepore → confirmado libro real y distinto, 2025, sobre la
  historia de las enmiendas constitucionales, ganador del Pulitzer 2026 → NUEVO; The Look vs.
  Becoming, misma autora Michelle Obama → confirmado libro real y distinto, 2025, sobre moda y
  estilo, no autobiografía → NUEVO) + **15 NUEVO** directos. Enriquecidos los **17 NUEVO** con
  MODO LIBRO (escritos directamente, sin subagente): Mark Twain [solo inglés, Penguin Press,
  asin 0525561722] (Ron Chernow); The Book of Records [solo inglés, Norton, asin 1324078650]
  (Madeleine Thien); El rey de las cenizas [ES, Salamandra, asin 8419851949] (S.A. Cosby);
  Audition [solo inglés, Riverhead, asin 059385232X] (Katie Kitamura); A Marriage at Sea [solo
  inglés, Riverhead, asin 0593854284] (Sophie Elmhirst); The Buffalo Hunter Hunter [solo inglés,
  Saga Press, asin 1668075083] (Stephen Graham Jones); Paper Girl [solo inglés, Celadon, asin
  0593656733] (Beth Macy); Flashlight [solo inglés, FSG, asin 037461637X] (Susan Choi); We the
  People [solo inglés, Liveright/Norton, asin 1631496085] (Jill Lepore); The Wilderness [solo
  inglés, Mariner, asin 0063318776] (Angela Flournoy); There Is No Place for Us [solo inglés,
  Crown, asin 0593237145] (Brian Goldstone); North Sun [solo inglés, A Strange Object/Deep
  Vellum, asin 1646053583] (Ethan Rutherford); 1929 [solo inglés, Viking, asin 0593296966]
  (Andrew Ross Sorkin); La soledad de Sonia y Sunny [ES, Salamandra, asin B0FWKJHNTB — ISBN-13
  979-prefijo, sin ISBN-10, se usó el ASIN] (Kiran Desai); Dead and Alive [solo inglés, Penguin
  Press, asin 0593834682] (Zadie Smith); What We Can Know [solo inglés, Knopf, asin 0593804724]
  (Ian McEwan); The Look [solo inglés, Crown, asin 0593800702] (Michelle Obama).
  `detectar_duplicados.py`: 0 `[DUP]` exactos (Jill Lepore y Michelle Obama quedan con 2 libros
  distintos cada una, casos `[REV]` legítimos). ASIN 10 caracteres OK en los 17, integridad
  `recomendadoPor` OK. **Obama 44 → 61 libros**; catálogo 284 → 301. Listicle de Obama
  regenerado a 61 (9 nuevos a "Ficción", 8 nuevos a "No ficción: memorias, ciencia y ensayo").
  Nota curiosa: "The Look" es la primera vez que Obama recomienda un libro escrito por su propia
  esposa. Backlog de Obama vuelve a 0 hasta su próxima lista (verano 2026 o fin de año 2026).

- **2026-07-13 — Discovery + Profundizar (tanda 1/3): Richard Branson.** Discovery vía
  `web_fetch` directo sobre la fuente documentada de su ficha (virgin.com/branson-family):
  **"70 must-read books"** (virgin.com/branson-family/richard-branson-blog/70-must-read-books,
  publicada 20/4/2017), lista vigente y superset de su "top 65" de 2016 (mismo blog, misma
  autoría, 2016 es subconjunto — se descartó por redundante). Manifiesto de 70 títulos →
  `reconciliar.py`: **4 YA-LINKED** (Where the Wild Things Are, Wild Swans, Mandela's Way, Black
  Box Thinking — backlog previo de Branson) + **4 CROSS-REF** (The Hitchhiker's Guide to the
  Galaxy, 1984, Cien años de soledad, Empieza con el porqué) + **3 REVISAR** (Mao: The Unknown
  Story vs. Wild Swans, misma autora Jung Chang → confirmado libro real y distinto, co-escrito
  con Jon Halliday → NUEVO; Originals vs. Give and Take/Think Again, mismo autor Adam Grant →
  confirmado libro real y distinto → NUEVO; Homo Deus vs. Sapiens, mismo autor Harari →
  confirmado libro real y distinto → NUEVO) + **59 NUEVO** directos. Total candidatos NUEVO: 62.
  Decisión de alcance (usuario): dividir los 62 NUEVO + 4 CROSS-REF (66 en total) en **3 tandas
  por relevancia**, la más relevante primero.
  **Tanda 1/3 (22 ítems) — hecha hoy:**
  - **4 CROSS-REF aplicados** (solo frontmatter, sin sección de cuerpo nueva — regla de cross-ref
    del playbook): the-hitchhiker-s-guide-to-the-galaxy, 1984, one-hundred-years-of-solitude,
    start-with-why → todos suman `richard-branson` a `recomendadoPor`.
  - **18 NUEVO enriquecidos** con MODO LIBRO vía 4 subagentes en paralelo (Sonnet): Originales:
    Cómo los inconformistas mueven el mundo [ES, Paidós, asin 8449333962] (Adam Grant); Homo
    Deus: Breve historia del mañana [ES, Debate, asin 8499926711] (Yuval Noah Harari); El largo
    camino hacia la libertad [ES, Debolsillo, asin 8466332693] (Nelson Mandela); Historia del
    tiempo [ES, Crítica, asin 8467033886] (Stephen Hawking); Cosmos [ES, Planeta, asin
    8432036269] (Carl Sagan); Vayamos adelante (Lean In) [ES, Conecta, asin 8415431678] (Sheryl
    Sandberg); Una verdad incómoda [ES, Gedisa, asin 8497842030] (Al Gore); Cuestión de justicia
    (Just Mercy) [ES, Península, asin 8499428770] (Bryan Stevenson); El Hobbit [ES, Minotauro,
    asin 8445012800] (J.R.R. Tolkien); La isla del tesoro [ES, Alianza, asin 8420666823] (R.L.
    Stevenson); Parque Jurásico [ES, Debolsillo, asin 8466342710] (Michael Crichton); Grandes
    esperanzas [ES, Alianza, asin 8491040978] (Charles Dickens); Mal de altura [ES, Desnivel,
    asin 8498294673] (Jon Krakauer); Fast Food: El lado oscuro de la comida rápida [ES, Grijalbo,
    asin 842533649X, categoria negocios en vez de ciencia] (Eric Schlosser); In Defense of Food
    [**sin ASIN confirmado** — no se pudo verificar de forma fiable una edición ES en Amazon,
    queda con `asin` vacío] (Michael Pollan); Yo sé por qué canta el pájaro enjaulado [ES, Libros
    del Asteroide, asin 8416213666] (Maya Angelou); Mao: la historia desconocida [ES, Taurus,
    asin 8430619607, autorLibro "Jung Chang y Jon Halliday" por ser coautoría real] (Jung
    Chang/Jon Halliday); Veinte mil leguas de viaje submarino [ES, Alianza, asin 8491813586]
    (Julio Verne). `detectar_duplicados.py`: 0 `[DUP]` exactos (Homo Deus/Sapiens y Mao/Wild
    Swans quedan como `[REV]` legítimos, mismo autor/a, libros distintos). ASIN 10 caracteres OK
    en 17/18 (In Defense of Food queda vacío). **Richard Branson 4 → 26 libros**; catálogo 301 →
    319. Sin listicle todavía (se espera a completar las 3 tandas para escribirlo con el
    manifiesto final).
  - **Pendiente: tanda 2/3 (23 ítems)** — Remote: Office Not Required, Limitless: Leadership
    That Endures, The Right Stuff, In the Heart of the Sea, Stalingrad: The Fateful Siege,
    Mountains Beyond Mountains, Shantaram, In Patagonia, The Quiet American, The World Without
    Us, No Future Without Forgiveness, A Full Life: Reflections at Ninety, Longitude, The Dice
    Man, Swallows and Amazons, The Adventures of Huckleberry Finn, The Adventures of Tom Sawyer,
    Peter Pan, The Jungle Book, George's Marvellous Medicine, Tales of the Unexpected, Oh, The
    Places You'll Go, Travels with Charley.
  - **Pendiente: tanda 3/3 (21 ítems)** — Winners: And How They Succeed, Abundance: The Future
    Is Better Than You Think, The Weather Makers, Big World Small Planet, Necker: A Virgin
    Island, Lost Ocean, Arctica: The Vanishing North, In-N-Out Burger, The Overview Effect,
    Happiness: A Guide to Developing Life's Most Important Skill, A Time for New Dreams, The
    Meaning of the 21st Century, Self Belief: The Vision, 101 Reasons to Get Out of Bed, If I
    Could Tell You Just One Thing, Letters to a Stranger, Ending the War on Drugs, Little Wins,
    Beyond the Blue, Obama: The Historic Presidency of Barack Obama, The Outermost House.

- **2026-07-16 — Enriquecimiento: Richard Branson, tanda 2/3 (23 fichas) + listicle
  regenerado.** Se enriquecen las 23 fichas pendientes de la tanda 2/3 vía 5 subagentes en
  paralelo (Sonnet), fuente primaria virgin.com/branson-family/richard-branson-blog/70-must-read-
  books (20/4/2017): Elegidos para la gloria [ES, Edhasa, asin 843393046X] (Tom Wolfe); En el
  corazón del mar [ES, Roca Editorial, asin 8432224405] (Nathaniel Philbrick); Stalingrado [ES,
  Booket, asin 8484325946] (Antony Beevor); Montañas tras las montañas [ES, Círculo de Tiza, asin
  8494645331] (Tracy Kidder); Shantaram [ES, Umbriel, asin 8415139136] (Gregory David Roberts);
  En la Patagonia [ES, Contraseña, asin 8499423124] (Bruce Chatwin); El americano tranquilo [ES,
  Debolsillo, asin 8420655899] (Graham Greene); El mundo sin nosotros [ES, Debate, asin
  8483067439] (Alan Weisman); Sin perdón no hay futuro [ES, Norma, asin 9872766185, título real
  distinto del sugerido "No hay futuro sin perdón"] (Desmond Tutu); A Full Life: Reflections at
  Ninety [**sin ASIN** — sin edición ES confirmada] (Jimmy Carter); Longitud [ES, Debate, asin
  8433972693] (Dava Sobel); El hombre de los dados [ES, Malpaso, asin 8416420254] (Luke
  Rhinehart); Las aventuras de Huckleberry Finn [ES, Akal, asin 8420678171] (Mark Twain); Las
  aventuras de Tom Sawyer [ES, Alianza, asin 8491042687] (Mark Twain); Swallows and Amazons
  [**sin ASIN** — solo existen box-sets en ES, sin edición individual] (Arthur Ransome); Peter
  Pan [ES, Anaya, asin 8420666742] (J.M. Barrie); El libro de la selva [ES, Alianza, asin
  8415601182] (Rudyard Kipling); La maravillosa medicina de Jorge [ES, Alfaguara, asin
  8420483184] (Roald Dahl); Relatos de lo inesperado [ES, Anagrama, asin 8433920863 — sorpresa,
  sí tiene edición ES vigente] (Roald Dahl); Remoto: No se requiere oficina [ES, Deusto, asin
  8496627926, categoria negocios] (Jason Fried y David Heinemeier Hansson); Limitless: Leadership
  That Endures [**sin ASIN ES** — ISBN real confirmado 0091955432, sin traducción] (Ajaz Ahmed);
  ¡Oh, cuán lejos llegarás! [ES, Beascoa, asin 1880507056] (Dr. Seuss); Viajes con Charley [ES,
  Nórdica, asin 8416112290] (John Steinbeck). `detectar_duplicados.py`: **0 `[DUP]`** exactos
  confirmado sobre los 434 archivos de `src/content/libros/`. ASIN real de 10 caracteres en 20/23
  (3 quedan vacíos: A Full Life, Swallows and Amazons, Limitless). **Richard Branson 26 → 49
  libros**; catálogo 411 → 434.
  - **Listicle regenerado** (`libros-que-recomienda-richard-branson.md`, `fecha` original
    2026-07-16 sin cambios, `fechaActualizado` 2026-07-16) para reflejar los 49 libros. Se
    reestructuró de 5 a **7 grupos temáticos** (dominante ficción(16) subdividida en "Infancia y
    clásicos para toda la vida" e "Novela y aventura para adultos"; categoría mínima
    psicología(1, Black Box Thinking) fusionada en "Negocios, liderazgo e innovación"; memorias
    (11) subdividida en "coraje y liderazgo" (8) y "expediciones/viajes" incorporada al grupo de
    historia real como "Historia, expediciones y aventuras reales" (7)). Grupos finales: Infancia
    y clásicos (8), Novela y aventura para adultos (8), Ciencia y cómo entender el mundo (7),
    Ciencia ficción (4), Historia/expediciones/aventuras reales (7), Negocios/liderazgo/
    innovación (7), Memorias de coraje y liderazgo (8). Verificación: 49/49 enlaces con título
    exacto de la ficha y `richard-branson` presente en `recomendadoPor`, 0 huérfanos, 0 extras.
  - **Pendiente: tanda 3/3 (21 ítems)** sigue sin tocar — ver listado completo arriba, en la
    entrada del 2026-07-13.

- **2026-07-13 — Discovery: Mark Zuckerberg (backlog nunca sourceado → discovery completo).**
  A diferencia de Gates/Obama/Branson (donde ya había un backlog cerrado), Zuckerberg nunca tuvo
  un discovery real: sus 4 libros previos (El fin del poder, Creatividad S.A., El problema de los
  tres cuerpos, Por qué fracasan los países) habían entrado como cross-refs sueltos, sin que se
  fetcheara nunca su fuente documentada ("A Year of Books", Facebook 2015, 23 títulos). Discovery
  vía `web_fetch` sobre **Wikipedia** (en.wikipedia.org/wiki/Mark_Zuckerberg_book_club, tabla
  completa con fecha de cada pick y cita a Business Insider/The Guardian por libro) + fs.blog
  (reseñas de cada título) → manifiesto de 23 títulos → `reconciliar.py`: **4 YA-LINKED** (los 4
  ya mencionados) + **3 CROSS-REF** (Sapiens, El optimista racional, El comienzo del infinito) +
  **3 REVISAR** (The Better Angels of Our Nature vs. Cuando todos saben que todos lo saben, mismo
  autor Steven Pinker → confirmado libro real y distinto, 2011 sobre el declive histórico de la
  violencia → NUEVO; Energy: A Beginner's Guide vs. Cómo funciona el mundo, mismo autor Vaclav
  Smil → confirmado libro real y distinto, 2006 → NUEVO; Genome vs. El optimista racional, mismo
  autor Matt Ridley → confirmado libro real y distinto, 1999 sobre genética → NUEVO) + **13 NUEVO**
  directos. Total NUEVO: 16.
  **3 CROSS-REF aplicados** (solo frontmatter): sapiens, the-rational-optimist,
  the-beginning-of-infinity → suman `mark-zuckerberg` a `recomendadoPor`.
  **16 NUEVO enriquecidos** con MODO LIBRO vía 4 subagentes en paralelo (Sonnet): Gang Leader for
  a Day [solo inglés, Penguin, asin 014311493X] (Sudhir Venkatesh); On Immunity: An Inoculation
  [solo inglés, Graywolf, asin 1555977200] (Eula Biss); La estructura de las revoluciones
  científicas [ES, FCE, asin 843750046X] (Thomas Kuhn); Rational Ritual [solo inglés, Princeton
  UP, asin 0691158282] (Michael Chwe); Dealing With China [solo inglés, Twelve, asin 1455504203]
  (Henry M. Paulson Jr.); Orwell's Revenge: The 1984 Palimpsest [solo inglés, Simon & Schuster,
  asin 1501127705] (Peter W. Huber); El color de la justicia (The New Jim Crow) [ES, Capitán
  Swing, asin 8494287923] (Michelle Alexander); Introducción a la historia universal
  (Al-Muqaddimah) [ES, FCE, asin 9681626451] (Ibn Jaldún); El jugador (The Player of Games) [ES,
  La Factoría de Ideas, asin 8498003563 — derivado por checksum de EAN-13 confirmado, no visto
  directo en URL de Amazon] (Iain M. Banks); Variedades de la experiencia religiosa [ES, Trotta,
  asin 849879644X] (William James); Portfolios of the Poor [solo inglés, Princeton UP, asin
  0691148198] (Collins/Morduch/Rutherford/Ruthven); The Idea Factory [solo inglés, Penguin, asin
  0143122797] (Jon Gertner); Orden mundial (World Order) [ES, Debate, asin 8499925715] (Henry
  Kissinger); Los ángeles que llevamos dentro (The Better Angels of Our Nature) [ES, Paidós, asin
  8449334640] (Steven Pinker); Energy: A Beginner's Guide [solo inglés, Oneworld, asin
  1786071339] (Vaclav Smil); Genoma (Genome) [ES, Taurus, asin 8430604146] (Matt Ridley).
  `detectar_duplicados.py`: 0 `[DUP]` exactos (Pinker, Smil, Ridley y Harari quedan con 2 libros
  cada uno, casos `[REV]` legítimos ya verificados). ASIN 10 caracteres OK en 16/16. **Mark
  Zuckerberg 4 → 23 libros (backlog "A Year of Books" completo, 0 pendientes)**; catálogo 319 →
  335. **Listicle de Zuckerberg regenerado** de 4 a 23 libros, agrupado por tema (Ciencia ficción,
  Poder/geopolítica/historia, Ciencia/mente/progreso, Economía y sociedad, Cultura/creatividad/
  sociedad humana); verificado con script: 23/23 links con `titulo` exacto, slug existente,
  `mark-zuckerberg` en `recomendadoPor`, 0 duplicados.

- **2026-07-13 — Discovery (solo discovery, sin enriquecer): Oprah Winfrey.** A pedido explícito
  del usuario ("sí, solo discovery"). Backlog previo: 5/5 libros ya enriquecidos, pero nunca se
  había fetcheado su fuente completa (los 5 eran cross-refs/picks sueltos). Fuente fetcheada:
  **beyondthebookends.com/oprahs-book-club-list** (actualizada 2/6/2026), listado completo mes a
  mes desde sept/1996 hasta jun/2026 (la fuente propia dice "107 libros de sept/1996 a sept/2025";
  el fetch trajo también los picks hasta jun/2026). Manifiesto de 114 candidatos (se separaron en
  líneas individuales los picks múltiples de un mismo mes: Faulkner ×3 en jun/2005, Kaye Gibbons
  ×2 en oct/1997, Dickens ×2 en dic/2010, Marilynne Robinson ×4 en mar/2021; se excluyeron del
  manifiesto los 5 ya confirmados en el catálogo) → `reconciliar.py`: **2 CROSS-REF** (Cien años
  de soledad, ya con Branson y Dua Lipa; The Covenant of Water) + **10 REVISAR**, todos resueltos
  a **NUEVO** tras confirmar que son obras reales y distintas del mismo autor/a: The Heart of a
  Woman vs. Yo sé por qué canta el pájaro enjaulado (Maya Angelou); Love in the Time of Cholera
  vs. Cien años de soledad (García Márquez); A Tale of Two Cities vs. Great Expectations
  (Dickens); Deacon King Kong vs. The Heaven & Earth Grocery Store (James McBride); Bewilderment
  vs. The Overstory (Richard Powers); Bittersweet vs. Quiet (Susan Cain); Small Things Like These
  vs. So Late in the Day (Claire Keegan); The Emperor of Gladness vs. On Earth We're Briefly
  Gorgeous (Ocean Vuong); All the Way to the River vs. Big Magic (Elizabeth Gilbert); Kin vs. An
  American Marriage (Tayari Jones) + **102 NUEVO** directos. **Total candidatos: 5 YA-LINKED + 2
  CROSS-REF + 112 NUEVO = 119 libros** en la historia del club (1996-2026), la lista histórica más
  grande de todo el catálogo hasta ahora (supera los 129 picks de Reese, aunque ahí también se
  habían filtrado antes de reconciliar).
  **No se tocó el catálogo** (0 fichas creadas, 0 cross-ref aplicados, 0 listicle) — por indicación
  explícita del usuario de correr *solo* el discovery. Manifiesto completo reconciliado queda en
  `/tmp/manifiesto_oprah_full.txt` (no versionado) y en esta entrada de PROGRESO.md como fuente de
  verdad para la próxima tanda. **Pendiente: decidir con el usuario cómo priorizar los 112 NUEVO +
  2 CROSS-REF** (la lista es abrumadoramente larga — 30 años de picks — así que probablemente
  convenga trabajarla por tandas cronológicas o por relevancia/consenso, siguiendo el mismo patrón
  usado con Reese Witherspoon y Richard Branson este mes).

- **2026-07-14 — Discovery: Satya Nadella.** Backlog previo: 4/4 libros ya enriquecidos (Mindset,
  Nonviolent Communication, The Boys in the Boat, Competing in the Age of AI), pero nunca se había
  fetcheado una fuente real y completa — la ficha del referente solo decía "blog de Microsoft y su
  libro Hit Refresh", sin URL concreta. Fuente fetcheada: **mostrecommendedbooks.com/people/
  satya-nadella-recommended-books** (actualizada 2/8/2025), agregador con 20 libros, cada uno con
  cita textual de Nadella (o de una nota periodística) y **URL primaria propia por libro**
  (fastcompany.com, weforum.org, x.com/satyanadella, entrevistas en YouTube) — cumple la regla de
  oro de MODO DESCUBRIR de registrar fuente por libro. Manifiesto de 20 → `reconciliar.py`: **4
  YA-LINKED** (los 4 ya mencionados) + **0 CROSS-REF** + **0 REVISAR** + **16 NUEVO** directos:
  Deep Learning (Ian Goodfellow), Forged in Crisis (Nancy Koehn), The New Leadership Literacies
  (Bob Johansen), The Great Transformation (Karl Polanyi), The Rise and Fall of American Growth
  (Robert J. Gordon), Prosperity (Colin Mayer), Shaping the Future of the Fourth Industrial
  Revolution (Klaus Schwab), The Great Convergence (Richard Baldwin), The Narrow Corridor (Daron
  Acemoglu y James A. Robinson — libro distinto de "Por qué fracasan los países", mismos autores,
  ya en catálogo vía Zuckerberg), An Astronaut's Guide to Life on Earth (Chris Hadfield), Tools and
  Weapons (Brad Smith), The Moment of Lift (Melinda Gates), No Rules Rules (Reed Hastings),
  AI Superpowers (Kai-Fu Lee), Masters of Scale (Reid Hoffman), Play Nice But Win (Michael Dell).
  **No se tocó el catálogo todavía** (0 fichas creadas) — queda como backlog listo para enriquecer,
  pendiente de que el usuario confirme si arrancamos la tanda de los 16 NUEVO.

- **2026-07-14 — Enriquecimiento: Satya Nadella (confirmado por el usuario).** Los 16 NUEVO del
  discovery de arriba, enriquecidos con MODO LIBRO vía 4 subagentes en paralelo (Sonnet): Deep
  Learning [solo inglés, MIT Press, asin 0262035618] (Ian Goodfellow, Yoshua Bengio y Aaron
  Courville — Nadella contrató a Bengio para el enfoque de IA de Microsoft tras leerlo); Forged in
  Crisis [solo inglés, Simon & Schuster, asin 1501174452] (Nancy Koehn); The New Leadership
  Literacies [solo inglés, Berrett-Koehler, asin 1626569614] (Bob Johansen); La gran transformación
  [ES, FCE, asin 6071652634] (Karl Polanyi); The Rise and Fall of American Growth [solo inglés,
  Princeton UP, asin 0691147728] (Robert J. Gordon); Prosperity [solo inglés, Oxford UP, asin
  0198824009] (Colin Mayer); Shaping the Future of the Fourth Industrial Revolution [solo inglés,
  Portfolio Penguin, asin 1984822616] (Klaus Schwab — Nadella figura como voz convocada en esta
  edición); La gran convergencia [ES, Antoni Bosch, asin 8494627112] (Richard Baldwin); El pasillo
  estrecho [ES, Deusto, asin 8423430812] (Daron Acemoglu y James A. Robinson — confirmado libro
  real y distinto de "Por qué fracasan los países", mismos autores); Guía de un astronauta para
  vivir en la Tierra [ES, Ediciones B, asin 8466655557] (Chris Hadfield); Tools and Weapons [solo
  inglés, Penguin Press, asin 1984877712] (Brad Smith y Carol Ann Browne); No hay vuelta atrás (The
  Moment of Lift) [ES, Conecta, asin 164473012X] (Melinda Gates); Aquí no hay reglas (No Rules
  Rules) [ES, Conecta, asin 8416883807] (Reed Hastings y Erin Meyer); Superpotencias de la
  inteligencia artificial (AI Superpowers) [ES, Deusto, asin 8423431312] (Kai-Fu Lee); Masters of
  Scale [solo inglés, Currency, asin 0593239083] (Reid Hoffman, June Cohen y Deron Triff); Play
  Nice But Win [solo inglés, Portfolio, asin 0593087747] (Michael Dell y James Kaplan).
  `detectar_duplicados.py`: 0 `[DUP]` exactos (Acemoglu/Robinson queda con 2 libros, caso `[REV]`
  legítimo). ASIN 10 caracteres OK en los 16 (con la gotcha conocida de `grep` mostrando falso
  negativo en 4 archivos — confirmado el contenido real vía Read). **Satya Nadella 4 → 20 libros**
  (backlog cerrado); catálogo 335 → 351. **Listicle nueva** (no existía antes):
  `/blog/libros-que-recomienda-satya-nadella`, escrita directamente con las 20 fichas, siguiendo la
  regla nueva de MODO LISTICLE (grupos temáticos balanceados, nunca por fecha): lead "Por dónde
  empezar" (4 destacados) + 4 grupos — Cultura organizacional y liderazgo (6), Tecnología e
  inteligencia artificial (4), Historia y economía: cómo cambian las sociedades (7), Memorias de
  liderazgo (3). Verificado con script: 20/20 links con `titulo` exacto tras corregir 10 títulos
  truncados (faltaba el subtítulo completo), slug existente, `satya-nadella` en `recomendadoPor`,
  0 duplicados.

- **2026-07-16 — Discovery (solo discovery, sin enriquecer en masa): Stephen King.** Backlog
  previo: 3/3 libros ya enriquecidos (El señor de las moscas, The Bleeding Heart, The Hair of
  Harold Roux), sin fuente documentada todavía en su ficha de referente más allá de la mención
  genérica a stephenking.com y su cuenta de X. Dos fuentes fetcheadas vía `WebSearch` + `web_fetch`:
  **fs.blog/stephen-king-reading-list** (reproduce íntegra la lista de ~96 libros que King publicó
  en su propio libro *On Writing: A Memoir of the Craft*, 2000 — cita textual: "estos son los
  mejores libros que leí en los últimos tres o cuatro años", el período en que escribió *La niña
  que amaba a Tom Gordon*, *Corazones en la Atlántida* y el propio *On Writing*; se excluyó 1 título
  no publicado — *The Sky in the Water*, de Tabitha King) y **mostrecommendedbooks.com/people/
  stephen-king-recommended-books** (26 libros, cada uno con cita textual de King y URL directa a su
  propio tuit en x.com/StephenKing como fuente primaria por libro, 2018-2022). Manifiesto combinado
  de 121 candidatos → `reconciliar.py`: **1 YA-LINKED** (Lord of the Flies, ya estaba) + **1
  CROSS-REF** (Into Thin Air / Mal de altura, ya en catálogo por Richard Branson) + **4 REVISAR**,
  los 4 resueltos a **NUEVO** tras confirmar que son obras reales y distintas del mismo autor/a:
  Oliver Twist vs. Great Expectations (Dickens); Enduring Love y The Cement Garden vs. What We Can
  Know (Ian McEwan, dos títulos distintos entre sí y del ya catalogado); The Dutch House vs. Tom
  Lake (Ann Patchett, ya en catálogo por Reese Witherspoon) + **115 NUEVO** directos.
  **1 CROSS-REF aplicado** (frontmatter + una frase breve fundada en la fuente real): into-thin-air
  suma `stephen-king` a `recomendadoPor` (cita paráfrasis de *On Writing*), `fechaActualizado`
  2026-07-16. Sin listicle de King todavía (no existía) → no aplica regla de propagación.
  **No se enriqueció el resto** (0 fichas nuevas creadas) — por alcance del pedido ("hagamos un
  discovery"), siguiendo el mismo patrón que Oprah Winfrey (2026-07-13). **Backlog: 119 candidatos
  NUEVO** (115 directos + 4 ex-REVISAR) listos para una futura tanda de "Profundizar Stephen King",
  divisible por relevancia/género como se hizo con Branson y Reese, dado el volumen. Nota temática:
  la lista de *On Writing* es sobre todo ficción literaria y suspenso de fines de los 90 (muchos
  títulos hoy con edición ES a confirmar caso por caso, varios agotados/descatalogados en inglés);
  la de mostrecommendedbooks.com es terror/thriller contemporáneo (2018-2022) con más probabilidad
  de edición ES vigente. Manifiesto completo queda en esta entrada de PROGRESO.md como fuente de
  verdad para la próxima tanda (archivo de trabajo `manifiesto_stephen_king.txt` no versionado).

- **2026-07-16 — Profundizar: Stephen King (tanda 1 de varias, "mezcla curada" pedida por
  Marcelo).** Del backlog de 119 candidatos del discovery de arriba, se armó una selección de los
  **20 títulos más consensuados/reconocibles** de ambas fuentes (tope de 20 por tanda, a pedido),
  enriquecidos con MODO LIBRO vía 4 subagentes en paralelo (Sonnet), todos con edición ES
  confirmada salvo 1: Hannibal [8497599373, DeBolsillo] y Cari Mora [8491294015, Suma de Letras]
  (Thomas Harris — dos obras distintas, mismo autor); Matar a un ruiseñor [8490701210, B de
  Bolsillo] (Harper Lee); Harry Potter y la piedra filosofal [8418173009, Salamandra] (J.K.
  Rowling); Cántico por Leibowitz [8490702241, Ediciones B] (Walter M. Miller Jr., cienciaficcion);
  El secreto [8426400302, Lumen] (Donna Tartt); Las cenizas de Ángela [8422671379, Maeva]
  (Frank McCourt, memorias); La Biblia envenenada [8484530256, Ediciones del Bronce] (Barbara
  Kingsolver); El paciente inglés [8420420905, Alfaguara] (Michael Ondaatje); Mientras agonizo
  [8420656577, Alianza] (William Faulkner); El corazón de las tinieblas [8420669806, Alianza]
  (Joseph Conrad); Un paseo por el bosque [8491873589, RBA] (Bill Bryson, memorias); Atando cabos
  [8472239217, Tusquets] (Annie Proulx); Y no quedó ninguno [846707051X, Espasa] (Agatha Christie —
  título vigente en ES, reemplazó a "Diez negritos"); La Novena Casa [8418359269, Hidra] (Leigh
  Bardugo); La casa holandesa [8491816593, Alianza/AdN] (Ann Patchett); La frontera [849139351X,
  HarperCollins Ibérica] (Don Winslow); Una cabeza llena de fantasmas [8416858268, Nocturna]
  (Paul Tremblay); Defender a Jacob [8499708684, La Esfera de los Libros] (William Landay). La
  única excepción: **Koko** [8440609884, Peter Straub] tiene ASIN real de una edición ES de
  Ediciones B (1989) pero **descatalogada** — se dejó igual (no es un ASIN inventado, la nota de
  edición al pie lo aclara), a diferencia de tratarlo como "solo inglés". `detectar_duplicados.py`:
  0 `[DUP]` exactos (Thomas Harris y Ann Patchett quedan con 2 libros cada uno, casos `[REV]`
  legítimos). ASIN 10 caracteres OK en las 20 (ninguno empieza con "B0"). **Stephen King 4 → 24
  libros** (incluye el cross-ref de Into Thin Air); catálogo 370 → 390. Sin listicle todavía (se
  espera completar más tandas del backlog antes de escribirla). **Backlog restante: 99 candidatos**
  (119 del discovery − 20 de esta tanda), para futuras tandas de hasta 20 títulos cada una.

- **2026-07-16 — Corrección + listicle: Stephen King.** A pedido de Marcelo: (1) `koko.md`
  corregida — las dos ediciones en español (Ediciones B, 1989 y una reedición posterior) están
  **descatalogadas** (confirmado vía casadellibro.com: "agotado en la editorial", solo reventa),
  así que se pasó a "solo inglés" con `asin` de la edición vigente de Anchor Books ("Blue Rose
  Trilogy, Book 1", asin `0307472205`, el mismo enlace que usa mostrecommendedbooks.com como fuente
  primaria). (2) **Listicle nueva** (no existía antes): `/blog/libros-que-recomienda-stephen-king`,
  escrita directamente con las 24 fichas (23 con ASIN + The Bleeding Heart, enriquecida pero sin
  ASIN confiable, con nota de "solo inglés" — cuenta igual como enriquecida según la regla del
  playbook). Lead "Por dónde empezar" (4 destacados: Matar a un ruiseñor, Hannibal, El secreto, Mal
  de altura) + 5 grupos temáticos balanceados: Terror, fantástico y ciencia ficción (5 — fusiona la
  única ficha de `cienciaficcion` para no dejarla huérfana), Crimen y suspenso (5), Clásicos de la
  literatura (4), Ficción contemporánea y literaria (7), Memorias y no ficción (3). Verificado por
  script: 24/24 links con `titulo` exacto (corregido 1 mismatch: "Mal de altura" → título completo
  "Mal de altura: La gran tragedia del Everest"), `stephen-king` presente en las 24, slug existente,
  0 huérfanos. Quedan **99 candidatos** en el backlog para las próximas tandas.

- **2026-07-16 — Discovery (solo discovery, sin enriquecer): J.K. Rowling.** Backlog previo: 4/4
  libros ya enriquecidos (Emma, La Ilíada, El pequeño caballo blanco, Team of Rivals), todos cross-
  refs sueltos — nunca se había fetcheado una fuente real y completa (la ficha del referente solo
  decía "jkrowling.com y entrevistas en medios literarios", sin URL concreta). Fuente fetcheada:
  **mostrecommendedbooks.com/people/jk-rowling-recommended-books** (27 libros, cada uno con cita
  textual de Rowling y URL de fuente primaria propia por libro — mayormente la entrevista "By the
  Book" del *New York Times*, 2012, y accio-quote.org, un archivo de entrevistas históricas de
  Rowling; también Business Insider, oprah.com y tuits propios en x.com/jk_rowling — cumple la
  regla de oro de MODO DESCUBRIR de registrar fuente por libro). Manifiesto de 27 → `reconciliar.py`:
  **4 YA-LINKED** (Team of Rivals, El pequeño caballo blanco, Emma, La Ilíada, ya estaban) + **0
  CROSS-REF** + **1 REVISAR**, resuelto a **NUEVO** tras confirmar que es una obra real y distinta
  del mismo autor: A Tale of Two Cities vs. Great Expectations (Dickens) + **22 NUEVO** directos.
  **Total: 23 candidatos NUEVO.** Dos de ellos son antologías/obra completa en vez de un título
  suelto (*The Collected Works of P. G. Wodehouse*, que Rowling nombró como uno de sus tres libros
  para una isla desierta, y *The Oxford Shakespeare: The Complete Works*, la misma respuesta) —
  quedan igual como candidatos por ahora; al enriquecer habrá que decidir si se cargan como
  antología o se reemplazan por una obra representativa, para no romper la convención de "1 ASIN =
  1 libro concreto" del catálogo. **No se enriqueció nada** (0 fichas nuevas creadas) — a pedido
  explícito ("haz un discovery"), mismo patrón que Oprah Winfrey y Stephen King. Manifiesto completo
  queda en esta entrada como fuente de verdad para la próxima tanda (archivo de trabajo
  `manifiesto_jk_rowling.txt` no versionado). Sin listicle de Rowling todavía (no existía).

- **2026-07-16 — Profundizar: J.K. Rowling (backlog cerrado salvo antologías).** De los 23
  candidatos del discovery de arriba, Marcelo pidió enriquecer todos **menos las 2 antologías**
  (*The Collected Works of P. G. Wodehouse* y *The Oxford Shakespeare: The Complete Works*, sus
  picks para "tres libros a una isla desierta" — quedan en backlog para decidir más adelante cómo
  representarlas sin romper la convención de "1 ASIN = 1 libro"). Enriquecidos los **21 restantes**
  con MODO LIBRO vía 4 subagentes en paralelo (Sonnet), todos con edición ES confirmada salvo 5
  títulos muy británicos y poco traducidos (marcados abajo): El viento en los sauces [8439280122,
  Everest] (Kenneth Grahame); Mujercitas [8418008652, Alma Editorial] (Louisa May Alcott); Los
  buscadores de tesoros [8415943385, Toromítico/Almuzara] (E. Nesbit); Zapatillas de ballet
  [8410025930, Blackie Books] (Noel Streatfeild); Belleza negra [8476515510, José J. Olañeta]
  (Anna Sewell); El castillo soñado [8478889892, Salamandra] (Dodie Smith); Lolita [8433968270,
  Anagrama] (Vladimir Nabokov); Historia de dos ciudades [8484287289, Alba] (Charles Dickens —
  confirmado libro real y distinto de *Grandes esperanzas*, ya en catálogo); Macbeth [8491050426,
  Penguin Clásicos, edición bilingüe] (William Shakespeare); La canción de Aquiles [8411485161,
  AdN] (Madeline Miller); The Collected Stories of Colette [**solo inglés**, 0374518653, Farrar,
  Straus and Giroux] (Colette — sin cita textual propia en la fuente, ficha honesta sobre ese
  punto: es el 3° de sus picks para isla desierta, sin comentario individual); Secretos de la
  carne: Vida de Colette [8498410827, Siruela] (Judith Thurman); Chéri [8417346228, Acantilado]
  (Colette); Nobles y rebeldes [8415625766, Libros del Asteroide] (Jessica Mitford — título ES real,
  no "Hijas y rebeldes"); La mujer que se daba con las puertas [8420429481, Alfaguara] (Roddy
  Doyle); Justicia: ¿Hacemos lo que debemos? [8499894143, Debate] (Michael J. Sandel); Los orígenes
  del totalitarismo [8420647713, Alianza] (Hannah Arendt); Poverty Safari [**solo inglés**,
  1912147033, Luath Press/Picador] (Darren McGarvey); Grimble [8426157190, Editorial Juventud —
  sorpresa, sí tiene ES] (Clement Freud); Manxmouse [**solo inglés**, 0007457316, HarperCollins
  Children's] (Paul Gallico); The Diaries of Auberon Waugh [**solo inglés**, 1888173416, The
  Akadine Press] (Auberon Waugh). `detectar_duplicados.py`: 0 `[DUP]` exactos (Dickens y Colette
  quedan con 2 libros cada uno, casos `[REV]` legítimos). ASIN 10 caracteres OK en las 21 (3 con
  `asin` vacío por solo-inglés real, ninguno "B0"). **J.K. Rowling 4 → 25 libros**; catálogo 390 →
  411. **Listicle nueva** (no existía antes): `/blog/libros-que-recomienda-j-k-rowling`, con las 25
  fichas: lead "Por dónde empezar" (4 destacados: Emma, Mujercitas, La Ilíada, Team of Rivals) + 6
  grupos temáticos balanceados — Infancia con estantería propia (4), Humor y fantasía para chicos
  (4), Clásicos de la literatura universal (6), Ficción contemporánea y Colette (4), Memorias y
  vidas literarias (4), Filosofía, historia y sociedad (3). Verificado por script: 25/25 links con
  `titulo` exacto, slug existente, `j-k-rowling` en `recomendadoPor`, 0 huérfanos. **Backlog
  restante: 2 antologías** (Wodehouse Complete Works, Oxford Shakespeare Complete Works) para
  decidir en una futura sesión.

- **2026-07-16 — Listicle: Richard Branson.** Revisado el estado actual del referente (26 libros
  enriquecidos, de la tanda 1/3 del discovery de 2026-07-13 — quedan 2 tandas más del backlog
  original, 44 candidatos, sin tocar) para escribir la listicle con lo ya enriquecido, sin esperar
  a cerrar las 3 tandas (a diferencia del criterio inicial de "esperar el manifiesto final"; se
  prioriza publicar con lo que hay, mismo patrón que Stephen King con su backlog parcial). No se
  enriqueció ninguna ficha nueva en esta sesión, solo se escribió la listicle. **Listicle nueva**
  (no existía antes): `/blog/libros-que-recomienda-richard-branson`, con las 26 fichas: lead "Por
  dónde empezar" (4 destacados: 1984, Cosmos, Cien años de soledad, El largo camino hacia la
  libertad) + 5 grupos temáticos balanceados — Ciencia y cómo entender el mundo (5), Ciencia
  ficción y aventura (4), Negocios, liderazgo e innovación (5 — fusiona la única ficha de
  `psicologia`, Pensamiento Caja Negra, para no dejarla huérfana), Ficción y clásicos de aventura
  (5), Memorias, coraje y justicia (7 — fusiona la única ficha de `historia`, Mao: la historia
  desconocida, junto a Cisnes salvajes de la misma autora). Verificado por script: 26/26 links con
  `titulo` exacto, slug existente, `richard-branson` en `recomendadoPor`, 0 huérfanos. **Pendiente:
  tandas 2/3 y 3/3 del backlog de Branson** (44 candidatos sourceados desde 2026-07-13, ver esa
  entrada para el detalle) — cuando se enriquezcan, la listicle va a necesitar regenerarse.

- **2026-07-17 — Discovery: James Clear (profundizar, backlog nunca sourceado).** James Clear solo
  tenía 3 libros vinculados (Sapiens, Daily Rituals, Hábitos atómicos), todos como cross-refs
  sueltos — nunca se había fetcheado su fuente documentada. Discovery vía `web_fetch` sobre las
  **13 subpáginas de categoría de jamesclear.com/best-books** (art, biographies, business, fitness,
  history, philosophy, psychology, science, self-help, writing, novels, fantasy, mystery) →
  manifiesto de **167 candidatos únicos** (deduplicados a mano; muchos libros se repiten entre
  categorías) → `reconciliar.py`: **1 YA-LINKED** (The War of Art) + **32 CROSS-REF directos** +
  **18 REVISAR** + **116 NUEVO** directos. Los 18 REVISAR se resolvieron a mano (Opus): 2 eran el
  mismo libro ya en catálogo con slug distinto al esperado → pasan a **CROSS-REF** (Daily Rituals:
  How Artists Work → `daily-rituals`; Sapiens: A Brief History of Humankind → `sapiens`); 15 eran
  libros distintos de autores ya presentes → pasan a **NUEVO** (Surely You're Joking Mr. Feynman!,
  The New New Thing, Moneyball, The Lost City of Z, Fooled by Randomness, Titan [confirmado: Ron
  Chernow escribió tanto Titan como una biografía separada de Mark Twain, ya en catálogo — son dos
  libros reales distintos], The Emperor of All Maladies, A Short History of Nearly Everything,
  State of Wonder, The Kite Runner, Everything I Never Told You, All the Light We Cannot See, The
  Lord of the Rings [trilogía como obra única, distinta de El Hobbit], The Martian, The Andromeda
  Strain); **1 se excluye** (The Harry Potter series — es la serie completa, no un libro individual,
  mismo criterio que las antologías excluidas de J.K. Rowling; ya está *Harry Potter y la piedra
  filosofal* individual en catálogo).
  **Totales finales: CROSS-REF=34, NUEVO=131, EXCLUIDO=1.** Es, por lejos, el backlog más grande de
  la sesión (más del doble que Stephen King). Manifiesto completo guardado en outputs
  (`manifiesto_james_clear.txt`) para la próxima sesión si hace falta.
  - **Decisión del usuario:** aplicar los cross-refs ahora, dejar los 131 NUEVO en backlog para
    otra sesión.
  - **32 cross-refs aplicados** vía 5 subagentes en paralelo (Sonnet), solo frontmatter (sin
    sección de cuerpo nueva, regla del playbook): just-kids, into-thin-air, the-boys-in-the-boat,
    a-walk-in-the-woods, just-mercy, mountains-beyond-mountains,
    the-autobiography-of-benjamin-franklin, the-blind-side, business-adventures,
    poor-charlie-s-almanack, thinking-fast-and-slow, nudge, the-4-hour-workweek, start-with-why,
    guns-germs-and-steel, meditations, the-little-prince, the-person-and-the-situation,
    a-brief-history-of-time, the-little-book-of-common-sense-investing, to-kill-a-mockingbird,
    siddhartha, americanah, a-thousand-splendid-suns, the-poisonwood-bible, the-alchemist, 1984,
    lord-of-the-flies, the-adventures-of-huckleberry-finn, the-hobbit, great-expectations,
    and-then-there-were-none. Al revisar, `sapiens` y `daily-rituals` ya tenían `james-clear`
    (eran 2 de los 3 vínculos originales del referente, junto con Hábitos atómicos) — el
    reconciliar.py los había marcado REVISAR por desajuste de slug contra el subtítulo del título
    del manifiesto, no por faltar el vínculo; sin cambios ahí. `detectar_duplicados.py`: 0 `[DUP]`
    sobre las 434 fichas del catálogo (sin cambios en el total, como corresponde a cross-refs puros).
    **James Clear pasa de 3 → 35 libros vinculados.** Sin listicle todavía (el referente está en la
    lista de "fichas 100%, falta escribir el post"; se puede escribir ahora con estos 35 o esperar
    a la próxima tanda de NUEVO — a decidir).
  - **Pendiente: 131 candidatos NUEVO** (fichas por crear, backlog completo en el manifiesto de
    outputs) + **1 excluido** (The Harry Potter series, es la saga completa no un libro puntual).

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
- **2026-07-14 — REGENERADA Dua Lipa** tras un cambio en `ENRIQUECER.md`/MODO LISTICLE: el criterio
  de organización pasó a ser único y obligatorio — **grupos temáticos balanceados, nunca por
  año/mes** (regla agregada: subdividir categorías dominantes, fusionar las chicas, apuntar a 3-6
  grupos de ~3-8 libros, fecha del pick siempre inline). El agrupado anterior por año (2023-2026)
  quedó desactualizado por esa regla nueva. Reorganizados los mismos 34 libros (sin tocar ninguna
  ficha del catálogo) en **6 grupos temáticos** + un lead `## Por dónde empezar` con 4 destacados:
  Guerra/historia/memoria colectiva (4), Raza/identidad/distopía (6), Duelo/pérdida/familia (7),
  Amor/deseo/voces transgresoras (5), Misterio/moralidad/suspenso literario (5), No ficción:
  memorias/crónica/ensayo (7) — la categoría `ficcion`, que concentraba 27/34 libros, quedó
  subdividida en 5 sub-temas editoriales en vez de un bloque único, tal como pide la regla nueva.
  Reseñas reescritas a partir de las mismas ya existentes (mismo dato factual, fecha de pick
  inline en cada una, sin reescribir desde cero). Verificado con script: 34/34 fichas con `titulo`
  exacto y `dua-lipa` en `recomendadoPor`, 0 duplicados fuera de las 4 menciones intencionales del
  lead. `fecha` original (2026-07-12) intacta; `fechaActualizado: 2026-07-14`.

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

- **2026-07-15 — Discovery + Profundizar: Warren Buffett.** Backlog previo: 6/6 libros ya
  enriquecidos (El inversor inteligente, Security Analysis, Acciones ordinarias y beneficios
  extraordinarios, Sam Walton: Made in America, Aventuras empresariales, Poor Charlie's
  Almanack), pero eran todos cross-refs/picks sueltos — nunca se había fetcheado una fuente real
  y completa (la ficha del referente no tenía línea "rastrearse a través de…", solo mencionaba de
  forma vaga "cartas anuales" y "décadas de entrevistas"). Fuentes fetcheadas vía `WebSearch` +
  `web_fetch`: **inc.com** ("Warren Buffett Recommends These 33 Books to Berkshire Hathaway
  Shareholders", Bill Murphy Jr., 2021 — parcialmente paywalled, solo se pudieron confirmar los 3
  primeros libros del ranking) y **cnbc.com** ("Full list of every book Warren Buffett has
  recommended...in his annual letters", dic. 2019 — cobertura completa de la década 2010-2019 con
  citas textuales de las cartas anuales por libro). Se extrajeron solo los libros con cita/contexto
  explícito y verificable en el texto fetcheado; se descartaron candidatos ambiguos (ej. "One Up On
  Wall Street", mencionado solo en agregadores sin cita primaria confirmada). Manifiesto de 12 →
  `reconciliar.py`: **0 YA-LINKED + 1 CROSS-REF + 0 REVISAR + 11 NUEVO**.
  - CROSS-REF: Shoe Dog ("Nunca te pares", Phil Knight) → + warren-buffett (ya estaba por Bill
    Gates). Frontmatter actualizado (recomendadoPor + resumen), sin sección de cuerpo nueva.
  - NUEVO (11, enriquecidos con MODO LIBRO vía 3 subagentes en paralelo, Sonnet): The Science of
    Hitting [solo inglés, Simon & Schuster, asin 0671621033] (Ted Williams — la metáfora de la
    "zona de strike de 77 celdas" que Buffett citó en su carta de 1977); Tap Dancing to Work [solo
    inglés, Portfolio/Penguin, asin 1591846803] (Carol Loomis); The Outsiders [solo inglés, Harvard
    Business Review Press, asin 1422162672] (William N. Thorndike); The Clash of the Cultures
    [solo inglés, Wiley, asin 1118122771] (John C. Bogle); Investing Between the Lines [solo
    inglés, McGraw-Hill, asin 0071714073] (L.J. Rittenhouse); Berkshire Hathaway Letters to
    Shareholders [solo inglés, compilación 2012 de Max Olson, asin 1595910778] (Warren Buffett);
    40 Chances: Finding Hope in a Hungry World [solo inglés, Simon & Schuster, asin 1451687869]
    (Howard G. Buffett, hijo de Warren); El pequeño libro para invertir con sentido común [ES,
    Deusto, asin 8423425401] (John C. Bogle); ¿Dónde están los yates de los clientes? [ES, Colección
    Baelo, asin 841230358X] (Fred Schwed); Limping on Water [solo inglés, autoeditado vía Smart
    Business Network, asin 0996408029] (Phil Beuth); Las reglas básicas de Warren Buffett [ES,
    Deusto, asin 8418464445] (Jeremy Miller). Categorías: negocios (9) y memorias (2: 40 Chances,
    Limping on Water). `detectar_duplicados.py`: 0 dups exactos (John C. Bogle queda con 2 libros
    distintos verificados: The Clash of the Cultures y El pequeño libro para invertir con sentido
    común). **Buffett 6 → 18 libros**; catálogo 351 → 362. Listicle regenerada de cero según MODO
    LISTICLE (grupos temáticos, no por año): "Por dónde empezar" (4 destacados) + 5 grupos — Los
    fundamentos del inversor en valor (3), Buffett y su círculo en sus propias palabras (4), Cómo
    funciona (y cómo falla) Wall Street (4), Negocios y sabiduría práctica (3), Memorias de
    líderes que admira (4). Verificado por script: 18/18 títulos exactos tras corregir 1 mismatch
    (40 Chances: Finding Hope in a Hungry World, texto de enlace venía truncado), `warren-buffett`
    presente en las 18 fichas, 0 duplicados de slug. Backlog de Buffett queda en 0 — cerrado hasta
    un próximo barrido (hay ~22 libros más del ranking completo de Inc.com sin confirmar, bloqueado
    por paywall/paginado; posible fuente para una futura tanda).

- **2026-07-16 — Profundizar: Naval Ravikant (backlog ya sourceado desde el discovery/reconcile
  previo).** Fuente: navalmanack.com/navals-recommended-reading (la lista curada del Almanack, con
  comentario real de Naval sobre cada libro), refetcheada completa para esta tanda.
  **Paso 1 — 7 cross-refs aplicados** (solo frontmatter + una frase breve fundada en la fuente real
  de Naval, sin inventar citas textuales): genome (+ mención de que Naval leyó/releyó todo Ridley),
  the-lessons-of-history (+ cita parafraseada "muy incisivo... cubre mucho terreno siendo chico"),
  the-sovereign-individual (+ "el mejor libro que leí desde Sapiens"), meditations (+ "un libro que
  me cambió la vida"), ficciones (+ "el autor más poderoso que leí que no escribía solo filosofía"),
  the-three-body-problem (+ mención como relectura habitual), man-s-search-for-meaning (+ mención
  como lectura de vuelta constante). Los 7 quedaron con `fechaActualizado: 2026-07-16`.
  **Paso 2 — 8 fichas nuevas** enriquecidas con MODO LIBRO vía 4 subagentes en paralelo (Sonnet),
  todas con edición ES confirmada y ASIN impreso real (0 vacíos, 0 "B0"): Jugarse la piel
  [8449335426, Paidós] y Antifrágil [8449328640, Paidós] (Nassim Nicholas Taleb, negocios); Siete
  breves lecciones de física [8433964003, Anagrama] y La realidad no es lo que parece [8490661901,
  Tusquets] (Carlo Rovelli, ciencia — dos obras distintas, sin solapar contenido); Cómo cambiar tu
  mente [8499929060, Debate] (Michael Pollan, ciencia — se preservó el matiz real de Naval de que
  no recomienda drogas y que la meditación logra lo mismo); La liberación del alma [8484455114,
  Gaia Ediciones] (Michael A. Singer, espiritualidad — sin cita propia de Naval en la fuente, se
  redactó sin inventarla, solo encuadrando el libro en su lista de espiritualidad junto a
  Krishnamurti/Osho/Marco Aurelio); El profeta [8471669226, Edaf] (Kahlil Gibran, espiritualidad —
  una de las citas más extensas y entusiastas de Naval en toda la fuente); Snow Crash [841750754X,
  Gigamesh] (Neal Stephenson, cienciaficcion).
  **Paso 3:** `detectar_duplicados.py` → 0 `[DUP]` exactos (Rovelli y Taleb quedan con 2-3 libros
  cada uno, casos `[REV]` legítimos ya verificados). Listicle regenerada de cero con las 23 fichas
  de Naval (`fecha` original 2026-07-10 sin tocar, `fechaActualizado: 2026-07-16`): "Por dónde
  empezar" (4 destacados: Sapiens, El individuo soberano, Meditaciones, El profeta) + 5 grupos
  balanceados — Inversión, riesgo y negocios (6), Física y el universo (4), Ciencia de la
  naturaleza humana y el progreso (4), Filosofía, espiritualidad y sentido de la vida (5), Ficción
  y ciencia ficción (4). Verificado por script: 23/23 links con `titulo` exacto, slug existente,
  `naval-ravikant` en `recomendadoPor` y `asin` presente en las 23, 0 slugs huérfanos, 0 fichas de
  Naval sin enlazar. **Naval Ravikant 4 → 23 libros** (7 de ellos ahora compartidos con otros
  referentes vía cross-ref); catálogo 362 → 370.

- **2026-07-17 — Acción "Sanear fichas" (Regla de atribución).** `python3 tools/auditar_fichas.py`
  detectó **40/434 fichas** con referentes del `recomendadoPor` no nombrados en el cuerpo (0 con
  exceso de secciones salvo `meditations`, que tenía 3). Saneadas las 40 en 4 tandas, tocando SOLO
  la parte de recomendación (línea consolidada "También lo recomienda(n) X [y Y]." antes del
  blockquote de edición), sin reescribir reseña/De qué trata/Para quién es, `fechaActualizado`
  bumpeado a 2026-07-17 en las 40: 1984, a-brief-history-of-time, a-gentleman-in-moscow,
  a-thousand-splendid-suns, a-walk-in-the-woods, americanah, an-american-marriage,
  and-then-there-were-none, business-adventures, great-expectations, guns-germs-and-steel,
  into-thin-air, just-kids, just-mercy, klara-and-the-sun, meditations, mountains-beyond-mountains,
  nudge, one-hundred-years-of-solitude, poor-charlie-s-almanack, project-hail-mary, sapiens,
  shoe-dog, siddhartha, start-with-why, the-4-hour-workweek, the-adventures-of-huckleberry-finn,
  the-alchemist, the-autobiography-of-benjamin-franklin, the-beginning-of-infinity, the-blind-side,
  the-hitchhiker-s-guide-to-the-galaxy, the-hobbit, the-little-book-of-common-sense-investing,
  the-little-prince, the-person-and-the-situation, the-poisonwood-bible, the-rational-optimist,
  thinking-fast-and-slow, to-kill-a-mockingbird.
  - **`meditations`** (único caso con 3 secciones): se consolidó la sección "Por qué lo recomienda
    Ryan Holiday" (razón genérica, sin cita/anécdota concreta) en la línea consolidada junto con
    James Clear; quedaron como sección propia Tim Ferriss (anécdota concreta: cita de Marco Aurelio
    en su heladera) y Naval Ravikant (cita textual + razón más rica, además `orden: 5` el más bajo
    de los 4 referentes) — criterio: razón más rica primero, `orden` como desempate.
  - **`sapiens.md`**: además de la atribución, se encontró y corrigió un bug de datos preexistente
    (no generado por esta tanda) — el cuerpo estaba cortado a mitad de palabra ("...nuestra espe")
    desde el commit inicial del repo (confirmado con `git show f3b585e`). Se completó la oración de
    forma neutra (sin inventar datos nuevos) y se agregó la línea consolidada con los 4 referentes
    faltantes. **Pendiente sugerido:** revisar si otras fichas viejas tienen el mismo tipo de corte.
  - ⚠️ **Nota de herramientas:** el mount que ve `bash` mostró versiones desincronizadas/truncadas
    de `into-thin-air.md`, `sapiens.md` y `shoe-dog.md` incluso varios minutos después de editarlos
    (bytes por debajo del propio HEAD de git, sin reflejar los cambios) — el re-audit por script vía
    bash siguió reportando esas 3 como pendientes. Contenido verificado manualmente correcto vía
    Read tool (fuente de verdad real, según el gotcha ya documentado en CONTENIDO.md §8). Resultado
    real: **40/40 saneadas**; el resultado de script quedó en 3/434 por el desync, no por un error
    real de contenido.
  - **Paso 3 — limpieza de `destacado` inerte:** eliminada la línea `destacado: ...` del frontmatter
    de los **40 archivos** de `src/content/autores/*.md` (campo descartado del schema). Confirmado
    con `grep -l '^destacado:' src/content/autores/*.md` → 0 resultados.

- **2026-07-17 — Discovery (solo discovery, sin enriquecer todavía): Malcolm Gladwell.** Backlog
  previo: 3/3 libros ya enriquecidos (The Blind Side, The Person and the Situation, Psychoanalysis:
  The Impossible Profession), pero la ficha del referente solo decía "su podcast" sin fuente
  concreta fetcheable. `WebSearch` no encontró una lista propia de Revisionist History con títulos
  explícitos, así que se buscaron agregadores con cita + fuente primaria por libro (mismo patrón
  que Nadella): **mostrecommendedbooks.com/malcolm-gladwell-books** y **readthistwice.com/person/
  malcolm-gladwell** (ambos JS-renderizados y devolvieron solo una porción del listado completo por
  lazy-load, igual que pasó antes con Reese Witherspoon/Oprah). De lo fetcheado, **18 candidatos**
  quedaron con fuente primaria verificable por libro (mayoría **tim.blog/2016/06/21/malcolm-gladwell/**
  — entrevista real en The Tim Ferriss Show — y también theweek.com/articles/509620, tweets propios
  de @Gladwell, NYT "By the Book", The Guardian y The Globe and Mail). Se descartaron a propósito la
  serie completa de Jack Reacher (30 libros, Lee Child) y "Irresistible" de Adam Alter: aparecían en
  el listado pero sin cita/fuente individual verificable en lo fetcheado — regla de oro de MODO
  DESCUBRIR, mejor lista corta 100% real que larga con dudosos.
  `reconciliar.py malcom-gladwell`: **0 YA-LINKED + 3 CROSS-REF + 0 REVISAR + 15 NUEVO**.
  - CROSS-REF: **Think Again** (Adam Grant, ya en catálogo vía Adam Grant/otros — falta sumar a
    Gladwell), **Just Kids** (Patti Smith, ya en catálogo vía Dua Lipa + James Clear), **Play Nice
    But Win** (Michael Dell, ya en catálogo vía varios referentes de negocios).
  - NUEVO (15): Strangers to Ourselves (Timothy D. Wilson), Merchant Princes (Leon A. Harris), The
    Russia House (John le Carré), The Little Drummer Girl (John le Carré), The Spy Who Came in from
    the Cold (John le Carré), Tinker Tailor Soldier Spy (John le Carré), The Checklist Manifesto
    (Atul Gawande), Traffic (Tom Vanderbilt), The Opposable Mind (Roger L. Martin), Freakonomics
    (Levitt/Dubner), First Friends (Gary Ginsberg), The Paris Architect (Charles Belfoure), A
    Thousand Pardons (Jonathan Dee), Drunk Tank Pink (Adam Alter), Together (Vivek H. Murthy).
    4 de estos títulos (Russia House, Little Drummer Girl, Spy Who Came in from the Cold, Tinker
    Tailor Soldier Spy) son la saga de espías de John le Carré que Gladwell recomendó en bloque en
    la entrevista de Tim Ferriss ("deberías leer al menos hasta Tinker Tailor...") — a diferencia de
    Reacher, acá sí hay cita textual y fuente concreta por título.
  **No se tocó el catálogo** (0 fichas creadas, 0 cross-ref aplicados) — discovery + reconciliación
  nada más, por ahora. Manifiesto completo con fuente por línea en
  `outputs/manifiesto_gladwell.txt` (scratchpad, no versionado). **Pendiente: confirmar con Marcelo
  si se enriquecen los 15 NUEVO + 3 CROSS-REF, y si conviene en una sola tanda o dividida** (sería
  Gladwell 3 → 21 libros).

- **2026-07-17 — Enriquecimiento + listicle: Malcolm Gladwell (confirmado por Marcelo: "enriquecer
  todo ahora").**
  - **3 CROSS-REF aplicados**: `think-again`, `just-kids` y `play-nice-but-win` suman
    `malcom-gladwell` a `recomendadoPor` + una línea/frase en el cuerpo que lo nombra con la cita
    real correspondiente (Regla de atribución), `fechaActualizado` a 2026-07-17.
  - **15 NUEVO enriquecidos** con MODO LIBRO vía 4 subagentes en paralelo (Sonnet), cada uno con la
    cita real de Gladwell y su fuente ya provistas (sin dejar que inventen razones): Strangers to
    Ourselves [solo inglés, Belknap/Harvard UP, asin 0674009363] (Timothy D. Wilson, psicologia); La
    casa Rusia [ES, Booket, asin 8408171712] y La chica del tambor [ES, Debolsillo, asin 8484504727]
    (John le Carré, ficcion); El espía que surgió del frío [ES, Best Seller, asin 8497930509] y El
    topo [ES, Biblioteca John le Carré, asin 8408161709] (le Carré, ficcion); El efecto Checklist
    [ES, Antoni Bosch, asin 849534856X] (Atul Gawande, negocios); Tráfico [ES, Debate, asin
    8483068435] (Tom Vanderbilt, ciencia); Merchant Princes [solo inglés, Harper & Row, asin
    0060117974] (Leon A. Harris, historia); The Opposable Mind [solo inglés, Harvard Business Press,
    asin 1422118924] (Roger L. Martin, negocios); Freakonomics [ES, Ediciones B, asin 8496581810]
    (Levitt/Dubner, negocios); First Friends [solo inglés, Twelve/Hachette, asin 1538702924] (Gary
    Ginsberg, historia); The Paris Architect [solo inglés, Sourcebooks Landmark, asin 1402284314]
    (Charles Belfoure, ficcion); A Thousand Pardons [solo inglés, Random House, asin 0812983386]
    (Jonathan Dee, ficcion); Drunk Tank Pink [solo inglés, Penguin, asin 0143124935] (Adam Alter,
    psicologia); Juntos [ES, Ares y Mares, asin 8491992634] (Vivek H. Murthy, psicologia).
    ASIN de 10 caracteres verificado en las 15 (todos vistos en URL real de Amazon, ninguno
    inventado); 8/15 con edición en español confirmada, 7/15 solo inglés.
  - `detectar_duplicados.py`: **0 `[DUP]`** exactos sobre los 449 archivos (John le Carré queda con
    4 libros, caso `[REV]` legítimo). ASIN 10 caracteres OK en las 15 nuevas + 3 cross-ref sin
    tocar. Re-audit de atribución: los 3 cross-ref + 15 nuevas quedan en regla (los 4 flags que
    reporta el script son el mismo gotcha de mount desincronizado de siempre — verificados
    manualmente vía Read tool como correctos: `into-thin-air`, `sapiens`, `shoe-dog`, `just-kids`).
  - **Listicle creado desde cero** (Gladwell nunca había tenido uno):
    `libros-que-recomienda-malcolm-gladwell.md`, `fecha`/`fechaActualizado` 2026-07-17, con las 21
    fichas. 5 grupos temáticos balanceados (sin `## Por dónde empezar`, no hizo falta con 21 libros
    bien repartidos): El universo de espías de John le Carré (4), Cómo pensamos —y por qué pensamos
    mal— (6, psicología/comportamiento), Sistemas, incentivos y por qué las cosas funcionan o no (4,
    negocios+ciencia — se sumó `traffic` acá en vez de a un grupo de ciencia de 1 solo libro, porque
    el propio Gladwell la llamó "heredera de Freakonomics"), Historias reales de gente extraordinaria
    (4, memorias+historia fusionadas), Ficción que lo atrapó (3, el resto de ficción fuera de le
    Carré). Verificado con script propio: 21/21 links con `titulo` EXACTO de la ficha, slug
    existente, `malcom-gladwell` presente en `recomendadoPor` de las 21, 0 huérfanos, 0 extras.
  **Malcolm Gladwell 3 → 21 libros**; catálogo 434 → 449.

- **2026-07-17 — Discovery (solo discovery, sin enriquecer todavía): Sam Altman.** Backlog previo:
  4/4 libros ya enriquecidos (El hombre en busca de sentido, Superinteligencia, El comienzo del
  infinito, The Making of the Atomic Bomb), fuente documentada como "Blog personal
  (blog.samaltman.com)" pero nunca fetcheada de forma completa. Esta vez el agregador
  **mostrecommendedbooks.com/sam-altman-books** SÍ devolvió el listado completo sin lazy-load
  (a diferencia de Gladwell/Reese/Oprah) — 45 libros individuales con fuente propia por título,
  mayoría de dos fuentes primarias reales: su propia respuesta en Hacker News a "what are the best
  books you recommend for a young startup founder" (news.ycombinator.com/item?id=10423017) y una
  captura de web.archive.org de 2015 de su estantería personal (blog.shelfie.com, "24 good books to
  read: here's what Sam Altman of Y Combinator is reading"), más varios tuits propios (@sama) y un
  post del blog de YC. Se excluyó a propósito la serie completa de Foundation (7 libros, Asimov)
  como bloque — solo se incluyó el primer libro *Foundation*, que ya estaba en catálogo, porque la
  fuente no especifica cuáles de los 7 recomendó puntualmente.
  `reconciliar.py sam-altman`: **2 YA-LINKED + 5 CROSS-REF + 3 REVISAR + 39 NUEVO**.
  - CROSS-REF: **Foundation** (Asimov, ya en catálogo), **Thinking, Fast and Slow** (Kahneman, ya en
    catálogo), **Brave New World** (Huxley, ya en catálogo), **Zero to One** (Thiel, ya en catálogo),
    **Meditations** (Marco Aurelio, ya en catálogo).
  - REVISAR (los 3, resueltos a NUEVO): **The Kite Runner** vs. *Mil soles espléndidos*, mismo autor
    Khaled Hosseini → confirmado libro real y distinto → NUEVO. **Einstein: His Life and Universe**
    vs. *El código de la vida* (The Code Breaker), mismo autor Walter Isaacson → confirmado libro
    real y distinto (biografía de Einstein vs. de Jennifer Doudna) → NUEVO. **The Principia** vs.
    *The System of the World* (ya en catálogo vía Neil deGrasse Tyson) → caso límite: la ficha
    existente es específicamente el Libro III del Principia de Newton en una edición suelta; lo que
    Altman recomendó en Hacker News es "The Principia" a secas, que en la edición de referencia
    (Univ. of California Press) es la obra completa de los 3 libros → decisión (a confirmar con
    Marcelo si no está de acuerdo): tratarlo como **NUEVO** por ser una edición de alcance distinto
    (obra completa vs. solo Libro III), mismo criterio que ya se usó con Cartas de un estoico /
    Cartas a Lucilio.
  - NUEVO (39, ordenados según aparecen en la fuente): Solution Selling (Michael Bosworth), The
    Supermen (Charles J. Murray), Endurance (Alfred Lansing), The Beak of the Finch (Jonathan
    Weiner), The Old Way (Elizabeth Marshall Thomas), Hold'em Poker for Advanced Players (David
    Sklansky), A Pattern Language (Christopher Alexander), Molecular Biology of the Cell (Bruce
    Alberts), Blitzscaling (Reid Hoffman), The Art of War in the Middle Ages (Charles Oman), A Life
    Decoded (J. Craig Venter), Winning (Jack Welch), The Transit of Venus (Shirley Hazzard),
    Plentiful Energy (Charles E. Till), The Death and Life of Great American Cities (Jane Jacobs),
    Pandaemonium (Humphrey Jennings), Plan B 3.0 (Lester R. Brown), Hateship, Friendship, Courtship,
    Loveship, Marriage (Alice Munro), Powering the Future (Robert B. Laughlin), The Principia (Isaac
    Newton, ver nota arriba), Fundamentals of Plasma Physics (Paul M. Bellan), Anna Karenina (Leo
    Tolstoy), Hunger of Memory (Richard Rodriguez), The Origin of Consciousness in the Breakdown of
    the Bicameral Mind (Julian Jaynes), The Trial of Socrates (I. F. Stone), The Republic (Platón),
    Dealers of Lightning (Michael A. Hiltzik), The Score Takes Care of Itself (Bill Walsh), The
    Constitutional Convention (James Madison/ed. Edward J. Larson), The Kite Runner (Khaled
    Hosseini, ver nota arriba), A Heartbreaking Work of Staggering Genius (Dave Eggers), The Fall
    (Albert Camus), The Legend of Henry Ford (Keith Sward), Einstein: His Life and Universe (Walter
    Isaacson, ver nota arriba), The Picture of Dorian Gray (Oscar Wilde), Call Me by Your Name
    (André Aciman), The Making of a Manager (Julie Zhuo), Medieval Technology and Social Change
    (Lynn White), Guns, Sails, and Empires (Carlo M. Cipolla), Secrets of Sand Hill Road (Scott
    Kupor), Mind of Napoleon (J. Christopher Herold), Skunk Works (Ben R. Rich).
  **No se tocó el catálogo** (0 fichas creadas, 0 cross-ref aplicados) — discovery + reconciliación
  nada más. Manifiesto completo con fuente por línea en `outputs/manifiesto_sam_altman.txt`
  (scratchpad, no versionado). **Pendiente: confirmar con Marcelo si se enriquecen los 39 NUEVO + 5
  CROSS-REF (44 en total, casi el triple del volumen de la tanda de Gladwell) y en qué tandas** —
  sería Sam Altman 4 → 46 libros si se aprueba todo.

- **2026-07-17 — Enriquecimiento tanda 1/3: Sam Altman (confirmado por Marcelo: "dividir en 3
  tandas de ~13").**
  - **5 CROSS-REF aplicados**: `foundation`, `thinking-fast-and-slow`, `brave-new-world`,
    `zero-to-one` y `meditations` suman `sam-altman` a `recomendadoPor` + una frase/línea en el
    cuerpo. Ojo: varias de estas fuentes son solo "estaba en su estantería" (relevamiento de 2015,
    sin cita propia) — se redactaron sin inventarle a Altman una opinión o anécdota que no dijo.
  - **Tanda 1/3 (13 NUEVO) enriquecidos** con MODO LIBRO vía 4 subagentes en paralelo (Sonnet),
    priorizados por consenso/relevancia (más referentes que también los recomiendan, según
    mostrecommendedbooks.com): Endurance. La prisión blanca [ES, Península, asin 8411001318]
    (Alfred Lansing, memorias); Anna Karénina [ES, Alianza, asin 8491814922] (Tolstoy, ficcion);
    Blitzscaling [ES, Empresa Activa, asin 8416997519] (Reid Hoffman, negocios); Einstein: su vida y
    su universo [ES, Debate, asin 8483067889] (Walter Isaacson, memorias — slug
    `einstein-his-life-and-universe` a propósito, para no chocar con `the-code-breaker.md` del mismo
    autor sobre Jennifer Doudna); The Score Takes Care of Itself [solo inglés, asin 1591843472]
    (Bill Walsh, negocios); The Making of a Manager [solo inglés, asin 0735219567] (Julie Zhuo,
    negocios); La República [ES, Alianza, asin 8420678813] (Platón, filosofia — el agente usó la
    edición ES real en vez del ASIN de la edición Hackett en inglés que traía la fuente original,
    siguiendo la regla de preferir edición ES); A Pattern Language [solo inglés, asin 0195019199]
    (Christopher Alexander, ciencia); Secrets of Sand Hill Road [solo inglés, asin 059308358X]
    (Scott Kupor, negocios — el agente cambió el ASIN Kindle de la fuente por el ISBN-10 real de
    tapa dura, porque Kindle no comisiona); Dealers of Lightning [solo inglés, asin 0887309895]
    (Michael A. Hiltzik, historia); El retrato de Dorian Gray [ES, Alianza, asin 8420654930] (Oscar
    Wilde, ficcion); El origen de la conciencia en la ruptura de la mente bicameral [ES, Julian
    Jaynes Society, asin 0979074479] (Julian Jaynes, psicologia); Llámame por tu nombre [ES,
    Alfaguara, asin 8420473898] (André Aciman, ficcion).
    En los libros cuya única fuente era el relevamiento de biblioteca de 2015 (sin cita propia de
    Altman), los agentes redactaron la sección de atribución con honestidad —"estaba en su
    biblioteca personal"— en vez de inventarle una razón o entusiasmo que no expresó.
  - `detectar_duplicados.py`: **0 `[DUP]`** exactos sobre los 462 archivos. ASIN 10 caracteres OK en
    las 13 nuevas. Re-audit de atribución: 0 pendientes reales (el script marcó 5 fichas por el
    gotcha de mount desincronizado de siempre, incluida `thinking-fast-and-slow` recién editada —
    verificada manualmente vía Read tool como correcta).
  - **Listicle regenerado** (`libros-que-recomienda-sam-altman.md`, tenía 4 libros desde 2026-07-10,
    `fechaActualizado` a 2026-07-17) con las 22 fichas actuales (4 previas + 13 nuevas + 5
    cross-ref). Reestructurado en 5 grupos temáticos: Startups, liderazgo y cómo construir
    compañías (6, negocios + A Pattern Language), Filosofía y psicología: cómo pensar y por qué
    pensamos mal (5), Ciencia ficción y futuros posibles (4), Historia real de gente que cambió todo
    (4, historia + memorias fusionadas), Literatura que también lo marcó (3, ficción). Verificado
    con script propio: 22/22 links con `titulo` EXACTO de la ficha, slug existente, `sam-altman`
    presente en `recomendadoPor` de las 22, 0 huérfanos, 0 duplicados de link.
  **Sam Altman 4 → 22 libros**; catálogo 449 → 462.
  **Backlog para tandas 2/3 (26 candidatos restantes, ya sourceados, sin enriquecer):** Solution
  Selling (Michael Bosworth), The Supermen (Charles J. Murray), The Beak of the Finch (Jonathan
  Weiner), The Old Way (Elizabeth Marshall Thomas), Hold'em Poker for Advanced Players (David
  Sklansky), Molecular Biology of the Cell (Bruce Alberts), The Art of War in the Middle Ages
  (Charles Oman), A Life Decoded (J. Craig Venter), Winning (Jack Welch), The Transit of Venus
  (Shirley Hazzard), Plentiful Energy (Charles E. Till), The Death and Life of Great American Cities
  (Jane Jacobs), Pandaemonium (Humphrey Jennings), Plan B 3.0 (Lester R. Brown), Hateship,
  Friendship, Courtship, Loveship, Marriage (Alice Munro), Powering the Future (Robert B. Laughlin),
  The Principia (Isaac Newton, ver nota de la entrada de discovery sobre el caso límite con The
  System of the World), Fundamentals of Plasma Physics (Paul M. Bellan), Hunger of Memory (Richard
  Rodriguez), The Trial of Socrates (I. F. Stone), The Constitutional Convention (James Madison/ed.
  Edward J. Larson), The Kite Runner (Khaled Hosseini), A Heartbreaking Work of Staggering Genius
  (Dave Eggers), The Fall (Albert Camus), The Legend of Henry Ford (Keith Sward), Medieval Technology
  and Social Change (Lynn White), Guns, Sails, and Empires (Carlo M. Cipolla), Mind of Napoleon (J.
  Christopher Herold), Skunk Works (Ben R. Rich). (Nota: son ~28 en la lista de arriba, no 26 —
  quedaron algunos títulos de más al repartir; ajustar tandas 2/3 en ~13-15 cada una al retomar.)

- **2026-07-18 — Acción "Sanear fichas" (nota de edición).** `python3 tools/auditar_fichas.py`
  reportó **24/462 fichas** con flags, pero la verificación manual vía Read tool (fuente de verdad,
  el mount de `bash` sigue sirviendo contenido stale/truncado — mismo gotcha ya documentado el
  2026-07-17) mostró que **18 de las 24 eran falsos positivos**: `brave-new-world`, `ficciones`,
  `foundation`, `genome`, `into-thin-air`, `just-kids`, `man-s-search-for-meaning`, `meditations`,
  `sapiens`, `shoe-dog`, `the-alchemist`, `the-lessons-of-history`, `the-sovereign-individual`,
  `the-three-body-problem`, `think-again`, `thinking-fast-and-slow`, `zero-to-one` ya tenían la nota
  de edición y/o la atribución correcta (varias de estas ya se habían saneado el 2026-07-17: nota de
  ese día sobre el mismo gotcha con `into-thin-air`/`sapiens`/`shoe-dog`/`just-kids`, que sigue sin
  resolverse). `koko` también es falso positivo: tiene nota de edición real (explica que las 2
  ediciones ES están descatalogadas) pero con una redacción que no matchea el regex del script
  (no empieza con "Edición"/"Por ahora"/"Disponible") — contenido correcto, no se tocó.
  **6 fichas con problema real** (nota de edición faltante, confirmada por Read): `business-adventures`
  (ya tenía la atribución de James Clear del 2026-07-17, pero no la nota → agregada: Deusto, trad.
  Iván Barbeitos), `common-stocks` (Deusto, trad. Mar Vidal), `educated` (Debolsillo, trad. Antonia
  Martín), `the-anxious-generation` (Deusto), `the-coming-wave` (Debate, trad. Clàudia Fernández
  Morenas), `the-intelligent-investor` (Deusto, edición revisada con comentarios de Jason Zweig,
  trad. Idoia Bengoechea — la ficha ya mencionaba esta edición en prosa pero le faltaba el blockquote
  formal). Las 6 verificadas por `WebSearch` contra fuentes reales (Amazon.es, Casa del Libro,
  PlanetadeLibros), sin inventar editorial. Solo se agregó la línea de edición + bump de
  `fechaActualizado` a 2026-07-18; el resto de cada ficha quedó intacto.
  **Pendiente sugerido:** el gotcha de mount desincronizado sigue activo y ya afectó 2 auditorías
  seguidas (2026-07-17 y 2026-07-18) con falsos positivos superpuestos — conviene que cualquier
  futura acción "Sanear" verifique cada `[FIX]` del script contra el Read tool antes de tocar nada,
  no confiar en el output crudo de `auditar_fichas.py` corrido vía `bash`.

- **2026-07-18 — Acción "Sanear fichas" (atribución huérfana), tercera tanda del día.** Marcelo
  corrió `auditar_fichas.py` nativo en Windows (worklist limpia, sin el gotcha de mount) y devolvió
  **32 fichas [FIX]**: 31 con "atribución huérfana tras 'Para quien es'" y 1 (`koko`) con "sin nota
  de edición". Verificado `koko.md` por tercera vez vía `Read`: sigue siendo falso positivo (la nota
  de edición existe, línea 32, pero empieza con "Hubo dos ediciones..." en vez de "Edición en
  español/Por ahora/Disponible", así que no matchea el regex) — no se tocó. Las 31 restantes se
  sanearon en 4 tandas de 8 con `Edit` quirúrgico: se movió la línea "También lo recomienda(n) X"
  desde después de "Para quién es" al cierre del último párrafo de la sección de recomendación
  ("Por qué lo recomienda…"), y se borró la línea huérfana + el blank line sobrante: `1984`,
  `a-brief-history-of-time`, `a-thousand-splendid-suns`, `a-walk-in-the-woods`, `americanah`,
  `and-then-there-were-none`, `great-expectations`, `guns-germs-and-steel`, `just-kids`,
  `just-mercy`, `klara-and-the-sun`, `mountains-beyond-mountains`, `nudge`,
  `one-hundred-years-of-solitude`, `play-nice-but-win`, `project-hail-mary`, `shoe-dog`,
  `siddhartha`, `start-with-why`, `the-adventures-of-huckleberry-finn`,
  `the-autobiography-of-benjamin-franklin`, `the-beginning-of-infinity`, `the-blind-side`,
  `the-hobbit`, `the-little-book-of-common-sense-investing`, `the-little-prince`,
  `the-person-and-the-situation`, `the-rational-optimist`, `think-again`, `thinking-fast-and-slow`,
  `to-kill-a-mockingbird`, `zero-to-one`. Caso especial: `thinking-fast-and-slow` no tiene sección
  "Por qué lo recomienda X" propia (Kahneman es el autor, no hay un desarrollo de recomendador
  separado), así que la frase se fundió al cierre del párrafo introductorio en vez de una sección
  de recomendación inexistente — señalarlo si se vuelve a tocar esa ficha. `fechaActualizado`
  bumpeado a 2026-07-18 en las 31. Cada ficha verificada por `Read` tras el `Edit` (defecto fuera +
  secciones intactas). **Pendiente:** pedirle a Marcelo que re-corra el audit para confirmar 0
  fichas a sanear.

- **2026-07-18 — Acción "Sanear fichas" (encabezado "También lo recomienda" → línea consolidada),
  segunda tanda del día.** Dado que el mount de `bash` seguía sirviendo versiones truncadas/viejas
  incluso del propio `tools/auditar_fichas.py` (72 líneas vía `bash` contra las 94 reales vía Read
  tool), esta vez el audit se hizo **enteramente con el tool `Grep`** (no `bash`), que sí lee el
  contenido real: confirmado cruzando `PROGRESO.md` (`bash` reportaba 681 líneas; el archivo real
  tiene 1267+). Barrido sobre las 462 fichas con el patrón `^##\s+Tambi[eé]n lo recomienda` encontró
  **10 fichas** que todavía usaban el formato viejo (sección H2 separada por recomendador) en vez de
  la línea consolidada que exige la Regla de atribución desde el 2026-07-17: `ficciones`, `genome`,
  `into-thin-air`, `man-s-search-for-meaning`, `poor-charlie-s-almanack`, `the-alchemist`,
  `the-intelligent-investor`, `the-lessons-of-history`, `the-sovereign-individual`,
  `the-three-body-problem`. En 3 de ellas (`into-thin-air`, `poor-charlie-s-almanack`,
  `the-alchemist`) también había una "atribución huérfana" (línea "También lo recomienda(n) X."
  suelta después de "Para quién es" o de "De qué trata", sin relación con la sección de
  recomendación). Se unificó cada una en **una sola sección** "## Por qué lo recomienda(n) X [y Y]"
  tejiendo la prosa existente (sin cortar ni inventar contenido) y, donde había un tercer o cuarto
  referente ya desarrollado en prosa, se preservó esa prosa dentro de la misma sección en vez de
  recortarla a una sola línea (regla dura de Sanear: no acortar lo que ya está bien). Bump de
  `fechaActualizado` a 2026-07-18 en las 9 que no lo tenían ya (`the-intelligent-investor` ya
  estaba en 2026-07-18 por la tanda anterior). De paso, se confirmó por segunda vez que `koko.md`
  es falso positivo real (nota de edición con redacción propia que no matchea el regex del script,
  contenido correcto) vía diff de listas `Grep` (461/462 fichas matchean el regex de edición; la
  única que no es `koko`). **Pendiente:** ninguno de los 10 referentes tocados tiene listicle
  publicado con esos libros afectados por el cambio de formato (el cambio es solo de presentación,
  no de contenido ni de `recomendadoPor`), así que no hace falta regenerar ningún listicle por esta
  tanda.

- **2026-07-19 — Acción "Profundizar": Oprah Winfrey, tanda 1.** El manifiesto del discovery del
  2026-07-13 (119 libros) se había perdido (vivía solo en `/tmp`, no versionado — mismo gotcha ya
  documentado con Dua Lipa tanda 1). Se re-fetcheó **beyondthebookends.com/oprahs-book-club-list**
  (mismo resultado: 107 libros de sept/1996 a sept/2025, más los picks hasta jun/2026) y se
  reconcilió a mano contra el catálogo actual. **5 YA-LINKED**: `a-new-earth` (ene 2008, repetido
  ene 2025), `becoming` (nov 2018), `hello-beautiful` (mar 2023), `the-underground-railroad`
  (ago 2016). **7 CROSS-REF aplicados hoy** (se sumó `oprah-winfrey` a `recomendadoPor` + se la
  nombró en el cuerpo, Regla de atribución): `one-hundred-years-of-solitude` (ene 2004),
  `anna-karenina` (may 2004), `the-poisonwood-bible` (jun 2000), `great-expectations` (dic 2010,
  pick conjunto con *Historia de dos ciudades*), `an-american-marriage` (feb 2018),
  `the-covenant-of-water` (may 2023), y un 7mo detectado recién vía `detectar_duplicados.py`
  (Marcelo corrió el script y el `[REV]` de Dickens con 2 libros hizo notar que `a-tale-of-two-
  cities` YA existía en el catálogo, de una tanda de J.K. Rowling — lo había marcado como NUEVO
  por error): `a-tale-of-two-cities` (dic 2010, pick conjunto con *Grandes esperanzas*).
  De paso, en `an-american-marriage` y `the-poisonwood-bible`
  se corrigió una atribución huérfana preexistente que el regex de `auditar_fichas.py` no detecta
  (empezaba con "Este libro también..." o quedaba después de "De qué trata" en vez de matchear
  `^También lo recomiend` justo tras "Para quién es") — anotar como posible mejora futura del script.
  **7 NUEVO enriquecidos (tanda 1, por relevancia/consenso)**: `east-of-eden` (jun 2003, Steinbeck),
  `the-road` (mar 2007, McCarthy, Pulitzer), `night` (ene 2006, Wiesel), `song-of-solomon`
  (oct 1996, Toni Morrison), `the-corrections` (sep 2001, Franzen), `middlesex` (jun 2007,
  Eugenides, Pulitzer), `wild` (jun 2012, Strayed — relanzamiento del club 2.0). ASIN de las 7
  verificado real vía WebSearch (Amazon, ISBN-10 de edición en español), ninguno inventado.
  **Catálogo: +7 fichas nuevas, +7 vínculos cross-ref.**

  **Manifiesto completo reconciliado (fuente de verdad, para que no se vuelva a perder)** —
  cronológico tal cual la fuente, título (autor) — año/mes — todo lo no marcado abajo como
  YA-LINKED/CROSS-REF/NUEVO-enriquecido queda como **backlog NUEVO pendiente**:

  **1996**: sep — The Deep End of the Ocean (Jacquelyn Mitchard); oct — Song of Solomon ✅ (tanda 1); nov —
  The Book of Ruth (Jane Hamilton); dic — She's Come Undone (Wally Lamb).
  **1997**: feb — Stones from the River (Ursula Hegi); abr — The Rapture of Canaan (Sheri
  Reynolds); may — The Heart of a Woman (Maya Angelou, distinta de *Yo sé por qué canta el pájaro
  enjaulado*, ya en catálogo); jun — Songs in Ordinary Time (Mary McGarry Morris); sep — A Lesson
  Before Dying ✅ (tanda 3); oct — A Virtuous Woman + Ellen Foster (Kaye Gibbons, 2 libros);
  dic — 3 libros infantiles de Bill Cosby (evaluar si corresponde incluirlos, fuera del perfil
  habitual del catálogo).
  **1998**: ene — Paradise ✅ (tanda 3); mar — Here on Earth (Alice Hoffman); abr — Black and
  Blue (Anna Quindlen); may — Breath, Eyes, Memory ✅ (tanda 3); jun — I Know This Much Is
  True (Wally Lamb); sep — What Looks Crazy on an Ordinary Day (Pearl Cleage); oct — Midwives
  ✅ (tanda 3, solo inglés); dic — Where the Heart Is (Billie Letts).
  **1999**: ene — Jewel (Bret Lott); feb — The Reader ✅ (tanda 2); mar — The Pilot's Wife
  (Anita Shreve); may — White Oleander ✅ (tanda 3, solo inglés); jun — Mother of Pearl (Melinda Haynes); sep —
  Tara Road (Maeve Binchy); oct — River, Cross My Heart (Breena Clarke); nov — Vinegar Hill
  (A. Manette Ansay); dic — A Map of the World (Jane Hamilton).
  **2000**: ene — Gap Creek (Robert Morgan); feb — Daughter of Fortune ✅ (tanda 2); mar — Back
  Roads (Tawni O'Dell); abr — The Bluest Eye ✅ (tanda 2); may — While I Was Gone (Sue Miller);
  jun — The Poisonwood Bible ✅ (cross-ref); ago — Open House (Elizabeth Berg); sep — Drowning Ruth
  (Christina Schwarz); nov — House of Sand and Fog ✅ (tanda 2, solo inglés).
  **2001**: ene — We Were the Mulvaneys ✅ (tanda 2); mar — Icy Sparks (Gwyn Hyman Rubio);
  may — Stolen Lives (Malika Oufkir); jun — Cane River (Lalita Tademy); sep — The Corrections ✅;
  nov — A Fine Balance ✅ (tanda 2).
  **2002**: ene — Fall on Your Knees (Ann-Marie MacDonald); abr — Sula ✅ (tanda 2).
  **2003**: jun — East of Eden ✅; sep — Cry, The Beloved Country ✅ (tanda 3).
  **2004**: ene — One Hundred Years of Solitude ✅ (cross-ref); abr — The Heart Is a Lonely Hunter
  ✅ (tanda 3); may — Anna Karenina ✅ (cross-ref); sep — The Good Earth ✅ (tanda 3).
  **2005**: jun — The Sound and the Fury ✅ (tanda 3) + As I Lay Dying ✅ (cross-ref, tanda 3 —
  ya estaba en catálogo por Stephen King) + Light in August ✅ (tanda 3), pick triple de Faulkner;
  sep — A Million Little Pieces ✅ (tanda 2).
  **2006**: ene — Night ✅.
  **2007**: ene — The Measure of a Man (Sidney Poitier); mar — The Road ✅; jun — Middlesex ✅; oct —
  Love in the Time of Cholera ✅ (tanda 2, distinta de *Cien años de soledad*, ya en catálogo);
  nov — Pillars of the Earth ✅ (tanda 2).
  **2008**: ene — A New Earth (YA-LINKED); sep — The Story of Edgar Sawtelle ✅ (tanda 3).
  **2009**: sep — Say You're One of Them ✅ (tanda 3).
  **2010**: sep — Freedom ✅ (tanda 2); dic — Great Expectations ✅ (cross-ref) + A Tale of Two Cities
  ✅ (cross-ref, agregado tras `detectar_duplicados.py` — ver nota en tanda 1).
  **2012**: jun — Wild ✅; dic — The Twelve Tribes of Hattie ✅ (tanda 3).
  **2014**: ene — The Invention of Wings ✅ (tanda 2).
  **2015**: feb — Ruby (Cynthia Bond).
  **2016**: ago — The Underground Railroad (YA-LINKED); sep — Love Warrior ✅ (tanda 3, solo inglés).
  **2017**: jun — Behold the Dreamers ✅ (tanda 3, solo inglés).
  **2018**: feb — An American Marriage ✅ (cross-ref); jun — The Sun Does Shine ✅ (tanda 3, solo
  inglés); nov — Becoming (YA-LINKED).
  **2019**: sep — The Water Dancer ✅ (tanda 2); nov — Olive, Again ✅ (tanda 2).
  **2020**: ene — American Dirt ✅ (tanda 2); abr — Hidden Valley Road ✅ (tanda 3, categoria
  psicologia); jun — Deacon King Kong ✅ (tanda 3, solo inglés, distinto de *The Heaven & Earth
  Grocery Store*, ya en catálogo); nov — Caste ✅ (tanda 2).
  **2021**: mar — Gilead ✅ (tanda 2) + Home ✅ + Lila ✅ + Jack ✅ (tanda 3 — saga de Marilynne
  Robinson completa, 4/4); jun — The Sweetness of
  Water ✅ (tanda 3); ago — The Love Songs of W. E. B. Du Bois (Honorée Fanonne Jeffers); sep —
  Bewilderment (Richard Powers, distinto de *The Overstory*, ya en catálogo).
  **2022**: feb — The Way of Integrity (Martha Beck); abr — Finding Me ✅ (tanda 3, solo inglés);
  jun — Nightcrawling ✅ (tanda 3); sep — That Bird Has My Wings (Jarvis Jay Masters); oct — Demon
  Copperhead ✅ (tanda 2, distinto de *La Biblia envenenada*, ya en catálogo).
  **2023**: feb — Bittersweet (Susan Cain, distinto de *Quiet*, ya en catálogo); mar — Hello
  Beautiful (YA-LINKED); may — The Covenant of Water ✅ (cross-ref); sep — Wellness ✅ (tanda 3);
  oct — Let Us Descend ✅ (tanda 2, solo inglés).
  **2024**: feb — The Many Lives of Mama Love (Lara Love Hardin); may — Long Island ✅ (tanda 2);
  jun — Familiaris (David Wroblewski); sep — Tell Me Everything ✅ (tanda 3, distinto de *Luz de
  febrero*, mismo universo Amgash/Lucy Barton); oct — From Here
  to the Great Unknown ✅ (tanda 3, solo inglés); dic — Small Things Like These (Claire
  Keegan, distinto de *So Late in the Day*, ya en catálogo).
  **2025**: ene — A New Earth (repetido, YA-LINKED); feb — Dream State (Eric Puchner); mar — The
  Tell (Amy Griffin); abr — Matriarch (Tina Knowles); may — The Emperor of Gladness (Ocean Vuong,
  distinto de *On Earth We're Briefly Gorgeous*, ya en catálogo); jun — The River Is Waiting ✅
  (tanda 3, solo inglés); jul — Culpability (Bruce Holsinger); ago — Bridge of Sighs ✅ (tanda 3,
  sorpresa: sí tiene edición en español pese a ser pick reciente); sep — All the
  Way to the River (Elizabeth Gilbert, distinto de *Big Magic*, ya en catálogo); oct — A Guardian
  and A Thief (Megha Majumdar); nov — Some Bright Nowhere (Ann Packer).
  **2026**: ene — Enough (Oprah Winfrey + Ania M. Jastreboff — libro propio de Oprah, evaluar si
  corresponde cargarlo como "recomendación"); feb — Kin (Tayari Jones, distinto de *Un matrimonio
  americano*, ya en catálogo); abr — Go Gentle (Maria Semple); may — John of John (Douglas Stuart);
  jun — Little Wonder (Sophie Chen Keller).

  **Pendiente tras tanda 1:** ~99 candidatos NUEVO + revisar el caso `Enough` (¿corresponde?).
  Fuente estable (beyondthebookends.com/oprahs-book-club-list) — se puede re-fetchear sin
  problema si hace falta, así que el riesgo de pérdida de este manifiesto es bajo ahora que además
  queda completo acá.

- **2026-07-19 — Acción "Profundizar": Oprah Winfrey, tanda 2 (20 libros nuevos, sin cross-ref
  nuevos esta vez).** Continuación directa de la tanda 1 del mismo día. Selección por
  relevancia/consenso sobre el backlog NUEVO restante del manifiesto de arriba, verificando antes
  vía `Grep`/`Glob` que no hubiera colisión de autor o slug con el catálogo existente (0
  colisiones detectadas para los 20 candidatos elegidos).
  **20 NUEVO enriquecidos con MODO LIBRO** (escritos directamente, sin subagente): `the-reader`
  (feb 1999, Bernhard Schlink, ES Anagrama, asin 8433966669); `daughter-of-fortune` (feb 2000,
  Isabel Allende, ES Debolsillo, asin 8401341507); `the-bluest-eye` (abr 2000, Toni Morrison, ES
  DeBolsillo, asin 8497932668); `house-of-sand-and-fog` (nov 2000, Andre Dubus III, solo inglés,
  asin 0393338118); `a-fine-balance` (nov 2001, Rohinton Mistry, ES Random House Mondadori, asin
  8439701985); `we-were-the-mulvaneys` (ene 2001, Joyce Carol Oates, ES Lumen, asin 8426413439);
  `sula` (abr 2002, Toni Morrison, ES DeBolsillo, asin 8497932641); `love-in-the-time-of-cholera`
  (oct 2007, García Márquez, ES Debolsillo, asin 849759245X); `pillars-of-the-earth` (nov 2007, Ken
  Follett, ES Debolsillo, asin 8499080286); `freedom` (sep 2010, Jonathan Franzen, ES Salamandra,
  asin 8498384788); `the-invention-of-wings` (ene 2014, Sue Monk Kidd, ES Suma de Letras, asin
  1629530743); `the-water-dancer` (sep 2019, Ta-Nehisi Coates, ES Seix Barral, asin 8432239631);
  `olive-again` (nov 2019, Elizabeth Strout, ES Duomo, asin 8417761411); `american-dirt` (ene 2020,
  Jeanine Cummins, ES Vintage Español, asin 8466667423); `caste` (nov 2020, Isabel Wilkerson, ES
  Paidós, asin 8449338301, categoria historia); `gilead` (mar 2021, Marilynne Robinson, ES Galaxia
  Gutenberg, asin 8481099031 — solo el primer libro de la saga de 4; Home/Lila/Jack quedan
  pendientes); `demon-copperhead` (oct 2022, Barbara Kingsolver, ES Batiscafo, asin 8419552623);
  `let-us-descend` (oct 2023, Jesmyn Ward, solo inglés, asin 198210449X); `long-island` (may 2024,
  Colm Tóibín, ES Lumen, asin 8426426654); `a-million-little-pieces` (sep 2005, James Frey, ES
  Literatura Random House, asin 8439738889, categoria memorias — ficha incluye nota sobre la
  polémica real de veracidad de 2006).
  ASIN de las 20 verificado real vía WebSearch (ISBN-10 de edición impresa, ninguno inventado);
  18/20 con edición en español confirmada, 2/20 solo inglés (`house-of-sand-and-fog`,
  `let-us-descend`). 0 CROSS-REF nuevos detectados en esta tanda.
  **Catálogo: +20 fichas nuevas.** Oprah pasa de 19 a **39 libros vinculados/enriquecidos**
  (verificado con `Grep` de `oprah-winfrey` sobre `src/content/libros`: 39 archivos = 5 YA-LINKED +
  7 CROSS-REF + 7 NUEVO tanda 1 + 20 NUEVO tanda 2).
  **Pendiente:** ~80 candidatos NUEVO restantes (119 históricos − 39 vinculados; backlog del
  manifiesto de arriba, sin marcar ✅) + Home/Lila/Jack de Marilynne Robinson (ya contados dentro de
  esos ~80) + revisar el caso `Enough`. Próxima tanda de "Profundizar Oprah" sigue el mismo patrón
  de selección por relevancia/consenso.
  **Listicle:** ver entrada siguiente — se generó por primera vez `libros-que-recomienda-oprah-
  winfrey.md` con los 39 libros disponibles a esta fecha.
  **Verificación `detectar_duplicados.py` (Marcelo, post-tanda 2):** 42 `[REV]` (autores con 2+
  libros) revisados uno por uno — **0 duplicados reales**. Confirman que la tanda no generó
  colisiones: `toni-morrison` queda con 3 libros distintos (song-of-solomon, sula, the-bluest-eye,
  los 3 de esta ronda de Oprah), `barbara-kingsolver` con 2 (demon-copperhead nuevo +
  the-poisonwood-bible), `charles-dickens` con 2 (a-tale-of-two-cities + great-expectations, el
  cross-ref de la tanda 1), `gabriel-garcia-marquez` con 2 (love-in-the-time-of-cholera nuevo +
  one-hundred-years-of-solitude), `jonathan-franzen` con 2 (freedom + the-corrections, ambos
  nuevos de esta tanda) — todos casos `[REV]` legítimos, libros reales y distintos. Dos casos ya
  documentados como precedente deliberado (no acción nueva): Asimov (`foundation` vs
  `the-foundation-trilogy`, edición suelta vs. ómnibus) y Séneca (`letters-from-a-stoic` vs
  `the-moral-letters-to-lucilius`, selección abreviada vs. correspondencia completa) — mismo
  criterio usado con "The Principia" en la tanda de Sam Altman. **Confirmado por Marcelo:**
  verificación cerrada, `[DUP]` también en 0. **Tanda 2 de Oprah queda cerrada y verificada.**

- **2026-07-20 — Acción "Profundizar": Oprah Winfrey, tanda 3 (30 libros: 29 NUEVO + 1 CROSS-REF).**
  Selección por relevancia/consenso sobre el backlog restante del manifiesto (~85 candidatos).
  Trabajo hecho vía **3 subagentes Sonnet en paralelo** (lotes de 10/10/9), cada uno con el
  manifiesto de libros asignado, fecha de pick y notas de casos especiales; verificación de
  colisiones de autor/slug hecha ANTES de despachar (Grep + Glob sobre los 30 candidatos).
  **1 CROSS-REF detectado en el chequeo previo** (no en el reparto de subagentes): `as-i-lay-dying`
  (Faulkner) ya estaba en el catálogo, recomendado por Stephen King — se sumó `oprah-winfrey` a
  `recomendadoPor`, se renombró la sección a "Por qué lo recomiendan Stephen King y Oprah Winfrey"
  y se agregó un párrafo sobre el pick triple de Faulkner de junio 2005 (edité esta a mano, no fue
  parte del despacho a subagentes).
  **29 NUEVO enriquecidos:** `paradise` (Toni Morrison, ES Ediciones B, asin 8440689322);
  `the-sound-and-the-fury` (Faulkner, ES Bruguera, asin 8402082645); `light-in-august` (Faulkner,
  ES DeBolsillo, asin 8490628173); `the-story-of-edgar-sawtelle` (Wroblewski, ES Planeta, asin
  840809534X); `cry-the-beloved-country` (Alan Paton, ES Ediciones Palabra — título real "Llanto
  por la tierra amada", asin 8498409241); `the-heart-is-a-lonely-hunter` (McCullers, ES Seix
  Barral, asin 8432219576); `the-good-earth` (Pearl S. Buck, ES Alianza, asin 8420677434);
  `white-oleander` (Janet Fitch, solo inglés, asin 0316284955); `breath-eyes-memory` (Danticat, ES
  consonni 2024, asin 8419490326); `midwives` (Bohjalian, solo inglés, asin 0375706771);
  `a-lesson-before-dying` (Gaines, solo inglés, asin 0375702709); `home` (Marilynne Robinson, ES
  Galaxia Gutenberg, asin 8481099635 — traductor no confirmado, se omitió); `lila` (Robinson, ES
  Galaxia Gutenberg, asin 8416252297); `jack` (Robinson, ES Galaxia Gutenberg, asin 8418526211 —
  con `home`/`lila` completa la saga de Gilead, 4/4); `the-sweetness-of-water` (Nathan Harris, ES
  AdN, asin 841362696X); `the-twelve-tribes-of-hattie` (Ayana Mathis, ES Salamandra, asin
  8498386217); `hidden-valley-road` (Robert Kolker, ES Sexto Piso, asin 8419261157, categoria
  psicologia); `deacon-king-kong` (James McBride, solo inglés — ojo: el subagente descartó un ISBN
  que en Amazon aparecía bajo "Diácono King Kong" por ser en realidad la edición portuguesa
  brasileña, no española — asin 073521672X, distinto de `the-heaven-and-earth-grocery-store` ya en
  catálogo); `behold-the-dreamers` (Imbolo Mbue, solo inglés — sin traducción a español pese a 11
  idiomas, asin 0525509712); `love-warrior` (Glennon Doyle Melton, ES HarperCollins Español, asin
  0718074106); `say-you-re-one-of-them` (Uwem Akpan, ES El Tercer Nombre, asin 8496693538);
  `the-sun-does-shine` (Anthony Ray Hinton, solo inglés, asin 1250124719, categoria memorias);
  `nightcrawling` (Leila Mottley, ES Plata, asin 8492919418); `finding-me` (Viola Davis, solo
  inglés, asin 0063037327, categoria memorias); `wellness` (Nathan Hill, ES AdN, asin 8410138069);
  `tell-me-everything` (Elizabeth Strout, ES Alfaguara, asin 841029902X, distinto de `olive-again`
  — universo Lucy Barton, no Olive Kitteridge); `bridge-of-sighs` (Richard Russo, ES Alfaguara, asin
  8420474118 — sorpresa: sí tiene edición ES de 2008 pese a ser pick de agosto 2025); `the-river-is-
  waiting` (Wally Lamb, solo inglés, asin 1668006391); `from-here-to-the-great-unknown` (Lisa Marie
  Presley y Riley Keough, solo inglés, asin 0593733878, categoria memorias).
  ASIN de las 29 verificado real vía WebSearch (ISBN-10 de edición impresa, ninguno inventado);
  16/29 con edición en español confirmada, 13/29 solo inglés (varias muy recientes, 2022-2025).
  Spot-check de 4 fichas (`cry-the-beloved-country`, `deacon-king-kong`, `home`, `tell-me-
  everything`): estructura MODO LIBRO correcta, Regla de atribución respetada, sin citas inventadas
  de Oprah, distinciones de libros del mismo autor correctamente señaladas.
  **Catálogo: +29 fichas nuevas, +1 vínculo cross-ref.** Oprah pasa de 39 a **69 libros
  vinculados/enriquecidos**.
  **Pendiente:** ~50 candidatos NUEVO restantes en el manifiesto de arriba + revisar el caso
  `Enough` + los 3 libros infantiles de Bill Cosby (1997, evaluar si corresponde). Nota para
  próxima tanda: el hallazgo de edición ES para *Bridge of Sighs* (pick reciente) sugiere revisar
  si algún otro pick marcado "solo inglés" en tandas viejas en realidad sí tiene edición en
  español no detectada en su momento — no urgente, pero vale una pasada futura.
  **Verificación `detectar_duplicados.py` (Marcelo, post-tanda 3): `[DUP]` en 0, 46 `[REV]`
  revisados — 0 duplicados reales.** Los `[REV]` nuevos que sumó esta tanda son exactamente los
  esperados: `william-faulkner` con 3 (as-i-lay-dying, light-in-august, the-sound-and-the-fury —
  el pick triple), `marilynne-robinson` con 4 (gilead, home, jack, lila — la saga completa),
  `toni-morrison` con 4 (paradise se suma a song-of-solomon, sula, the-bluest-eye),
  `james-mcbride` con 2 (deacon-king-kong vs. the-heaven-and-earth-grocery-store, ya
  documentado), `elizabeth-strout` con 2 (olive-again vs. tell-me-everything, ya documentado).
  **Tanda 3 de Oprah queda cerrada y verificada.**

- **2026-07-20 — Discovery + Profundizar (completo en una sola tanda): Yuval Noah Harari.**
  Backlog previo: 3/3 libros ya enriquecidos (Armas, gérmenes y acero; Un mundo feliz; Historia y
  cronología del mundo), pero nunca se había fetcheado una fuente real y completa de sus lecturas
  — la ficha del referente solo decía "rastrearse a través de ynharari.com (Reading List)" sin URL
  concreta. El fetch directo a `ynharari.com/reading-list/` devolvió una página vacía (JS-rendered,
  mismo patrón que otros sitios de autor); `WebSearch` encontró la fuente real y mejor documentada:
  **ynharari.com/apple-books-collection** ("A Haphazard Guided Tour of Humanity on the Brink",
  colección curada por el propio Harari para Apple Books, con **cita textual real de Harari por
  cada libro** — la fuente con mejor calidad de atribución usada hasta ahora en el sitio).
  Manifiesto de 12 libros → reconciliación manual (Grep/Glob, sin `reconciliar.py` por ser lote
  chico): **2 YA-LINKED** (`brave-new-world`, `guns-germs-and-steel`, ya en catálogo con
  `yuval-noah-harari` en `recomendadoPor`) + **1 CROSS-REF** (`thinking-fast-and-slow`, ya en
  catálogo vía Kahneman/James Clear/Sam Altman) + **9 NUEVO**.
  **1 CROSS-REF aplicado**: `thinking-fast-and-slow` suma `yuval-noah-harari` a `recomendadoPor`;
  al no tener sección "Por qué lo recomienda X" propia (Kahneman es el autor, mismo caso especial
  documentado el 2026-07-18), la mención de Harari se fusionó al párrafo introductorio, con su
  cita real traducida ("uno de los mejores puntos de partida para explorar la maraña de la mente
  humana").
  **9 NUEVO enriquecidos** (escritos directamente, sin subagente, por ser lote chico; cada uno usa
  la cita real de Harari de la fuente, traducida, en la sección de atribución — nunca una cita
  inventada): El mono que llevamos dentro [ES, Booket/Planeta, asin 8490665788] (Frans de Waal,
  ciencia); La sexta extinción [ES, Crítica/Drakontos, asin 849892779X] (Elizabeth Kolbert,
  ciencia, ganadora del Pulitzer); Armas de destrucción matemática [ES, Capitán Swing, asin
  8494740849] (Cathy O'Neil, ciencia); Congo [ES, Taurus, asin 8430619437] (David Van Reybrouck,
  historia); China: la edad de la ambición [ES, Malpaso, asin 8494174967] (Evan Osnos, historia,
  ganador del National Book Award); Black Flags: The Rise of ISIS [solo inglés, Anchor Books, asin
  0804168938] (Joby Warrick, historia, ganador del Pulitzer); Caudillos del crimen [ES, Grijalbo,
  asin 6073143125] (Ioan Grillo, historia); El camino hacia la no libertad [ES, Galaxia Gutenberg,
  asin 8417355529] (Timothy Snyder, historia); En defensa de la Ilustración [ES, Paidós, asin
  8449334624] (Steven Pinker, filosofia).
  ASIN de las 9 verificado real vía WebSearch (ISBN-10 de edición impresa, ninguno inventado); 7/9
  con edición en español confirmada, 2/9 solo inglés (Black Flags no tiene edición ES localizable).
  Spot-check de 2 fichas (`congo`, `enlightenment-now`): estructura MODO LIBRO correcta, citas de
  Harari fieles a la fuente, sin invención.
  **Yuval Noah Harari 3 → 13 libros, backlog 100% cerrado** (los 12 candidatos de la colección de
  Apple Books quedaron todos resueltos: 2 ya estaban, 1 cross-ref, 9 nuevos). Catálogo: +9 fichas.
  **Corrección:** Harari SÍ tenía listicle previo (`libros-que-recomienda-yuval-noah-harari.md`,
  creado 2026-07-10 con los 3 libros originales) — no detectado en la búsqueda inicial de esta
  entrada porque el `Grep` de "Harari" en `PROGRESO.md` no incluye entradas de blog, solo de
  fichas. **Listicle regenerado** (confirmado con el usuario vía pregunta explícita) de 3 a 13
  libros, `fecha` original 2026-07-10 sin cambios, `fechaActualizado` 2026-07-20. Reestructurado en
  3 grupos temáticos parejos: "Big history: de los primates a la civilización" (3), "El mundo que
  se rompe: crisis, poder y desinformación contemporáneos" (5), "Ciencia, mente y el futuro que
  viene" (5), más lead "Por dónde empezar" con 3 destacados. Cada entrada usa una cita real de
  Harari traducida de la fuente (ynharari.com/apple-books-collection), nunca inventada. Verificado:
  13/13 links con `titulo` exacto de la ficha, slug existente, `yuval-noah-harari` presente en
  `recomendadoPor` de las 13.
  **Verificación `detectar_duplicados.py` (Marcelo): `[DUP]` en 0, 46 `[REV]` revisados — 0
  duplicados reales.** Único `[REV]` nuevo de esta tanda: `steven-pinker` pasa de 2 a 3 libros
  (se suma `enlightenment-now` a `the-better-angels-of-our-nature` y
  `when-everyone-knows-that-everyone-knows`), tres obras reales y distintas (2011, 2018 y una
  más reciente). **Tanda de Yuval Noah Harari queda cerrada y verificada.**

- **2026-07-22 — Discovery (solo discovery, a pedido explícito): Adam Grant.** Backlog previo:
  4/4 libros ya enriquecidos (Piensa de nuevo, El código de la cultura, Dar y recibir, Quiet).
  **Corrección de fuente:** la bio del referente decía "rastrearse a través de su newsletter
  *Think Again*" — error, *Think Again* es un libro suyo, no la newsletter; su newsletter real se
  llama **Granted** (adamgrant.substack.com, 500.000+ suscriptores). Pendiente corregir
  `autores/adam-grant.md` cuando se toque la ficha (no se editó en esta tanda, solo discovery).
  Fuente fetcheada: 3 entradas de **Granted** con recomendaciones explícitas (libro + autor +
  link de Amazon por ítem, agrupadas por eje temático): **"The New Books to Fight Brain Rot"**
  (26/8/2025, 8 libros), **"The New Books to Refresh Your Thinking in 2026"** (18/1/2026, 12
  libros) y **"The 12 New Books to Enliven Spring and Summer"** (2/5/2026, 12 libros).
  Manifiesto de 32 candidatos (título | autor | mes de publicación | URL fuente):
  1. How to Be a Living Thing — Mari Andrew (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  2. 1929 — Andrew Ross Sorkin (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  3. Finding My Way — Malala Yousafzai (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  4. Algospeak — Adam Aleksic (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  5. The Genius Myth — Helen Lewis (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  6. Read Your Mind — Oz Pearlman (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  7. Anointed — Toby Stuart (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  8. Playful — Cas Holman (2025) — adamgrant.substack.com/p/the-new-books-to-fight-brain-rot
  9. Poisonous People — Leanne ten Brinke (marzo 2026) — adamgrant.substack.com/p/the-new-books-to-refresh-your-thinking
  10. The Balancing Act — Nedra Tawwab (febrero 2026) — ídem
  11. Flourish — Dan Coyle (febrero 2026) — ídem
  12. Mattering — Jennifer Wallace (enero 2026) — ídem
  13. The Story of Stories — Kevin Ashton (marzo 2026) — ídem
  14. Revealing — Leslie John (febrero 2026) — ídem
  15. Your Best Meeting Ever — Rebecca Hinds (febrero 2026) — ídem
  16. Jolted — Anthony Klotz (marzo 2026) — ídem
  17. The Other Side of Change — Maya Shankar (enero 2026) — ídem
  18. Politics Without Politicians — Hélène Landemore (febrero 2026) — ídem
  19. We the Women — Norah O'Donnell (febrero 2026) — ídem
  20. The Triangle of Power — Alexander Stubb (enero 2026) — ídem
  21. Human Raised — Dana Suskind (julio 2026) — adamgrant.substack.com/p/the-12-new-books-to-enliven-spring
  22. Incorruptible — Eric Ries (mayo 2026) — ídem
  23. Leave the Lights On — Elizabeth Dunn y Jiaying Zhao (junio 2026) — ídem
  24. Inside the Box — David Epstein (mayo 2026) — ídem
  25. The Power of Beliefs — Shawn Achor (mayo 2026) — ídem
  26. Why We Talk Funny — Valerie Fridland (abril 2026) — ídem
  27. How to Not Know — Simone Stolzoff (mayo 2026) — ídem
  28. Joyful Anyway — Kate Bowler (abril 2026) — ídem
  29. Anxietyland — Gemma Correll (abril 2026) — ídem
  30. You've Been Pooping All Wrong — Trisha Pasricha (abril 2026) — ídem
  31. The Plunge — Chris Ballard (junio 2026) — ídem
  32. Walk — Courtney Conley y Milica McDowell (mayo 2026) — ídem

  **Reconciliación manual (Grep sobre `titulo:` en `src/content/libros`, sin correr
  `reconciliar.py` — pendiente correrlo en Windows para veredicto definitivo): 1 CROSS-REF
  detectado** — `1929.md` ya existe en el catálogo (asin `0593296966`, idéntico al `/dp/` del
  link de Amazon del post de Grant), recomendado hoy solo por `barack-obama` → sumar
  `adam-grant` a su `recomendadoPor` cuando se toque. Los otros 31 títulos no matchean ningún
  slug existente en un chequeo manual (no exhaustivo, reemplaza correr el script real).
  **No se tocó el catálogo** (0 fichas creadas/editadas, 0 listicle regenerado) — por indicación
  explícita del usuario de correr *solo* el discovery.
  **Ojo con las ediciones:** el manifiesto entero son novedades de abril 2025 a julio 2026 (nada
  de backlog histórico), así que es esperable que la mayoría **no tenga edición en español
  todavía** — al enriquecer, confirmar edición ES real antes de cargar y dejar en "solo
  inglés/a decidir" lo que no la tenga (mismo caso que backlogs recientes de Nadella/Zuckerberg).
  **Pendiente:** correr `reconciliar.py adam-grant <manifiesto> src/content/libros` en Windows
  para confirmar YA-LINKED/CROSS-REF/REVISAR/NUEVO con certeza; decidir con el usuario cuántos y
  cuáles priorizar (32 es un lote grande para un referente que hoy solo tiene 4 libros); corregir
  la fuente citada en `autores/adam-grant.md` (newsletter Granted, no "Think Again").

- **2026-07-22 — Reconciliación + tanda 1: Adam Grant.** Marcelo corrió
  `python tools/reconciliar.py adam-grant tools/manifiesto_adam_grant.txt src/content/libros`
  en Windows (el manifiesto quedó versionado en `tools/manifiesto_adam_grant.txt`, no en /tmp).
  Resultado sobre los 32 candidatos: **0 YA-LINKED, 1 CROSS-REF, 1 REVISAR, 30 NUEVO.**
  **CROSS-REF aplicado:** `1929` (Andrew Ross Sorkin) ya estaba en el catálogo vía Barack Obama
  (mismo ASIN `0593296966` que el link de Amazon del post de Grant) → se sumó `adam-grant` a su
  `recomendadoPor`, la sección de atribución se renombró a "Por qué lo recomiendan Barack Obama y
  Adam Grant" y se tejió una cita real de Grant desde Granted ("el análisis definitivo del mayor
  crac bursátil del siglo, del mejor periodista de negocios de nuestra época"). Sin listicle que
  regenerar (Grant todavía no tiene uno; el de Obama no cambió de contenido, solo se sumó un
  referente más al libro).
  **REVISAR resuelto a NUEVO:** `Inside the Box` (David Epstein) matcheaba por autor con `range`
  (ya en catálogo), pero son libros reales y distintos del mismo autor — *Range* (2019, sobre
  generalistas) vs. *Inside the Box* (2026, sobre límites que desbloquean creatividad) — no es
  cross-ref, es ficha nueva. Queda contado dentro de los 30 NUEVO restantes.
  **Pre-chequeo de edición ES** (subagente Haiku, 1-2 búsquedas por título, sin inventar ASIN):
  de los 30 NUEVO, **29 son "solo inglés todavía"** (son lanzamientos de abril 2025 a julio 2026,
  varios ni siquiera publicados en inglés a la fecha de este chequeo — esperable que tarden en
  tener traducción) + **1 con edición ES confirmada: `Poisonous People`** → *Personas venenosas:
  Cómo detectarlas para protegernos*, Grijalbo, ISBN-10 `8425373948` (verificado en amazon.com,
  coincide con el ISBN-13 9788425373947 de Fnac/Penguin Random House/librerías españolas).
  **1 ficha nueva enriquecida** (MODO LIBRO completo, cita real de Grant desde Granted en la
  sección de atribución, categoria `psicologia`): `poisonous-people.md`.
  **Adam Grant: 4 → 6 libros** (1929 vía cross-ref + Personas venenosas nueva). **Backlog
  restante: 29 candidatos "esperar edición ES"** (incluye `inside-the-box`, `finding-my-way`,
  `algospeak`, y el resto del manifiesto en `tools/manifiesto_adam_grant.txt`) — revisar en una
  futura pasada cuando salgan más traducciones (probable ventana: 6-18 meses post-lanzamiento en
  inglés, según patrón histórico del catálogo). Sin listicle de Adam Grant todavía (recién a 6
  libros; se escribe cuando el referente tenga un cuerpo de fichas más sólido). **Pendiente:**
  corregir la bio de `autores/adam-grant.md` (dice "newsletter Think Again", debería decir
  "newsletter Granted").

- **2026-07-22 — Discovery: Andrew Ng.** Backlog previo: 3/3 libros ya enriquecidos (Zero to
  One, Life 3.0, Artificial Intelligence: A Modern Approach). Fuente fetcheada: **fs.blog/
  short-list-books-new-things** (Farnam Street, 31/10/2016), artículo curado con **cita textual
  real de Ng por libro** (originada en una entrevista a Huffington Post India) — misma calidad
  de fuente que la usada con Harari, no un agregador secundario. Manifiesto de 7 libros: Zero to
  One (Peter Thiel), Crossing the Chasm (Geoffrey A. Moore), The Lean Startup (Eric Ries),
  Talking to Humans (Giff Constable), Rocket Surgery Made Easy (Steve Krug), The Hard Thing
  About Hard Things (Ben Horowitz), So Good They Can't Ignore You (Cal Newport).
  **Reconciliación manual** (Grep/Glob por slug y por `autorLibro`, lote chico, sin
  `reconciliar.py`): **1 YA-LINKED** (`zero-to-one`, ya en `recomendadoPor` de `andrew-ng`) +
  **1 CROSS-REF** (`the-hard-thing-about-hard-things`, ya en catálogo vía Marc Andreessen) +
  **5 NUEVO**: Crossing the Chasm, The Lean Startup, Talking to Humans, Rocket Surgery Made
  Easy, So Good They Can't Ignore You.
  **1 CROSS-REF aplicado:** se sumó `andrew-ng` a `recomendadoPor` de
  `the-hard-thing-about-hard-things`; la sección de atribución se renombró a "Por qué lo
  recomiendan Marc Andreessen y Andrew Ng" y se tejió la cita real de Ng ("es un poco oscuro,
  pero cubre un montón de territorio útil sobre cómo es realmente construir una organización").
  Sin listicle que regenerar (ni Andreessen ni Ng tienen uno publicado con este libro afectado).
  **No se enriquecieron los 5 NUEVO todavía** — a diferencia del backlog de Adam Grant, estos
  son bestsellers de negocios de hace más de una década (2009-2014), altísima probabilidad de
  tener edición en español desde hace años, así que no requieren el mismo pre-chequeo; quedan
  listos para una tanda de enriquecimiento directa. **Andrew Ng: 3 → 4 libros** (solo el
  cross-ref aplicado por ahora). Sin listicle todavía.

- **2026-07-22 — Tanda de enriquecimiento: los 5 NUEVO de Andrew Ng.** ASIN de edición en
  español verificado real vía WebSearch para 4/5 (ninguno inventado); 1/5 solo inglés (libro
  autoeditado sin traducción):
  `crossing-the-chasm` (Geoffrey A. Moore, ES Paidós, trad. Albert Cuesta Zaragosi, asin
  8498753554, categoria negocios); `the-lean-startup` (Eric Ries, ES Deusto, trad. Javier San
  Julián, asin 842340949X, categoria negocios); `talking-to-humans` (Giff Constable, solo
  inglés — autoeditado, sin edición ES localizable, asin 099080092X, categoria negocios);
  `rocket-surgery-made-easy` (Steve Krug, ES *Haz fácil lo imposible*, Anaya Multimedia, asin
  8441527547, categoria negocios); `so-good-they-can-t-ignore-you` (Cal Newport, ES *Hazlo tan
  bien que no puedan ignorarte*, Asertos, trad. Diego Pereda Sancho, asin 8494463136, categoria
  **psicologia** — encaja mejor ahí que en negocios, es sobre mindset de carrera/maestría, no
  metodología de empresa).
  Las 5 fichas usan la cita real de Andrew Ng desde fs.blog (traducida) en la sección de
  atribución, ninguna cita inventada. **Andrew Ng: 4 → 9 libros.** Backlog de discovery cerrado
  al 100% (7/7 candidatos del manifiesto de fs.blog resueltos: 1 YA-LINKED + 1 CROSS-REF + 5
  NUEVO, todos aplicados/enriquecidos).

- **2026-07-22 — Listicle nuevo: Andrew Ng.** `libros-que-recomienda-andrew-ng.md`, primera
  vez (no existía antes). 9/9 libros enriquecidos, agrupados en 3 grupos temáticos parejos:
  "Construir y escalar una empresa" (4: Cruzando el abismo, De cero a uno, Emprender y liderar
  una startup, El método Lean Startup), "Escuchar bien: a tus usuarios y a tu propia carrera"
  (3: Talking to Humans, Haz fácil lo imposible, Hazlo tan bien que no puedan ignorarte — une
  investigación de usuarios y psicología de carrera bajo el mismo eje de "escuchar antes de
  actuar") y "Los fundamentos técnicos de la inteligencia artificial" (2: Inteligencia
  artificial: un enfoque moderno, Vida 3.0 — grupo chico pero temáticamente distinto,
  deliberadamente no fusionado con los de negocios). Verificado: 9/9 links con `titulo` exacto
  de la ficha, slug existente, `andrew-ng` presente en `recomendadoPor` de las 9, sin
  duplicados. Cierra con enlaces a `/referentes` y `/categorias/negocios`.

- **2026-07-22 — Discovery: Vitalik Buterin.** Backlog previo: 4/4 libros ya enriquecidos (The
  Sovereign Individual, The Network State, Stubborn Attachments, Radical Markets). A diferencia
  de Adam Grant/Andrew Ng, Vitalik no tiene una fuente única curada (su bio cita "su blog en
  vitalik.ca", pero no existe ahí una lista de lecturas) — sus recomendaciones están dispersas en
  tweets sueltos y entrevistas. Se descartó incluir candidatos sin URL verificable por libro (The
  Origins of Totalitarianism de Hannah Arendt, Thinking in Bets de Annie Duke): aparecían en
  agregadores pero sin fuente primaria localizable, así que quedan afuera por regla de oro
  ("si no podés sourcear un libro, no lo incluyas") — no descartados para siempre, solo no
  incluidos hoy por falta de URL confiable.
  **Fuentes fetcheadas con cita + URL propia por libro:** books-guru.com/experts/vitalik-buterin
  (agregador que linkea el tweet original de Vitalik por cada recomendación, mismo estándar que
  Nadella/Zuckerberg) + nfx.com/post/vitalik-buterin-the-a-sides (transcripción real de una
  entrevista de Morgan Beller a Vitalik, feb/2021, con cita textual completa).
  Manifiesto de 6 candidatos: The Sovereign Individual (Davidson & Rees-Mogg), The Network State
  (Balaji Srinivasan), The Elephant in the Brain (Kevin Simler y Robin Hanson), The Scout Mindset
  (Julia Galef), The Precipice (Toby Ord), The Revolt of the Public (Martin Gurri).
  **Reconciliación manual** (Grep/Glob, lote chico): **2 YA-LINKED** (`the-sovereign-individual`
  y `the-network-state`, ambos ya con `vitalik-buterin` en `recomendadoPor`) + **4 NUEVO**: The
  Elephant in the Brain, The Scout Mindset, The Precipice, The Revolt of the Public. Sin
  cross-ref (ninguno de los 4 existía antes bajo otro referente). **No se enriquecieron
  todavía** — a confirmar con el usuario. **Vitalik Buterin: sigue en 4/4** (sin cambios en el
  catálogo hasta que se decida enriquecer los 4 NUEVO).

- **2026-07-22 — Tanda de enriquecimiento: los 4 NUEVO de Vitalik Buterin.** ASIN verificado
  real vía WebSearch para las 4 (ninguno inventado); 2/4 solo inglés:
  `the-elephant-in-the-brain` (Kevin Simler y Robin Hanson, solo inglés — se encontró un ASIN en
  Amazon con formato "[Tapa dura] [Kevin Simler]" que parece una edición no oficial/POD sin
  editorial identificable, así que se descartó y se usó la edición inglesa real de Oxford
  University Press, asin 0190495995, categoria psicologia); `the-scout-mindset` (Julia Galef, ES
  *La mentalidad del explorador*, Paidós/colección Contextos, trad. Fernando Borrajo, asin
  8449340284, categoria psicologia); `the-precipice` (Toby Ord, solo inglés — **ojo, falso
  positivo detectado**: un listado de Amazon.com.mx mostraba el título traducido "El Precipicio"
  pero al verificar el ISBN resultó ser el mismo libro en inglés con el título solo traducido
  para el storefront, no una edición real en español; asin 1526600234, categoria filosofia);
  `the-revolt-of-the-public` (Martin Gurri, ES *La rebelión del público*, Adriana Hidalgo/
  colección Interferencias, trad. Santiago Armando, asin 8419208604, categoria historia).
  Las 4 fichas usan la cita real de Vitalik (de books-guru.com o la entrevista NFX) en la
  sección de atribución, ninguna inventada. **Vitalik Buterin: 4 → 8 libros.** Backlog de
  discovery cerrado al 100%.

- **2026-07-22 — Listicle nuevo: Vitalik Buterin.** `libros-que-recomienda-vitalik-buterin.md`,
  primera vez (no existía antes). 8/8 libros enriquecidos, agrupados en 3 grupos temáticos:
  "Repensar las instituciones: dinero, Estados y por qué tambalean" (4: El individuo soberano,
  The Network State, Mercados radicales, La rebelión del público), "El largo plazo: crecimiento
  y riesgo existencial" (2: Stubborn Attachments, The Precipice) y "Cómo pensamos y por qué nos
  mentimos" (2: The Elephant in the Brain, La mentalidad del explorador). Intro aclara que
  Buterin no tiene fuente única curada, a diferencia de otros referentes del sitio. Verificado:
  8/8 links con `titulo` exacto de la ficha, slug existente, `vitalik-buterin` presente en
  `recomendadoPor` de las 8, sin duplicados (incluye `the-network-state`, que tiene `asin`
  vacío por regla §3.4 pero cuenta como enriquecida por tener cuerpo completo). Cierra con
  enlaces a `/referentes` y `/categorias/negocios`.
