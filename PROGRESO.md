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
**+ Isabel Allende** (#41, 2026-07-31: 6/6) **+ Mario Vargas Llosa** (#42, 2026-07-31: 46/46)
**+ Jenna Bush Hager** (#43, 2026-08-01: 31/31 fichas + listicle; backlog histórico 2019-2023
pendiente de sourcear).

- **2026-08-06** — Profundizar Ryan Holiday: manifiesto de 38 candidatos reconciliado
  (3 YA-LINKED, 8 CROSS-REF, 4 REVISAR, 23 NUEVO). Los 4 REVISAR (Leadership in Turbulent Times,
  Tiny Beautiful Things, The Second Mountain, Titan) se resolvieron como libros nuevos —mismo
  autor que otra ficha del catálogo, pero obra distinta— → total NUEVO = 27, todos enriquecidos
  en 4 lotes paralelos (subagentes Sonnet): *La psicología del dinero*, *A Calendar of Wisdom*,
  *El hombre invisible*, *Sigue adelante*, *La biblioteca en llamas*, *Autobiografía* (Malcolm X),
  *Esencialismo*, *Maestría*, *Cómo vivir*, *Las 33 estrategias de la guerra*, *Memorias de
  Adriano*, *Ansiedad por el estatus*, *El juego de Ender*, *The Rise of Theodore Roosevelt*,
  *Las 48 leyes del poder*, *Saliendo de la esclavitud*, *Bird by Bird*, *The Moral Animal*,
  *Ejercicios espirituales y filosofía antigua*, *The Power Broker*, *La estrategia del océano
  azul*, *El libro de los cinco anillos*, *Essays and Aphorisms*, *Liderazgo: en tiempos
  turbulentos*, *Pequeñas cosas bellas*, *La segunda montaña*, *Titan*.
  ⚠️ Dudas a revisar: `a-calendar-of-wisdom` quedó en inglés (ediciones ES encontradas parecen
  autopublicadas/con errores, confianza <80%); `the-autobiography-of-malcolm-x` ASIN confirmado
  solo vía listado amazon.com/-/es (~75% confianza); `philosophy-as-a-way-of-life` identificación
  de edición ES con ~85% confianza (hay otro libro de Hadot con título similar en español que NO
  es este). Sin edición ES confirmada (quedaron en inglés): `essays-and-aphorisms`,
  `the-rise-of-theodore-roosevelt`, `bird-by-bird`, `the-moral-animal`, `the-power-broker`,
  `titan`. Ryan Holiday → **34/34 fichas ajenas enriquecidas** (+ 4 propias ya existentes,
  excluidas del listicle a propósito). Listicle regenerado (ver abajo).
- **2026-08-07** — Profundizar Marc Andreessen: manifiesto de 30 candidatos reconciliado
  (2 YA-LINKED, 9 CROSS-REF, 2 REVISAR, 18 NUEVO). Los 2 REVISAR (Homage to Catalonia vs.
  1984/Animal Farm; A Spy Among Friends vs. the-spy-and-the-traitor, ambos de Ben Macintyre pero
  sobre personas distintas —Philby vs. Gordievsky—) se resolvieron como libros nuevos → total
  NUEVO = 20, enriquecidos en 3 lotes paralelos (subagentes Sonnet): Cuando las profecías fallan,
  Life the Movie, El verdadero creyente, Homenaje a Cataluña, The WEIRDest People in the World,
  No me puedes lastimar, Compórtate, Un espía entre amigos, The Rise of Superman, El triunfo de
  las ciudades, El arte de la buena vida, Whole Earth Discipline, The Myth of the Rational Voter,
  El juicio político de los expertos, El fin de la historia y el último hombre, Sólo los
  paranoides sobreviven, Extreme Ownership, Born Standing Up, El libro de Steve Jobs, The Power
  of Productivity.
  ⚠️ Dudas a revisar: editoriales de edición ES con confianza <80% (verificar antes de publicar):
  `when-prophecy-fails` (sello "Rediciones Anómalas", ~65%), `the-true-believer` (Tecnos, ~75%),
  `can-t-hurt-me` (Lioncrest, ~70%), `behave` (Capitán Swing, ~75%). Sin edición ES confirmada
  (quedaron en inglés): `life-the-movie`, `the-weirdest-people-in-the-world`, `the-rise-of-superman`,
  `whole-earth-discipline`, `the-myth-of-the-rational-voter`, `extreme-ownership`,
  `born-standing-up`, `the-power-of-productivity`. Marc Andreessen → **29/29 fichas ajenas
  enriquecidas** (+ 3 propias/preexistentes: Emprender y liderar una startup, High Output
  Management, Revoluciones tecnológicas y capital financiero). Listicle nuevo (ver abajo).

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
- **2026-08-06** — 8 cross-refs de Ryan Holiday: The Road, Range, Endurance, The Great Gatsby,
  The Score Takes Care of Itself, Man's Search for Meaning, The Black Swan, The 4-Hour Workweek
  (esta última tenía un defecto de atribución huérfana — sin sección "Por qué lo recomienda" y
  una línea suelta antes del blockquote de edición— corregido de paso al sumar el cross-ref).
- **2026-08-07** — 9 cross-refs de Marc Andreessen: The Righteous Mind, The Courage to Be
  Disliked, Skin in the Game, Thinking in Bets, Zero to One, Thinking Fast and Slow, The Lean
  Startup, The Rational Optimist, Poor Charlie's Almanack (esta última solo cierre, tope de 2
  desarrollados ya alcanzado con Buffett/Naval). `thinking-fast-and-slow.md` tenía la atribución
  mezclada dentro del párrafo de intro, sin sección propia — corregido de paso: se separó en una
  sección `## Por qué lo recomiendan James Clear y Sam Altman` que también suma a Andreessen.

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

- **2026-08-06** — Listicle de Ryan Holiday **regenerado** (pasó de 4 a 34 libros ajenos
  enlazados; excluye a propósito sus propios libros). Reorganizado en 5 grupos temáticos
  balanceados (Clásicos estoicos y filosofía, Disciplina/creatividad/carácter, Estrategia/poder/
  negocios, Biografías/historia/memorias, Ficción y mirada científica) + bloque "Por dónde
  empezar". `fecha` original (2026-07-10) preservada, `fechaActualizado` a 2026-08-06.
- **2026-08-07** — Listicle de Marc Andreessen **nuevo** (32 libros enlazados). Organizado en 6
  grupos temáticos balanceados (Construir y liderar empresas, Economía/mercados/incertidumbre,
  Cómo pensamos y decidimos, Psicología de las creencias y la política, Ciencia/evolución/
  progreso, Biografías/memorias/historia real) + bloque "Por dónde empezar".

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

- **2026-07-22 — Discovery: Peter Thiel.** Backlog previo: 3/3 (Zero to One, El individuo
  soberano, Things Hidden Since the Foundation of the World). Fuente fetcheada:
  **fs.blog/peter-thiel-favorite-reads** (Farnam Street, nov/2014), que compila 2 fuentes
  primarias con cita real de Thiel: 3 libros de una respuesta al Wall Street Journal (2012,
  "libros que más disfrutó ese año") + 4 libros de una Reddit AMA ("me gusta el género de libros
  del pasado escritos sobre el futuro"). Manifiesto de 8: 100 Plus (Sonia Arrison), Bloodlands
  (Timothy Snyder), Resurrection From the Underground (René Girard — sobre Dostoievski, obra
  real y distinta de *Things Hidden*, mismo autor ya en catálogo), Psychopolitics (Jean-Michel
  Oughourlian, sugerido por Thiel en la misma respuesta), New Atlantis (Francis Bacon, 1627),
  The American Challenge (Jean-Jacques Servan-Schreiber), The Great Illusion (Norman Angell),
  The Diamond Age (Neal Stephenson). **Reconciliación manual (Glob, lote chico): 0 YA-LINKED, 0
  CROSS-REF, 8 NUEVO** — ninguno matcheaba el catálogo. **No enriquecido todavía.** Peter Thiel
  quedaría en 3 → 11 libros si se hace la tanda completa.

- **2026-07-22 — Discovery: Angela Duckworth.** Backlog previo: 3/3 (Grit, Flow, Mindset).
  Fuente fetcheada: la sección "Recommended Reading" del propio libro *Grit* (págs. 283-284),
  vía la lista de Goodreads que la reproduce completa (**goodreads.com/list/show/105205**,
  "A list of all of the books from the recommended reading section of Grit, found on page 283
  and 284") — es, literalmente, la bibliografía de su propio libro, la fuente más primaria
  posible. Manifiesto de 19: Peak (Ericsson), Mindset (Dweck), Make It Stick (Brown), Why We Do
  What We Do (Deci), Learned Optimism (Seligman), How Children Succeed (Tough), The Path to
  Purpose (Damon), Thanks! (Emmons), The Myth of Achievement Tests (Heckman, ed.), Wired to
  Create (Kaufman), The Rise (Lewis), Head Strong (Matthews), Divine Fury (McMahon), The
  Marshmallow Test (Mischel), Rethinking Positive Thinking (Oettingen), The Power of Interest
  for Motivation and Engagement (Renninger), Age of Opportunity (Steinberg), Superforecasting
  (Tetlock), Why Don't Students Like School? (Willingham).
  **Reconciliación manual (Glob + Grep de títulos, sin `reconciliar.py` por ser de origen
  distinto a un slug estándar): 1 YA-LINKED** (Mindset, ya en `recomendadoPor` de
  `angela-duckworth`) **+ 0 CROSS-REF + 18 NUEVO** — ninguno de los 18 matcheaba el catálogo
  (verificado también que Superforecasting y otros títulos populares no estuvieran ya cargados
  bajo otro referente). **No enriquecido todavía.** Es, por lejos, el backlog más grande de los
  tres — Angela Duckworth quedaría en 3 → 21 libros si se hace la tanda completa.

- **2026-07-22 — Discovery: Daniel Kahneman.** Backlog previo: 3/3 (Pensar rápido, pensar
  despacio, Nudge, El desafío de Kahneman/The Undoing Project). Kahneman falleció en marzo de
  2024, así que no hay ni habrá una fuente nueva — se trabajó con lo documentado hasta esa
  fecha. Fuente principal: **goodbooks.io/people/daniel-kahneman**, agregador editorial
  (metodología propia: validan cada sugerencia contra entrevistas o contacto directo) que lista
  5 libros; más una fuente independiente confirmada por separado: el elogio de tapa real de
  Kahneman para *Homo Deus* de Harari ("Homo Deus te va a shockear. Te va a entretener. Sobre
  todo, te va a hacer pensar de maneras en las que no habías pensado antes"), verificado que es
  el blurb real impreso en ediciones del libro. Manifiesto de 6: Skin in the Game (Taleb),
  Loonshots (Safi Bahcall), Scarcity (Mullainathan y Shafir), Simpler (Cass Sunstein), Clinical
  Versus Statistical Prediction (Paul Meehl, 1954 — monografía académica, no un libro de
  divulgación; queda para decidir si se carga o se descarta por no encajar con el tono del
  sitio), Homo Deus (Harari).
  **Reconciliación manual (Glob): 2 CROSS-REF + 4 NUEVO.** **2 CROSS-REF aplicados de
  inmediato** (son triviales, sin ambigüedad): `homo-deus` sumó a `daniel-kahneman` con su cita
  real de tapa tejida en la sección de atribución (ahora "Por qué lo recomiendan Richard Branson
  y Daniel Kahneman"); `skin-in-the-game` sumó a `daniel-kahneman` en el cierre de la sección de
  Naval Ravikant (sin cita propia disponible, solo la mención en el agregador). **4 NUEVO sin
  enriquecer todavía**: Loonshots, Scarcity, Simpler, Clinical Versus Statistical Prediction.
  Daniel Kahneman: 3 → 5 libros aplicados (cross-refs), quedaría en 9 si se completa la tanda de
  NUEVO.

  **Resumen de los tres discoveries:** 30 candidatos NUEVO en total (8 Thiel + 18 Duckworth + 4
  Kahneman) más los 2 cross-ref de Kahneman ya aplicados. Ninguno enriquecido todavía — a
  definir con el usuario cómo tandear antes de escribir las fichas y los 4 listicles
  (Thiel/Duckworth/Kahneman/James Clear) pendientes de la sesión.

- **2026-07-22/23 — Enriquecimiento: Peter Thiel + Angela Duckworth + Daniel Kahneman, las 30
  fichas NUEVO completas en una sola tanda (decisión del usuario: "Todo ahora, los 3 completos"),
  vía 4 subagentes Sonnet en paralelo.
  **Peter Thiel (8/8):** 100 Plus [solo inglés, Basic Books, asin 0465063764] (Sonia Arrison);
  Tierras de sangre [ES, Galaxia Gutenberg, asin 848109949X] (Timothy Snyder); Resurrection From
  the Underground [solo inglés, Michigan State UP, asin 1611860377] (René Girard — aclarado en
  el cuerpo que es obra distinta de *Things Hidden Since the Foundation of the World*, ya en
  catálogo del mismo autor); Psychopolitics [solo inglés, Michigan State UP, asin 1611860539]
  (Jean-Michel Oughourlian, colaborador de Girard); Nueva Atlántida [ES, Akal, asin 8446016532]
  (Francis Bacon, 1627 — se descartaron ediciones ES self-published/POD de dudosa procedencia);
  El desafío americano [ES, Plaza & Janés, asin 8422601028] (Jean-Jacques Servan-Schreiber); The
  Great Illusion [solo inglés, Cosimo Classics, asin 1602069387] (Norman Angell — se descartó una
  "edición ES" con ISBN falso en Amazon); La era del diamante [ES, B de Bolsillo, asin
  8498723647] (Neal Stephenson). Todas las citas de atribución usan las palabras reales de Thiel
  de la respuesta al WSJ 2012 y su Reddit AMA (vía fs.blog), sin inventar razones donde no había
  cita textual (The Great Illusion, The Diamond Age). **Peter Thiel: 3 → 11 libros.**
  **Angela Duckworth (18/18, vía 2 subagentes en paralelo):** Número uno / Peak [ES, Conecta,
  asin 8416029814] (Ericsson); Make It Stick [solo inglés, Belknap Press, asin 0674729013]
  (Brown); Why We Do What We Do [solo inglés, Penguin, asin 0140255265] (Deci); Aprenda
  optimismo [ES, Debolsillo, asin 8499087973] (Seligman); Cómo hacer que los niños triunfen [ES,
  Vergara, asin 6074805784] (Tough); The Path to Purpose [solo inglés, Free Press, asin
  1416537236] (Damon); ¡Gracias! [ES, Ediciones B, asin 8466638415] (Emmons); Wired to Create
  [solo inglés, TarcherPerigee, asin 0399174109] (Kaufman); The Rise [solo inglés, Simon &
  Schuster, asin 1451629249] (Lewis); Head Strong [solo inglés, Oxford UP, asin 0199916179]
  (Matthews); Divine Fury [solo inglés, Basic Books, asin 0465003257, categoria historia en vez
  de psicologia] (McMahon); El test de la golosina [ES, Debate, asin 8499925049] (Mischel);
  Rethinking Positive Thinking [solo inglés, Current, asin 1617230235] (Oettingen); The Power of
  Interest for Motivation and Engagement [solo inglés, Routledge, asin 1138779792] (Renninger);
  Age of Opportunity [solo inglés, HMH, asin 0544279778] (Steinberg); Superpronosticadores [ES,
  Katz Editores, asin 8415917279] (Tetlock); ¿Por qué a los estudiantes no les gusta la escuela?
  [ES, Aptus, asin Kindle B09SLYNX9T] (Willingham); The Myth of Achievement Tests [solo inglés,
  University of Chicago Press, asin 022632480X] (Heckman, ed.). Fuente de atribución para las 18:
  la sección "Recommended Reading" del propio libro *Grit* (págs. 283-284, vía la lista de
  Goodreads que la reproduce), sin citas textuales inventadas de Duckworth — cada ficha explica
  la conexión temática real con su investigación. **Angela Duckworth: 3 → 21 libros.**
  **Daniel Kahneman (4/4):** Loonshots [solo inglés, St. Martin's, asin 1250185963, categoria
  negocios] (Safi Bahcall); Escasez [ES, FCE, asin 607163170X, categoria psicologia]
  (Mullainathan y Shafir); (más) Simple: El futuro del Gobierno [ES, Marcial Pons, asin
  8416212422, categoria negocios] (Cass Sunstein); Clinical Versus Statistical Prediction [solo
  inglés, monografía académica de 1954, asin 1568218311, categoria psicologia] (Paul Meehl —
  se decidió incluirla, con formato de intro breve, por ser una influencia seminal real y
  documentada de Kahneman, no un libro de nicho sin conexión). Para Loonshots/Scarcity/Simpler no
  había cita textual de Kahneman (fuente: agregador goodbooks.io) → atribución por conexión
  temática, sin inventar quotes. **Daniel Kahneman: 5 → 9 libros** (sobre los 2 cross-ref ya
  aplicados el mismo día).
  Verificación (Opus): spot-check de 3 fichas (Clinical Versus Statistical Prediction,
  Resurrection From the Underground, The Myth of Achievement Tests) sin errores — ASIN de 10
  caracteres, sin citas inventadas, atribución correcta, buena disambiguación de obras del mismo
  autor. Confirmada la existencia física de las 30 fichas vía Glob. **0 ASIN inventados, todos
  verificados por WebSearch contra listados reales.** Catálogo: 194 → 224 libros (sumando las 30
  fichas + los 2 cross-ref previos que ya estaban contados). **Pendiente: correr
  `detectar_duplicados.py`** (recomendado para Marcelo, no se corrió desde el sandbox) y escribir
  los 4 listicles (Thiel, Duckworth, Kahneman, James Clear).

- **2026-07-23 — Los 4 listicles pendientes, escritos en paralelo (4 subagentes Sonnet).**
  **Peter Thiel** (`libros-que-recomienda-peter-thiel.md`, nuevo): 11 libros en 4 grupos —
  Construir algo nuevo: de startups al Estado (3), René Girard y la irracionalidad humana (3),
  Historia y el costo real del poder (2), Ciencia, longevidad y futuros especulativos (3).
  **Angela Duckworth** (`libros-que-recomienda-angela-duckworth.md`, nuevo): 21 libros en 6
  grupos (3+3+4+4+4+3) — Su propia investigación y las bases de la psicología positiva; Cómo se
  entrena de verdad una habilidad; Motivación y por qué hacemos lo que hacemos; Propósito,
  carácter e infancia; Creatividad, genio y fracaso productivo; Resiliencia y visión de futuro.
  **Daniel Kahneman** (`libros-que-recomienda-daniel-kahneman.md`, nuevo): 9 libros en 4 grupos
  (2+3+2+2) — Su propia obra y el mapa de nuestros sesgos; Cómo el contexto moldea la decisión;
  Riesgo, responsabilidad y el largo plazo; Los límites del juicio experto.
  **James Clear** (`libros-que-recomienda-james-clear.md`, nuevo — usa su catálogo actual de 36
  libros vinculados, NO el backlog perdido de 131 candidatos del 2026-07-17, por decisión del
  usuario): 36 libros en 7 grupos (6+6+5+4+4+5+6) — Hábitos, decisiones y la mente que elegimos;
  Grandes ideas para entender el mundo (y a nosotros mismos); Negocios y el arte de crear algo
  que dure; Biografías y rutinas de gente notable; Coraje real: historias de superación y
  resistencia; Clásicos que atraviesan generaciones; Novelas sobre identidad, raza y el peso de
  la historia. Confirmado que las 36 fichas leídas tenían `james-clear` en `recomendadoPor`.
  Verificación (Opus): spot-check completo de los listicles de Kahneman y James Clear (los dos
  de mayor riesgo, uno por antigüedad del referente y otro por escala) — 0 títulos parafraseados
  (todos usan el `titulo` exacto de cada ficha), 0 citas inventadas, 0 duplicados, estructura y
  tono consistentes con los listicles previos (Vitalik Buterin, Andrew Ng, Reese Witherspoon
  como modelos). **Blog: 18 → 22 artículos.** Con esto se cierra la tanda completa de discovery +
  enriquecimiento + listicle para Thiel, Duckworth y Kahneman, y queda publicado por primera vez
  el listicle de James Clear.
  **`detectar_duplicados.py` corrido por Marcelo (2026-07-23): 0 `[DUP]` exactos, 49 `[REV]`**
  (autores con 2+ libros) — revisados todos: 100% legítimos, obras distintas del mismo autor,
  incluyendo los casos nuevos de esta tanda (René Girard, Timothy Snyder, Neal Stephenson,
  Michael Lewis, Yuval Noah Harari). Catálogo confirmado limpio, sin duplicados reales.

- **2026-07-23 — Acción "Profundizar": Oprah Winfrey, tanda 4 (23 libros: 22 NUEVO + 1 caso
  especial).** Decisión del usuario (vía pregunta): tanda parcial de ~20-25 sobre el backlog
  restante (~56 candidatos), priorizando los picks más relevantes/reconocibles (los primeros
  históricos del club, autores ya conocidos por el catálogo, y los lanzamientos 2025-2026 de
  mayor perfil) en vez de los 56 completos. También decidido: **incluir "Enough"** (libro propio
  de Oprah, coescrito con la Dra. Ania M. Jastreboff, regla ya establecida del sitio) y
  **excluir los 3 libros infantiles de Bill Cosby** (dic. 1997, fuera del tono/audiencia del
  catálogo — mismo criterio que excluyó antes la saga completa de Harry Potter).
  Trabajo hecho vía **3 subagentes Sonnet en paralelo** (lotes de 8/8/7), cada uno con
  verificación de colisiones de slug/autor ANTES de escribir (Grep + Glob).
  **Lote 1 (8, picks históricos 1996-2002):** The Deep End of the Ocean [solo inglés, asin
  0140286276 — el PRIMER libro elegido en la historia del club, sept. 1996] (Jacquelyn
  Mitchard); She's Come Undone [solo inglés, asin 0671021001] (Wally Lamb); Stones from the
  River [solo inglés, asin 0684858096] (Ursula Hegi); Here on Earth [solo inglés, asin
  0425169693] (Alice Hoffman); Black and Blue [solo inglés, asin 0440226104] (Anna Quindlen); I
  Know This Much Is True [solo inglés, asin 0006513239] (Wally Lamb); Donde está el corazón [ES,
  Ediciones B, asin 8440669771] (Billie Letts); Arrodíllate [ES, Mondadori, asin 843970285X]
  (Ann-Marie MacDonald).
  **Lote 2 (8, 2007-2024, varios con disambiguación de autor ya en catálogo):** The Measure of a
  Man [solo inglés, asin 0061357901, categoria memorias] (Sidney Poitier); Ruby [solo inglés,
  asin 0804188246] (Cynthia Bond); Desconcierto/Bewilderment [ES, AdN/Alianza, asin 841362682X —
  distinto de *El clamor de los bosques*, mismo autor Richard Powers, ya en catálogo vía Bill
  Gates] (Richard Powers); The Love Songs of W. E. B. Du Bois [solo inglés, asin 006294293X]
  (Honorée Fanonne Jeffers); The Way of Integrity [solo inglés, asin 0593298780, categoria
  psicologia] (Martha Beck); Agridulce/Bittersweet [ES, Ediciones Urano, asin 8417694692,
  categoria psicologia — distinto de *Quiet*, misma autora Susan Cain, ya en catálogo]; Cosas
  pequeñas como esas/Small Things Like These [ES, Eterna Cadencia, asin 8412492110 — distinto de
  *So Late in the Day*, misma autora Claire Keegan, ya en catálogo]; Familiaris [solo inglés,
  asin 0349147086 — precuela de *The Story of Edgar Sawtelle*, mismo autor David Wroblewski, ya
  en catálogo].
  **Lote 3 (7, 2025-2026, lanzamientos muy recientes + 1 caso especial):** Dream State [solo
  inglés, asin 0385550669] (Eric Puchner); The Tell [solo inglés, asin 0593731204, categoria
  memorias] (Amy Griffin); Matriarch [solo inglés, asin 0593597400, categoria memorias] (Tina
  Knowles); El emperador de Alegría/The Emperor of Gladness [ES, Anagrama, asin 8433947796 —
  distinto de *On Earth We're Briefly Gorgeous*, mismo autor Ocean Vuong, ya en catálogo] (Ocean
  Vuong); Hasta la orilla del río/All the Way to the River [ES, Suma de Letras, asin B0FD6WXDY5
  (ISBN-13 979-prefijo sin ISBN-10, se usó el ASIN), categoria memorias — distinto de *Big
  Magic*, misma autora Elizabeth Gilbert, ya en catálogo] (Elizabeth Gilbert); Kin [solo inglés,
  asin 0525659188 — distinto de *An American Marriage*, misma autora Tayari Jones, ya en
  catálogo] (Tayari Jones); **Enough** [solo inglés, asin 1668217287, categoria memorias, caso
  especial — libro propio de Oprah, coescrito con la Dra. Ania M. Jastreboff, sección de
  atribución adaptada a "Por qué está en esta lista" en vez de "Por qué lo recomienda"] (Oprah
  Winfrey y Ania M. Jastreboff).
  ASIN de las 23 verificado real vía WebSearch (ISBN-10 o ASIN de edición impresa/Kindle real,
  ninguno inventado). 4/23 con edición en español confirmada (Donde está el corazón, Arrodíllate,
  Desconcierto, Agridulce, Cosas pequeñas como esas, El emperador de Alegría, Hasta la orilla del
  río — son 7, no 4, la mayoría de las más recientes 2025-2026 quedaron solo inglés por ser
  lanzamientos muy nuevos). Verificación (Opus): spot-check de 2 fichas (`enough`, `bewilderment`)
  sin errores — atribución correcta, disambiguación de autor sólida, sin citas inventadas de
  Oprah, caso especial de "Enough" bien resuelto. Nota de estilo menor: el slug `shes-come-
  undone` no sigue el patrón habitual del sitio para apóstrofes (`-s-`, como en `why-don-t-
  students-like-school`) — no es un error funcional, solo una inconsistencia cosmética, no
  ameritó renombrar.
  **Oprah Winfrey: 69 → 92 libros vinculados/enriquecidos.** Backlog restante: ~33 candidatos del
  manifiesto original (56 - 23 de esta tanda) + los 3 de Bill Cosby (excluidos por decisión,
  pueden reconsiderarse a futuro si cambia el criterio).
  **2026-07-24 — Listicle de Oprah regenerado a 92** (retomado tras la pausa por Emma Watson):
  integrados a mano (Opus, vía `Edit` puntuales, sin reescribir el archivo) los 23 libros nuevos en
  los grupos temáticos existentes — Familias a la deriva (+6: The Deep End of the Ocean [primer
  pick histórico del club, sept. 1996], She's Come Undone, I Know This Much Is True, Black and
  Blue, Arrodíllate, Familiaris), Comunidades puestas a prueba (+2: Donde está el corazón, El
  emperador de Alegría), El sur profundo (+1: Ruby), Raza/memoria/resistencia (+2: The Love Songs
  of W. E. B. Du Bois, Kin), Viajes/guerra/supervivencia (+2: Stones from the River, Cosas
  pequeñas como esas), Amor y reencuentros (+2: Here on Earth, Dream State), Memorias que
  marcaron una época (+5: The Measure of a Man, The Tell, Matriarch, Hasta la orilla del río,
  Enough), Historia/ciencia/espiritualidad (+3: Desconcierto, The Way of Integrity, Agridulce). No
  se creó ningún grupo nuevo; no se tocó ningún libro preexistente. Verificado por conteo (Grep de
  encabezados `###`/bullets, descontando los 4 repetidos de "Por dónde empezar"): **92/92 libros**
  presentes, 0 faltantes, 0 de más. Frontmatter actualizado (`fechaActualizado: 2026-07-24`,
  descripción "más de 90 picks reales"). **Listicle de Oprah: cerrado y al día.**

- **2026-07-24 — Discovery + enriquecimiento + listicle completo: Emma Watson (Our Shared
  Shelf).** Emma Watson solo tenía 4 libros vinculados (Monólogos de la vagina, Persépolis, Los
  argonautas, El cuento de la criada), todos cargados como cross-refs sueltos — nunca se había
  fetcheado la fuente real de su club de lectura feminista "Our Shared Shelf" (Goodreads,
  2016-2019), pese a que la ficha del referente ya la mencionaba. Fuente fetcheada:
  **radicalreads.com/emma-watson-favorite-books** ("All 32 of Emma Watson's Feminist Book Club
  Picks", vía el hilo completo de Goodreads), que reproduce **citas textuales reales de la propia
  Watson** (marcadas "-EW") para buena parte de los 32 picks — cumple con creces la regla de oro
  de MODO DESCUBRIR. Manifiesto de 32 → reconciliación manual (Grep + Glob, lote no ambiguo): **4
  YA-LINKED** (los 4 ya mencionados) + **1 CROSS-REF** (`pachinko`, ya en catálogo vía Dua Lipa —
  se sumó `emma-watson` a `recomendadoPor` y se renombró la sección a "Por qué lo recomiendan Dua
  Lipa y Emma Watson") + **27 NUEVO** directos, de los cuales 4 con disambiguación de autor ya en
  catálogo (Roxane Gay: *Hunger* ≠ *Bad Feminist*/Dua Lipa; Nicholas D. Kristof: *Half the Sky* ≠
  *Chasing Hope*/Bill Gates; Maya Angelou: *Mom & Me & Mom* ≠ *I Know Why the Caged Bird
  Sings*/Richard Branson; Toni Morrison: *Beloved* ≠ Song of Solomon/Sula/The Bluest Eye/Paradise,
  las 4 de Oprah — confirmadas todas como obras reales y distintas antes de escribir).
  **27 NUEVO enriquecidos** vía 3 subagentes Sonnet en paralelo (9/9/9): Mi vida en la carretera
  [ES, Alpha Decay, asin 8494511343] (Gloria Steinem); El color púrpura [ES, Debolsillo, asin
  8401491150] (Alice Walker); Todo sobre el amor [ES, Paidós, asin 8449337917] (bell hooks); Cómo
  ser mujer [ES, Anagrama, asin 8433977717] (Caitlin Moran); Hunger Makes Me a Modern Girl [solo
  inglés, Riverhead, asin 0399184767] (Carrie Brownstein); La mitad del cielo [ES, Duomo, asin
  8492723823] (Kristof/WuDunn); Mom & Me & Mom [solo inglés, asin 1400066115] (Maya Angelou);
  Mujeres que corren con los lobos [ES, Ediciones B, asin 8413141214] (Clarissa Pinkola Estés); El
  mito de la belleza [ES, Continta Me Tienes, asin 8412087682] (Naomi Wolf); Hambre [ES, Capitán
  Swing, asin 8494740881] (Roxane Gay); El poder [ES, Roca Editorial, asin 8416859213] (Naomi
  Alderman); Por qué no hablo con blancos sobre racismo [ES, Península, asin 8499429572] (Reni
  Eddo-Lodge); Heart Berries [solo inglés, Counterpoint, asin 1619023342] (Terese Marie Mailhot);
  Las chicas del radio [ES, Capitán Swing, asin 8494886118] (Kate Moore); El odio que das [ES,
  Gran Travesía, asin 8494631578] (Angie Thomas); Leche y miel [ES, asin 151199715X] (Rupi Kaur);
  Rebeca [ES, Debolsillo, asin 8497938860] (Daphne du Maurier); La hermana, la extranjera [ES,
  Horas y Horas, asin 8487715931] (Audre Lorde); Eloquent Rage [solo inglés, asin 1250112575]
  (Brittney Cooper); Good and Mad [solo inglés, asin 1501181815] (Rebecca Traister); The Things I
  Would Tell You [solo inglés, asin 0863561462] (ed. Sabrina Mahfouz); Fierce Femmes and Notorious
  Liars [solo inglés, asin 0994047134] (Kai Cheng Thom); Solito, Solita [solo inglés, asin
  1608466183] (ed. Mayers/Freedman); Mariposa [ES, Plaza & Janés, asin 8401022134] (Yusra
  Mardini); Beloved [ES, DeBolsillo, asin 8490625107] (Toni Morrison); ¿De quién es esta historia?
  [ES, Lumen, asin 8426424457] (Rebecca Solnit); Cenicienta liberada [ES, Lumen, asin 842640779X]
  (Rebecca Solnit).
  Todas las citas textuales de Emma Watson usadas (marcadas "-EW" en la fuente) fueron traducidas
  y tejidas en prosa, atribuidas correctamente; para los picks sin cita propia (~14 de 27) no se
  inventó ninguna, solo se contextualizó el pick dentro de Our Shared Shelf.
  Verificación (Opus): spot-check de 2 fichas (`beloved`, `hunger`) sin errores — disambiguación de
  autor sólida, cita real bien atribuida, sin invenciones. ASIN de las 27 verificado real (10
  caracteres), ninguno inventado. **Emma Watson: 4 → 32 libros vinculados/enriquecidos, backlog
  100% cerrado** (Our Shared Shelf terminó en enero de 2020, así que no hay picks futuros que
  esperar).
  **Listicle escrito de cero** (`libros-que-recomienda-emma-watson.md`, no existía antes): 32
  libros en 7 grupos temáticos — El eje del club: cuerpo, deseo y voz propia (5); Memorias de
  artistas y activistas (5); Historias reales de supervivencia y coraje (4); Teoría y ensayo
  feminista (7); Ficción especulativa: cuando el poder cambia de manos (2); Novelas sobre raza,
  identidad e historia (4); Voces nuevas, antologías y relecturas (5). **Blog: 22 → 23 artículos.**
  Pendiente recomendado: correr `detectar_duplicados.py` (Marcelo, desde Windows) para confirmar
  que los 4 casos de disambiguación de autor de esta tanda quedaron bien.

- **2026-07-24 — Richard Branson: tanda 3/3 (CIERRE del backlog, 21 libros).** Última tanda
  pendiente desde el 2026-07-13/16 sobre la fuente **virgin.com/branson-family/richard-branson-
  blog/70-must-read-books** (abril 2017). Se re-fetcheó la fuente completa para confirmar autores
  exactos de los 21 ítems restantes (varios ambiguos de memoria) antes de despachar. Enriquecidos
  vía 3 subagentes Sonnet en paralelo (7/7/7): Winners: And How They Succeed [solo inglés, asin
  0091958857] (Alastair Campbell); Abundancia: El futuro es mejor de lo que piensas [ES, Antoni
  Bosch, asin 8495348926 — **slug distinto** `abundance-the-future-is-better-than-you-think`,
  disambiguado de `abundance.md`/Klein-Thompson ya en catálogo vía Gates/Obama] (Diamandis y
  Kotler); The Weather Makers [solo inglés, asin 0802142923] (Tim Flannery); Big World, Small
  Planet [solo inglés, asin 0300218362] (Rockström y Klum); Necker: A Virgin Island [solo inglés,
  edición limitada teNeues, asin 3832797947 — **formato adaptado "Qué es"** en vez de "De qué
  trata", libro de fotografía sobre la isla privada de Branson] (Russell James); Lost Ocean [solo
  inglés, asin 0143108999 — **formato adaptado**, coloring book] (Johanna Basford); Arctica: The
  Vanishing North [solo inglés, asin 3832732810 — prólogo del propio Branson, dato verificado]
  (Sebastian Copeland); In-N-Out Burger [solo inglés, asin 0061346713] (Stacy Perman); The
  Overview Effect [solo inglés, asin 1563472600] (Frank White); En defensa de la felicidad [ES,
  Urano, asin 8479537841] (Matthieu Ricard); A Time for New Dreams [solo inglés, asin 1788549635]
  (Ben Okri); The Meaning of the 21st Century [solo inglés, asin 1573223239] (James Martin); Self
  Belief: The Vision [solo inglés, asin 0753555395] (Jamal Edwards); One Hundred & One Reasons to
  Get Out of Bed [solo inglés, asin 0994462808 — el agente corrigió el tema real del libro
  (entrevistas a conservacionistas ambientales, no autoayuda genérica) tras investigar] (Natasha
  Milne); If I Could Tell You Just One Thing [solo inglés, asin 1782119248] (Richard Reed);
  Letters to a Stranger [solo inglés, asin 0718181611 — vendido comercialmente como *Dear
  Stranger: Letters on the Subject of Happiness*, mismo proyecto benéfico a favor de MIND, mismo
  Branson como uno de los autores de las cartas, `autorLibro: "VV.AA."`] (VV.AA.); Ending the War
  on Drugs [solo inglés, asin 0753557460, `autorLibro: "VV.AA."` — compilado por el propio Branson
  como miembro de la Global Commission on Drug Policy, con ensayos de expresidentes (Zedillo,
  Cardoso, Obasanjo, Gaviria) y expertos en política de drogas] (VV.AA.); Little Wins [solo
  inglés, asin 0241977940] (Paul Lindley); Beyond the Blue: The Ultimate Insider's Guide to the
  XPRIZE Revolution [solo inglés, asin 1886743207 — título ambiguo resuelto con alta confianza vía
  contexto (el ítem siguiente en la lista original de Branson es *Abundance* de Peter Diamandis,
  fundador del XPRIZE)] (James Richard Campbell); Obama: The Historic Presidency of Barack Obama –
  2,920 Days [solo inglés, asin 1454926392 — formato semi-adaptado, libro de fotografía] (Mark
  Greenberg); La casa más lejana/The Outermost House [ES, Volcano Libros, asin 8494993429] (Henry
  Beston, 1928).
  Verificación (Opus): spot-check de 3 fichas (`beyond-the-blue`, `101-reasons-to-get-out-of-bed`,
  `necker-a-virgin-island`) sin errores — investigación honesta en los casos más ambiguos (el
  agente corrigió su propia hipótesis inicial sobre 101 Reasons tras encontrar el libro real),
  formato adaptado bien resuelto para los libros de fotografía/coloring book, sin contenido
  inventado. ASIN de los 21 verificados reales (10 caracteres), ninguno inventado.
  **Richard Branson: 49 → 70 libros vinculados/enriquecidos — backlog 100% cerrado** (coincide
  exactamente con el título original de la fuente, "70 must-read books").

  **2026-07-24 — Listicle de Branson regenerado a 70.** Corrección de un supuesto erróneo: se le
  pidió al subagente escribir el listicle "por primera vez" asumiendo que no existía, pero en
  realidad SÍ existía desde el 2026-07-16 (49 libros, formato `###`) — un dato que ya estaba
  correctamente registrado en este mismo archivo más arriba pero que no se tuvo a mano al planear
  esta tanda. El subagente detectó el archivo existente y lo reemplazó por completo (vía `Write`)
  con la versión de 70 libros en formato de bullets (estilo James Clear/Reese Witherspoon), sin
  pérdida de contenido real (los 49 libros previos están todos re-incluidos con su reseña
  correspondiente). **70/70 libros verificados** (checklist 1-70 sin huecos ni repetidos, hecha
  por el propio subagente antes de escribir) en **9 grupos temáticos**: Clásicos de infancia que
  nunca envejecen (8), Aventura y clásicos de siempre (10), Ciencia ficción y especulación sobre
  el futuro (6), Historia/guerra/coraje real (9), Negocios/liderazgo/modelos que rompen las reglas
  (10), Ciencia/cosmos/planeta (9), Filantropía/justicia/coraje moral (6), Bienestar/propósito/
  crecimiento personal (6), Fotografía/naturaleza/objetos que se disfrutan en silencio (6).
  Verificación (Opus): lectura completa del archivo final, sin errores — todos los `titulo` exactos,
  slugs verificados, sin duplicados. **Corrección de bookkeeping importante**: al recontar el
  directorio de blog completo (`Glob`), el catálogo real es **28 artículos** (27 listicles de
  referente + 1 best-of de categoría), no 23 como se venía registrando en PENDIENTES.md — el
  conteo previo nunca había incluido a Richard Branson (con listicle desde 07-16) ni a Malcolm
  Gladwell (con listicle propio ya existente, referente que PENDIENTES.md listaba erróneamente
  como "sin arrancar"). Corregido en PENDIENTES.md.

- **2026-07-31 — Acción "Profundizar": Oprah Winfrey, tanda 5 (CIERRE del backlog, 30 libros).**
  El manifiesto original de 119 candidatos del discovery del 2026-07-13 vivía solo en
  `/tmp/manifiesto_oprah_full.txt` (no versionado) y ya no estaba disponible. **Se reconstruyó el
  backlog restante re-fetcheando la fuente completa** (beyondthebookends.com/oprahs-book-club-list,
  actualizada 2/6/2026) y comparándola contra los 92 libros ya vinculados (`Grep` de
  `recomendadoPor: oprah-winfrey`) — método equivalente a un mini-discovery incremental, ya
  anticipado como patrón válido en la nota de cierre de Dua Lipa. Resultado: **30 candidatos NUEVO**
  (21 históricos 1996-2001 + 9 recientes 2022-2026, incluidos los picks reales de 2026 hasta junio),
  todos confirmados como obras reales antes de escribir (caso especial verificado por WebSearch:
  *John of John* de Douglas Stuart, pick #123 del club, mayo 2026 — título correcto, no error de
  scraping de la fuente). Decisión del usuario (vía pregunta): **los 30 completos en esta tanda**,
  cerrando el backlog al 100%.
  Trabajo hecho vía **4 subagentes Sonnet en paralelo** (lotes de 8/7/7/8) + 4 fichas completadas
  a mano por el orquestador tras fallas parciales de dos subagentes (uno cortado por error de API
  a mitad de stream, otro con dos ítems sin terminar): **What Looks Like Crazy on an Ordinary Day**
  [solo inglés, asin 0061710385 — título real difiere del truncado "What Looks Crazy..." de la
  fuente, corregido tras verificar] (Pearl Cleage); **Jewel** [solo inglés, asin 0671038184, edición
  "Oprah's Book Club"] (Bret Lott); **John of John** [solo inglés, asin 0802167195, finalista Orwell
  Prize y longlist Booker 2026] (Douglas Stuart, ya en catálogo vía *Shuggie Bain*); **Little Wonder**
  [solo inglés, asin B0G5X5Z5R9 — ISBN-13 979-prefijo sin ISBN-10, se usó el ASIN de Amazon, sello
  Thousand Voices de Jenna Bush Hager] (Sophie Chen Keller).
  Resto de las 26 fichas (subagentes): The Book of Ruth, The Rapture of Canaan, The Heart of a Woman,
  Songs in Ordinary Time, Mujer virtuosa (A Virtuous Woman) y Ellen Foster [mismo mes, misma autora
  Kaye Gibbons, libros distintos] (histórico 1996-97); The Pilot's Wife, Mother of Pearl, Tara Road,
  River Cross My Heart, Vinegar Hill, A Map of the World [misma autora que The Book of Ruth, Jane
  Hamilton, libro distinto] y Gap Creek (1999); Back Roads, While I Was Gone, Open House, Drowning
  Ruth, Icy Sparks, Stolen Lives (memoria real, coautora Michèle Fitoussi) y Cane River (2000-01);
  That Bird Has My Wings, The Many Lives of Mama Love, Culpability, A Guardian and A Thief, Some
  Bright Nowhere y Go Gentle (2022-26). Disambiguaciones de autor verificadas sin error: Maya
  Angelou (*The Heart of a Woman* ≠ *Yo sé por qué canta el pájaro enjaulado*/*Mom & Me & Mom*, ya
  en catálogo); Jane Hamilton (*The Book of Ruth* ≠ *A Map of the World*, ambos NUEVO); Kaye Gibbons
  (dos libros distintos el mismo mes). Solo 7/30 con edición en español confirmada (Mujer virtuosa,
  Ellen Foster, La mujer del piloto, Madreperla, Tara Road: una casa en Irlanda) — la mayoría de los
  históricos 1996-2001 y casi todos los de 2024-2026 quedaron solo inglés (lanzamientos muy
  recientes o ediciones agotadas sin reedición ES). ASIN de los 30 verificado real (10 caracteres o
  ASIN de Amazon cuando no hay ISBN-10), ninguno inventado.
  **Oprah Winfrey: 92 → 122 libros vinculados/enriquecidos. Backlog: 100% cerrado** (no quedan
  candidatos pendientes del manifiesto beyondthebookends.com; quedan excluidos por decisión los 3
  infantiles de Bill Cosby, dic. 1997, reconsiderables a futuro si cambia el criterio).
  **Listicle regenerado a 122** vía `Edit` puntuales (sin reescribir el archivo): se sumaron los 30
  libros a los grupos temáticos existentes (Mother of Pearl → El sur profundo; River Cross My Heart
  y Cane River → Raza/memoria/resistencia; Rapture of Canaan, Icy Sparks y John of John →
  Comunidades puestas a prueba; A Guardian and A Thief → Viajes/guerra/supervivencia; Culpability,
  Some Bright Nowhere, Go Gentle y Little Wonder → Familias a la deriva; The Heart of a Woman,
  Stolen Lives, That Bird Has My Wings y The Many Lives of Mama Love → Memorias que marcaron una
  época) y se crearon **2 grupos temáticos nuevos** para no desbalancear "Familias a la deriva"
  (que hubiera quedado con 27 libros, por encima del umbral de subdivisión del propio playbook):
  **"El club 1.0: infancias y familias que se quiebran"** (8: Book of Ruth, Ellen Foster, Jewel,
  Vinegar Hill, Back Roads, Drowning Ruth, A Map of the World, Gap Creek) y **"El club 1.0: mujeres
  que reinventan su vida"** (7: Songs in Ordinary Time, Mujer virtuosa, What Looks Like Crazy on an
  Ordinary Day, The Pilot's Wife, Tara Road, Open House, While I Was Gone). Frontmatter actualizado
  (`fechaActualizado: 2026-07-31`, descripción "más de 120 picks reales"). **Verificado por conteo**
  (`Grep` de links `### [...](/libros/...)`, 126 ocurrencias − 4 duplicados intencionales del bloque
  "Por dónde empezar" = 122 únicos): coincide exacto con las 122 fichas reales. **Listicle de Oprah:
  cerrado y al día — backlog en 0.**

- **2026-07-31 — Acción "Nuevo referente": Isabel Allende (alta completa).** Primera figura hispana
  del catálogo (prioridad #1 del backlog de referentes nuevos en `CONSOLIDADO_candidatos_
  referentes.md`, ver PENDIENTES.md §11). Fuente documentada y fetcheada: **The Week, "Isabel
  Allende's 6 favorite books"** (2014, actualizada 2016), entrevista con cita textual propia de
  Allende por cada libro — mismo estándar de fuente que Malcolm Gladwell/Emma Watson. Reconciliación
  manual (`Grep`/`Glob`, 6 candidatos, sin ambigüedad): **2 CROSS-REF** (`one-hundred-years-of-
  solitude`, ya en catálogo vía Dua Lipa/Richard Branson/Oprah; `the-road`, ya en catálogo vía
  Oprah) + **4 NUEVO**: Las mil y una noches [ES, Cátedra, asin 8437634512, `autorLibro: "Anónimo"`]
  ; La mujer eunuco [ES, Kairós, asin 8472455769, categoria historia] (Germaine Greer); Drácula [ES,
  Alianza, asin 8420687413] (Bram Stoker); Broken Open: How Difficult Times Can Help Us Grow [solo
  inglés, asin 0375759913, categoria memorias] (Elizabeth Lesser).
  **Bio del referente** (`autores/isabel-allende.md`, orden 50): biografía real con foco en el
  exilio de 1973, *La casa de los espíritus*, y la fuente de sus recomendaciones. Sumada a
  `src/lib/ambitos.ts` bajo el ámbito "Escritores".
  **Cross-refs aplicados con desarrollo en prosa** (no solo frase de cierre, por la riqueza de la
  cita real de Allende): `the-road.md` pasó de una sección desarrollando solo a Oprah a
  "Por qué lo recomiendan Oprah Winfrey e Isabel Allende", con la cita real de Allende sobre el
  libro citada y traducida; `one-hundred-years-of-solitude.md` sumó a Allende con su cita real en
  la frase de cierre (ya tenía 2 referentes desarrollados — Dua Lipa como principal —, así que
  Allende se nombra sin abrir desarrollo propio, respetando el máximo de 2 de MODO LIBRO).
  Las 4 citas reales de Allende (Mil y una noches, Mujer eunuco, Drácula, La carretera, Cien años de
  soledad) traducidas del inglés y atribuidas correctamente, ninguna inventada. Nota de contexto
  verificada: el libro de Elizabeth Lesser lo recomienda en relación directa con el duelo por la
  muerte de su hija Paula (1992), tema que la propia Allende trató en sus memorias *Paula* — dato
  real usado para enriquecer la sección de atribución sin inventar biografía.
  ASIN de los 4 NUEVO verificado real (10 caracteres), ninguno inventado.
  **Isabel Allende: 0 → 6 libros vinculados/enriquecidos, backlog 100% cerrado** (la fuente es una
  lista fija y cerrada de 2014, no un club de lectura con picks nuevos — no hay backlog pendiente
  salvo que Allende dé una entrevista nueva con más recomendaciones a futuro).
  **Listicle escrito de cero** (`libros-que-recomienda-isabel-allende.md`): lista simple sin grupos
  temáticos (regla de MODO LISTICLE para menos de 8 libros), los 6 en el orden de la fuente original.
  **Referentes: 40 → 41. Catálogo: 392 → 396 libros** (392 + 4 NUEVO). **Blog: 28 → 29 artículos.**
  Pendiente recomendado: correr `detectar_duplicados.py` (Marcelo, desde Windows) para confirmar
  que los 2 cross-ref y las 4 fichas nuevas quedaron bien.

- **2026-07-31 — Acción "Nuevo referente": Mario Vargas Llosa (1936-2025, alta completa).**
  Segunda figura hispana del catálogo. **Discovery ya hecho por Marcelo** (fuera de sesión):
  manifiesto de 45 candidatos en `vargas-llosa-manifiesto.txt` (raíz del repo), de dos fuentes
  documentadas — **RPP** ("Mario Vargas Llosa recomienda sus 10 libros favoritos al mundo") y
  **La verdad de las mentiras** (1990, su libro de ensayos) + **Historia de un deicidio** (1971,
  su monografía sobre García Márquez). Marcelo corrió `reconciliar.py` en Windows y pegó la salida:
  **YA-LINKED=0, CROSS-REF=6, REVISAR=6, NUEVO=34**. Los 6 REVISAR se resolvieron a **NUEVO** tras
  confirmar que son obras reales y distintas del mismo autor ya en catálogo: Steppenwolf ≠
  Siddhartha (Hesse); Sanctuary ≠ Mientras agonizo/Luz de agosto/El sonido y la furia (Faulkner);
  The Power and the Glory y The End of the Affair ≠ The Quiet American (Greene, 2 libros distintos
  del mismo autor); Animal Farm ≠ 1984 (Orwell); One Day in the Life of Ivan Denisovich ≠
  Archipiélago Gulag (Solzhenitsyn). **Total: 6 CROSS-REF + 40 NUEVO = 46 libros.**
  **Bio del referente** (`autores/mario-vargas-llosa.md`, orden 50, escrita **en pasado** por
  tratarse de un referente fallecido): biografía real con foco en el boom latinoamericano, el
  Nobel 2010 y las dos fuentes documentadas de sus recomendaciones. Sumada a `src/lib/ambitos.ts`
  bajo "Escritores".
  **6 cross-refs aplicados** (editados a mano por el orquestador, con desarrollo en prosa donde
  había dato real específico y solo mención en la frase de cierre donde no): `light-in-august.md`
  desarrollado a fondo (Vargas Llosa la llamó "la más moderna" de sus 10 favoritos, dato real de
  RPP) — pasó a "Por qué lo recomiendan Oprah Winfrey y Mario Vargas Llosa"; `heart-of-darkness.md`,
  `brave-new-world.md`, `east-of-eden.md` y `lolita.md` sumados en la frase de cierre (ya tenían
  otro referente desarrollado, y no hay cita textual verificada de Vargas Llosa libro por libro en
  *La verdad de las mentiras* — se optó por no inventar citas, solo mencionar el hecho real de que
  los reseñó ahí); `one-hundred-years-of-solitude.md` (ya con 4 referentes) sumó a Vargas Llosa en
  el cierre con un dato real y rico: le dedicó un libro entero, *Historia de un deicidio*, a la obra
  de García Márquez.
  **40 NUEVO enriquecidos vía 5 subagentes Sonnet en paralelo** (lotes 9/8/8/8/7, arrancando por
  los 10 favoritos de RPP según pidió Marcelo): tanda 1 — Don Quijote de la Mancha, Guerra y paz,
  Madame Bovary, Moby Dick, Tirant lo Blanc (con dato real: la edición de Alianza usada trae
  prólogo del propio Vargas Llosa), La montaña mágica, Los demonios, Esplendores y miserias de las
  cortesanas, Ulises; tanda 2 — La señora Dalloway, Auto de fe, La casa de las bellas durmientes,
  El cuaderno dorado, Sostiene Pereira, La muerte en Venecia, Dublineses, Manhattan Transfer; tanda
  3 — El gran Gatsby, El lobo estepario, Nadja, Santuario, La condición humana, Trópico de Cáncer,
  Siete cuentos góticos, El cero y el infinito; tanda 4 — El poder y la gloria, El fin de la
  aventura, El extranjero, Rebelión en la granja, La romana, El reino de este mundo (Carpentier
  escribió en español — blockquote adaptado a "idioma original: español" en vez de "traducción
  de…"), El viejo y el mar, París era una fiesta (memorias, no ficción); tanda 5 — No soy Stiller,
  El Gatopardo, Doctor Zhivago, El tambor de hojalata, Un día en la vida de Iván Denísovich,
  Opiniones de un payaso, Herzog. Todos los subagentes verificaron colisión de slug/autor antes de
  escribir (Faulkner, Greene, Hemingway y Solzhenitsyn tenían más de un libro entre los candidatos
  o ya en catálogo). **40/40 ASIN verificados reales (10 caracteres), ninguno inventado — 39/40 con
  edición en español confirmada** (solo *A Harlot High and Low* usó una edición de 2025 recién
  publicada en español, y ningún título quedó "solo inglés": el catálogo de clásicos tiene
  traducción española consolidada para prácticamente todo). Para las secciones de atribución sin
  cita textual verificada, todos los subagentes usaron el marco fijo indicado ("Vargas Llosa lo
  reseñó en *La verdad de las mentiras*...") sin inventar citas puntuales por libro.
  **Mario Vargas Llosa: 0 → 46 libros vinculados/enriquecidos, backlog 100% cerrado** (el
  manifiesto original de 45 candidatos está completo — no queda backlog salvo que en el futuro
  aparezca una fuente nueva y documentada con más recomendaciones suyas, algo poco probable dado
  que el referente ya falleció).
  **Listicle escrito de cero** (`libros-que-recomienda-mario-vargas-llosa.md`): 46 libros en **6
  grupos temáticos** — Sus diez favoritos de toda la vida (10, la lista RPP completa), Vanguardia y
  experimentación narrativa (8), Totalitarismo/poder/resistencia individual (9, temática ligada
  directamente a la cita del Nobel de Vargas Llosa), Pasiones/cuerpo/transgresión (8), Mundos que
  se apagan: aristocracias/imperios/épocas doradas (5), Fe/soledad/resistencia moral (6) — más lead
  "Por dónde empezar" (4: Don Quijote, Cien años de soledad, El extranjero, El viejo y el mar).
  **Verificado por conteo** (`Grep` de links `### [...](/libros/...)`, 50 ocurrencias − 4
  duplicados del lead = 46 únicos): coincide exacto con las 46 fichas reales.
  **Referentes: 41 → 42 (segunda figura hispana). Catálogo: 396 → 436 libros** (396 + 40 NUEVO).
  **Blog: 29 → 30 artículos.**
  Pendiente recomendado: correr `detectar_duplicados.py` (Marcelo, desde Windows) para confirmar
  que los 6 cross-ref y las 40 fichas nuevas quedaron bien.

- **2026-08-01 — Alta de Jenna Bush Hager (referente #43, "Nuevo referente" pipeline completo).**
  **Bio:** `autores/jenna-bush-hager.md` creada (orden 50, ámbito "Entretenimiento" en `ambitos.ts`) —
  presentadora de TODAY (NBC) y creadora de **Read With Jenna**, club de lectura mensual desde marzo
  de 2019. **Discovery:** fetch de la fuente oficial `today.com/read-with-jenna-book-club-list` —
  la página estática solo expuso los picks de **febrero 2024 a julio 2026** (30 meses + 1 bonus, 31
  títulos); el archivo histórico completo (marzo 2019–enero 2024, ~55 picks más) está detrás de
  paginación JS y queda como **backlog para una futura sesión "Profundizar"** (no sourceado
  todavía). **Reconciliación:** hecha a mano vía `Grep` contra `src/content/libros/` (mismo
  resultado que `reconciliar.py`, sin usar bash) — **0 YA-LINKED, 0 CROSS-REF, 31 NUEVO**. Decisión
  de Marcelo (vía pregunta): encarar los 31 ahora, dejar el archivo histórico para después.
  **Enriquecidas las 31 fichas NUEVO** vía 4 subagentes Sonnet en paralelo (tandas de 8/8/8/7):
  Todo final es un comienzo [8408287478] (Dolly Alderton), Entre dos aguas [0063292211] (Cristina
  Henríquez), La casa en Mango Street [8466360840] (Sandra Cisneros, bonus marzo 2024), The
  Husbands [0385550618, sin ES] (Holly Gramazio), Real Americans [0593537254, sin ES] (Rachel
  Khong), Swift River [1668027917, sin ES] (Essie Chambers), Todos los colores de la oscuridad
  [8419851701] (Chris Whitaker), The Wedding People [1250899575, sin ES] (Alison Espach), Las
  hermanas Blue [8492919701] (Coco Mellors), Poderoso río Rojo [**sin ASIN** — ISBN-13 979, sin
  ISBN-10 confirmado] (Louise Erdrich), This Motherless Land [0063084295, sin ES] (Nikki May),
  Devociones. Poesía reunida [8426431941] (Mary Oliver, antología poética), The Life Cycle of the
  Common Octopus [0593830458, sin ES] (Emma Knight), This Is a Love Story [0593851269, sin ES]
  (Jessica Soffer), The Dream Hotel [0593317602, sin ES] (Laila Lalami), Heartwood [1668063611, sin
  ES] (Amity Gaige), Los nombres [8419851817] (Florence Knapp), Un asunto de familia [8439746172]
  (Claire Lynch), Happy Wife [0593974379, sin ES] (Meredith Lavender y Kendall Shores), My Other
  Heart [0593831012, sin ES] (Emma Nanami Strenner), Buckeye [0593595033, sin ES] (Patrick Ryan),
  The Irish Goodbye [1250408156, sin ES] (Heather Aimee O'Neill), Cursed Daughters [1805463365, sin
  ES — la autora sí tiene otra novela traducida] (Oyinkan Braithwaite), Orgullo y prejuicio
  [8420632902] (Jane Austen, pick especial aniversario 250), Homeschooled: A Memoir [1335000984,
  sin ES, memorias] (Stefan Merrill Block), One & Only [B0FHN8C9X3, sin ES] (Maurene Goo), Wait for
  Me [1250399300, sin ES] (Amy Jo Burns), Upward Bound [0593979974, sin ES] (Woody Brown), Caller
  Unknown [0063338475, sin ES] (Gillian McAllister), The Children [0063487438, sin ES] (Melissa
  Albert), The Shampoo Effect [B0FTFLTHMF, sin ES] (Jenny Jackson, pick más reciente jul-2026).
  **30/31 con ASIN real de 10 caracteres** (1 vacío: Poderoso río Rojo/The Mighty Red, fallback de
  búsqueda). **Verificación:** 0 `[DUP]` de título vía `Grep` (chequeo manual) confirmado después
  con `detectar_duplicados.py` corrido por Marcelo en Windows sobre el catálogo completo: **0
  `[DUP]` exactos, 74 `[REV]`** (autores con 2+ libros, todos informativos/legítimos — suma 2 casos
  nuevos por esta tanda: Maurene Goo con *One & Only* [Jenna] + *Throwback* [Reese Witherspoon], y
  Jane Austen con *Orgullo y prejuicio* [Jenna] + *Emma* [J.K. Rowling], ambos pares de libros
  distintos del mismo autor). Spot-check de 3 fichas (Good Material, Devotions, Pride and Prejudice)
  sin errores ni citas inventadas.
  ⚠️ **Flag *Upward Bound* — RESUELTO (2026-08-01, mismo día).** Marcelo confirmó los datos exactos:
  es una **novela de ficción** (no memoria — la `categoria: ficcion` ya estaba bien puesta),
  ambientada en un centro de día para adultos con discapacidad en el sur de California, basada en
  parte en la vida de Brown como autista no verbal, escrita junto a su madre Mary Brown con el
  **rapid prompting method (RPM)**, una variante de la **comunicación facilitada (FC)**. Ficha
  editada: se nombra el método explícitamente y se suma una frase neutral sobre la controversia
  científica de la FC/RPM (estudios controlados cuestionan que el mensaje sea del autor y no del
  facilitador; sus defensores, incluida la familia Brown, sostienen que es una herramienta de acceso
  genuina) — mismo criterio de cautela evenhanded ya usado con otros referentes polémicos del
  catálogo.
  **Listicle escrito de cero** (`libros-que-recomienda-jenna-bush-hager.md`): 31 libros en **5
  grupos temáticos** — Relaciones/rupturas/comedias con filo (6), Familias con secretos (7),
  Suspenso/distopías/giros especulativos (7), Comunidad/raíces/duelo compartido (6),
  Clásicos/poesía/no ficción (5) — más lead "Por dónde empezar" (4: Real Americans, Orgullo y
  prejuicio, Las hermanas Blue, The Wedding People).
  **Referentes: 42 → 43. Catálogo: 436 → 467 libros** (436 + 31 NUEVO). **Blog: 30 → 31 artículos.**
  **Pendiente:** backlog histórico de Read With Jenna (marzo 2019–enero 2024, ~55 picks) sin
  sourcear — requiere Chrome/paginación o cruce con Parade/NBC Insider, para una futura
  "Profundizar Jenna Bush Hager".

- **2026-08-03 — Alta de Derek Sivers (referente #44, "Nuevo referente" pipeline completo).**
  **Bio:** `autores/derek-sivers.md` creada (orden 50, ámbito "Negocios e Inversión" en
  `ambitos.ts`) — fundador de CD Baby (vendida en 2008, USD 22M donados a una fundación de
  educación musical), escritor y ex-músico; reseña y puntúa del 1 al 10 cada libro que lee en
  **sivers.org/book**. **Discovery:** manifiesto ya curado a mano por el usuario en
  `derek-sivers-manifiesto.txt` (raíz del repo) — 27 títulos, sus 10/10 y 9/10 más relevantes
  para negocios/psicología/filosofía práctica sobre un catálogo real de 480+ reseñas. **
  Reconciliación:** hecha a mano vía `Glob`/`Grep` contra `src/content/libros/` (sin bash) —
  **4 CROSS-REF + 23 NUEVO**, 0 REVISAR.
  **4 CROSS-REF aplicados** (frontmatter + mención en el cuerpo respetando la regla de
  atribución): sapiens (se sumó a la frase de cierre junto a Obama/Clear/Ravikant/Zuckerberg),
  skin-in-the-game (cierre junto a Kahneman), the-war-of-art (cierre junto a Clear/Holiday),
  atomic-habits (única ficha con recomendadoPor previo de un solo referente-autor — se agregó
  una sección nueva `## Por qué lo recomienda Derek Sivers` en vez de solo una frase de cierre,
  por ser el primer recomendador externo del libro).
  **23 NUEVO enriquecidos** vía 3 subagentes Sonnet en paralelo (tandas de 8/8/7): The Waste
  Books [0940322501, sin ES] (Georg Christoph Lichtenberg); Todo es negociable [8432036064]
  (Herb Cohen); The Listening Book [159030831X, sin ES] (W.A. Mathieu); Atrévete a no gustar
  [8408184164] (Kishimi/Koga); Sum: cuarenta historias desde la otra vida [8467033770] (David
  Eagleman); ¿Padres jardineros o padres carpinteros? [8499986358 — título real corregido en
  verificación, ver flag abajo] (Alison Gopnik); Playful Parenting [0345442865, sin ES]
  (Lawrence J. Cohen); On Writing Well [0060891548, sin ES] (William Zinsser); Tropezar con la
  felicidad [843442522X] (Daniel Gilbert); El mito del emprendedor [8449303656] (Michael E.
  Gerber); 12 reglas para vivir [8408193309] (Jordan Peterson); El sutil arte de que (casi todo)
  te importe una mierda [8491392289] (Mark Manson); El ego es tu enemigo [8408274562] (Ryan
  Holiday); Esto es marketing [8417568263] (Seth Godin); Decide y apuesta [8411004074] (Annie
  Duke); La mente de los justos [842343009X] (Jonathan Haidt); Organízate con eficacia
  [8416997861] (David Allen); Despertando al gigante interior [9700507335] (Tony Robbins); El
  Efecto Compuesto [8393222249] (Darren Hardy); Juegos finitos y juegos infinitos [8478080503,
  confirmado libro distinto de *the-infinite-game* de Simon Sinek] (James P. Carse); How Minds
  Change [0593190297, sin ES] (David McRaney); Problemas salvajes [841796360X] (Russ Roberts);
  Cuando todo se derrumba [8484459942] (Pema Chödrön).
  ⚠️ **Flag *the-gardener-and-the-carpenter* — RESUELTO (2026-08-03, mismo día).** El subagente
  puso el título "El jardinero y el carpintero" sin ASIN confirmado. Verificación de Opus con
  1 búsqueda: la edición ES real (Temas de Hoy, trad. María Jesús Asensio Tudela) se publicó como
  **"¿Padres jardineros o padres carpinteros?"** (asin 8499986358, confirmado por URL directa de
  amazon.es) — título y ASIN corregidos en la ficha (slug sin tocar).
  **23/23 con ASIN real de 10 caracteres** (0 vacíos tras la corrección). Verificación: `asin`
  de 10 chars OK en las 23 (chequeo manual vía `Grep`), `recomendadoPor: [derek-sivers]` OK,
  ningún libro colisiona con el resto del catálogo (los 27 títulos del manifiesto se chequearon
  contra el catálogo completo antes de crear fichas). Spot-check de Opus: 5 fichas leídas
  completas (waste-books, 12-rules-for-life, when-things-fall-apart, getting-things-done,
  this-is-marketing) — estructura, tono, puntaje de Sivers citado correctamente en las 5, sin
  errores.
  **Listicle escrito de cero** (`libros-que-recomienda-derek-sivers.md`): 27 libros en **5
  grupos temáticos** — Negocios, marketing y productividad (6), Hábitos, disciplina y
  superación personal (4), Mente, comunicación y comportamiento (6), Filosofía práctica y
  grandes preguntas (4), Crianza y curiosidad científica (3) — más lead "Por dónde empezar"
  (4: Hábitos atómicos, Sapiens, La guerra del arte, Organízate con eficacia).
  **Referentes: 43 → 44. Catálogo: 467 → 490 libros** (467 + 23 NUEVO). **Blog: 31 → 32
  artículos.**
  **Pendiente:** el catálogo real de Sivers en sivers.org/book supera los 480 libros reseñados;
  esta alta tomó solo la selección curada de 10/10 y 9/10 más vendible en ES — un futuro
  "Profundizar Derek Sivers" podría bajar a puntajes 7-8/10 si se agota el material de alto
  puntaje.

- **2026-08-03 — Profundizar: Jeff Bezos (sin discovery real previo → discovery completo +
  listicle nuevo).** Bezos era uno de los 13 referentes "sin listicle" del catálogo: tenía 4
  libros de la carga base original (Built to Last, The Remains of the Day, The Black Swan, Sam
  Walton: Made in America) pero nunca había pasado por un discovery real. Decisión de Marcelo
  (vía pregunta): profundizar primero, listicle después, en vez de publicar el post con solo 4
  libros. **Discovery:** `web_fetch` sobre mostrecommendedbooks.com/people/jeff-bezos-recommended-
  books (32 libros listados, cada uno con cita y fuente primaria propia — mismo patrón que se usó
  con Satya Nadella). **Reconciliación:** manual vía Glob/Grep contra el catálogo (sin bash) — **4
  YA-LINKED** (los 4 ya mencionados, coinciden exactamente con la fuente, confirma su fiabilidad)
  + **2 CROSS-REF** (Dune, ya recomendado por Tim Ferriss/Elon Musk — Bezos se declaró "gran fan
  de la ciencia ficción" y la ubicó entre sus series favoritas; El jugador/The Player of Games, ya
  recomendado por Mark Zuckerberg — Bezos citó a toda la saga de La Cultura de Iain M. Banks como
  "uno de mis favoritos personales") + **11 NUEVO**. Nota: la fuente cuenta "32 libros" porque
  desagrega la saga Dune (6 tomos) y la saga La Cultura (11 tomos) libro por libro; siguiendo el
  criterio ya usado con la Trilogía de la Fundación, cada saga se representa acá con **una sola
  ficha** (la puerta de entrada de cada una), no con un tomo por separado.
  **2 CROSS-REF aplicados** (frontmatter + mención en el cuerpo, respetando la regla de
  atribución): dune.md y the-player-of-games.md suman `jeff-bezos` a `recomendadoPor`.
  **11 NUEVO enriquecidos** vía 2 subagentes Sonnet en paralelo (tandas de 6/5), todos con cita o
  fuente real documentada (nunca de memoria): Creation: Life and How to Make It [0674011139, sin
  ES] (Steve Grand, según biografía de Brad Stone: "Bezos quedó fascinado"); Data-Driven Marketing
  [0470504544, sin ES] (Mark Jeffery, parte de "Jeff's Reading List"); Reinicia [8492452587]
  (David Heinemeier Hansson y Jason Fried — cita real de Bezos vía basecamp.com/books/rework: "Sin
  dejarse perturbar por la sabiduría convencional..."); El dilema de los innovadores [9506412936]
  (Clayton Christensen, "Jeff's Reading List"); The Mythical Man-Month [0201835959, sin ES
  comprable pese a existir traducción citada en Wikipedia] (Frederick P. Brooks Jr., raíz de los
  "equipos de dos pizzas" de Amazon); Lean Thinking [8498750210] (James P. Womack, "Jeff's Reading
  List"); Empresas que sobresalen [8496426858] (Jim Collins, "Jeff's Reading List"); Memos from
  the Chairman [0761103465, sin ES] (Alan C. Greenberg, "Jeff's Reading List"); La Meta
  [847978718X] (Eliyahu M. Goldratt — según la biografía, "la biblia" del equipo que arregló la
  logística de Amazon); El relojero ciego [8433557378] (Richard Dawkins — **cita textual primaria
  verificada**: "Extraordinary", carta anual a accionistas de Amazon 2020, aboutamazon.com); Lights
  Out [0358250412, sin ES] (Thomas Gryta y Ted Mann — **cita textual primaria verificada**: tweet
  de Bezos de mayo 2022, "If you're looking for some scary bedtime reading...").
  **11/11 con ASIN real de 10 caracteres** (0 vacíos). Verificación: `asin` de 10 chars OK en las
  11 (chequeo manual vía Grep), `recomendadoPor: [jeff-bezos]` OK, total de fichas con
  `jeff-bezos` en `recomendadoPor` confirmado en 17 (4+2+11) vía Grep sobre todo el catálogo.
  Spot-check de Opus: 2 fichas leídas completas (El relojero ciego, Lights Out) — ambas citas
  primarias usadas correctamente entre comillas, resto de citas (vía biografía de Brad Stone)
  correctamente enmarcadas como "según la biografía" y no como cita textual de Bezos.
  **Listicle escrito de cero** (`libros-que-recomienda-jeff-bezos.md`): 17 libros en **3 grupos
  temáticos** — Cultura y disciplina operativa (4), Innovación/riesgo/construcción de equipos y
  productos (5), Fuera de los negocios: ficción/ciencia/ciencia ficción (4) — más lead "Por dónde
  empezar" (4: Empresas que perduran, El cisne negro, La Meta, Dune).
  **Jeff Bezos: 4 → 17 libros. Catálogo: 490 → 501 libros** (490 + 11 NUEVO). **Blog: 32 → 33
  artículos.** Referentes: sin cambios (44) — es "Profundizar", no alta de referente nuevo.
  **Pendiente:** ninguno formal — el discovery cubrió toda la fuente disponible (32/32 ítems de
  mostrecommendedbooks.com reconciliados). Si en el futuro Bezos hace declaraciones nuevas
  (entrevistas, cartas a accionistas, X) se puede volver a profundizar con un discovery chico.

- **2026-08-03 — Profundizar: Natalie Portman (discovery grande, tanda prioritaria 2022-2025 +
  listicle nuevo).** Portman era otra de las "sin listicle": 4 libros de la carga base original
  (The Copenhagen Trilogy, My Brilliant Friend, Fates and Furies, Breasts and Eggs), sin discovery
  real. Su fuente es @natsbookclub, el club de lectura que conduce en Instagram (~129K
  seguidores, un pick mensual). **Discovery:** intenté `web_fetch` sobre
  tertulia.com/editorial-list/complete-list-natalie-portman-book-club (listado oficial más
  completo, 46 picks) pero la página pagina por JS y solo trajo los primeros ~10; Claude in
  Chrome no estaba conectado en la sesión para forzar el scroll. Se completó cruzando 4 fuentes
  secundarias con cita o atribución real por libro: Tertulia (10 picks 2022-2025, con cita
  textual), Brit+Co ("recently read", ~20 títulos 2023-2024), Women.com (7 picks con reseña y
  algunas citas reales), mostrecommendedbooks.com (10 picks históricos 2019-2020, con fuente
  primaria). Total **48 candidatos únicos** tras deduplicar. **Reconciliación:** manual vía
  Glob/Grep — **6 YA-LINKED/CROSS-REF** (Fortuna vía Obama/Dua Lipa, MANIAC vía Obama, Lágrimas en
  H-Mart vía Dua Lipa, Sobre los huesos de los muertos vía Dua Lipa, ¡Mártir! vía Obama, Todo
  sobre el amor vía Emma Watson — los 6 ya estaban en el catálogo) + **42 NUEVO**.
  **Decisión de Marcelo (vía pregunta):** dado el volumen (42 NUEVO, escala similar a Reese
  Witherspoon), priorizar los **25 más recientes y mejor documentados (2022-2025)** ahora, y dejar
  un **backlog de 17** (7 recientes no priorizados + los 10 históricos de 2019-2020) para una
  futura tanda de "Profundizar".
  **6 CROSS-REF aplicados** (frontmatter + mención en el cuerpo, respetando la regla de
  atribución): trust.md, the-maniac.md, crying-in-h-mart.md,
  drive-your-plow-over-the-bones-of-the-dead.md, martyr.md y all-about-love.md suman
  `natalie-portman` a `recomendadoPor` (para trust.md, que ya tenía 2 referentes, se sumó a la
  frase de cierre; el resto tenía 1 solo referente, se agregó una frase de cierre nueva).
  **25 NUEVO enriquecidos** vía 4 subagentes Sonnet en paralelo (tandas de 7/6/6/6), con cita real
  entre comillas cuando existía fuente primaria (Tertulia/Women.com/Brit+Co) y sin inventar
  ninguna cuando no la había (instrucción explícita: "contá que lo sumó a su club, sin comillas"):
  Un poder diferente [6073862709] (Jacinda Ardern, cita real); The English Understand Wool
  [0811230074, sin ES]; Consider Yourself Kissed [1529154758, sin ES] (Jessica Stanley, cita
  real); Saving Five [1035427788, sin ES] (Amanda Nguyen, cita real); Autocracia S.A.
  [8419642967] (Anne Applebaum, cita real); The Coin [1646222768, sin ES] (Yasmin Zaher, cita
  real); ¡Reconquista tu tiempo! [843443752X] (Jenny Odell, cita real, título ES distinto al
  original); La guardiana [8418363010] (Yael Van Der Wouden, cita real); Monstruos [841100211X]
  (Claire Dederer, cita real); El lago de la creación [B0FDQWQ46Q — ASIN no-ISBN de edición ES
  reciente, 10 caracteres verificados] (Rachel Kushner, cita real); El cuarto de Giovanni
  [8419261874] (James Baldwin, cita de una línea del libro que ella destacó); Se acabó el pastel
  [8433981366, sin cita] (Nora Ephron); Y eso fue lo que pasó [8416011958, sin cita] (Natalia
  Ginzburg); The Family Roe [1324036079, sin ES, sin cita] (Joshua Prager); Pura pasión
  [8490667551] (Annie Ernaux, dato real: pick sugerido por la librería Shakespeare and Company);
  How to Love Your Daughter [0593539648, sin ES] (Hila Blum, cita real); Tres luces [8412664795]
  (Claire Keegan — título ES real "Tres luces", distinto del original "Foster"); Biografía de X
  [8420472107] (Catherine Lacey, sin cita); La postal [8426422853] (Anne Berest, sin cita); Olga
  muere soñando [6073911912] (Xochitl Gonzalez, sin cita); Niña, mujer, otras [8491818138]
  (Bernardine Evaristo, Booker Prize 2019, sin cita); Mujeres sin hombres [8481362689] (Shahrnush
  Parsipur, sin cita); Reunión [8433981153] (Natasha Brown, sin cita); Vladimir [1982187638, sin
  ES] (Julia May Jonas, sin cita); Fight Night [0571370733, sin ES] (Miriam Toews, sin cita).
  **25/25 con ASIN real de 10 caracteres** (0 vacíos; 1 con formato Amazon B0... en vez de ISBN
  clásico, mismo patrón ya aceptado en el catálogo para ediciones muy recientes). Verificación:
  `asin` de 10 chars OK en las 25 (chequeo manual vía Grep), `recomendadoPor: [natalie-portman]`
  OK. Spot-check de Opus: 3 fichas leídas completas (Saving Five, Vladimir, Fight Night) — citas
  reales bien atribuidas, ninguna inventada, tono y estructura correctos.
  **Listicle escrito de cero** (`libros-que-recomienda-natalie-portman.md`): 35 libros (4
  originales + 6 cross-ref + 25 nuevo) en **4 grupos temáticos** — Vínculos familiares y
  generaciones de mujeres (9), Matrimonios/deseo/lo que se rompe (7), Identidad/cuerpo/sociedad
  (6), Poder/ciencia/grandes preguntas (9) — más lead "Por dónde empezar" (4: La amiga estupenda,
  Fortuna, Niña mujer otras, ¡Mártir!). La categoría `ficcion`, dominante (25/35), se subdividió en
  4 sub-temas editoriales en vez de dejarla como un bloque único.
  **Natalie Portman: 4 → 35 libros. Catálogo: 501 → 526 libros** (501 + 25 NUEVO). **Blog: 33 → 34
  artículos.**
  **Pendiente — backlog de 17 candidatos para una futura "Profundizar Natalie Portman":**
  recientes no priorizados (7): The Vulnerables (Sigrid Nunez), Fruiting Bodies (Kathryn Harlan),
  A Sister's Story (Donatella Di Pietrantonio), Cassandra at the Wedding (Dorothy Baker), Poet
  Warrior (Joy Harjo), Something That May Shock and Discredit You (Daniel M. Lavery), Middlemarch
  (George Eliot); históricos 2019-2020 vía mostrecommendedbooks.com (10): Lost Children Archive
  (Valeria Luiselli), Royals (Emma Forrest), The Truth Will Set You Free... (Gloria Steinem), She
  Said (Jodi Kantor), Hope in the Dark (Rebecca Solnit), Becoming Ms. Burton (Susan Burton),
  Kaddish.com (Nathan Englander), Trick Mirror (Jia Tolentino), We Are the Weather (Jonathan
  Safran Foer), The Waves (Virginia Woolf). Además: el listado completo de Tertulia (46 picks,
  fuente más autorizada) quedó parcialmente sin explorar por la paginación JS — si en una futura
  sesión Claude in Chrome está conectado, vale la pena re-intentar el fetch completo para
  detectar picks intermedios (2020-2022) que ninguna de las 4 fuentes secundarias cubrió.

- **2026-08-04 — Profundizar: Adam Grant (backlog pre-sourceado, cierre completo + listicle
  nuevo).** A diferencia de Bezos/Portman, este no fue un discovery nuevo: el backlog ya estaba
  sourceado desde el 2026-07-22 en `tools/manifiesto_adam_grant.txt` (32 candidatos extraídos de
  tres posts de **Granted**, adamgrant.substack.com/p/the-new-books-to-fight-brain-rot,
  .../the-new-books-to-refresh-your-thinking y .../the-12-new-books-to-enliven-spring), y había
  quedado sin tocar por ser libros muy recientes (2025-2026) a la espera de ver si aparecían
  ediciones en español. **Reconciliación:** de los 32 candidatos, 2 ya estaban resueltos de
  sesiones previas (1929 vía cross-ref con Obama; Personas venenosas ya enriquecida) → quedaban
  **30 candidatos**. Reconciliación manual vía 30 `Glob` individuales contra `src/content/libros/`:
  **30/30 confirmados NUEVO** (0 colisiones).
  **30 NUEVO enriquecidos** vía 4 subagentes Sonnet en paralelo (tandas de 8/8/7/7), con
  advertencia reforzada de verificación (libros de 2025-2026, cerca del límite de conocimiento
  confiable): **las 30 fichas fueron verificadas como publicaciones reales** (Amazon, Goodreads,
  PenguinRandomHouse.com, Simon & Schuster, W. W. Norton — varias vía fetch directo a la página
  del publisher para confirmar ISBN/fecha exacta), 0 reportadas como "no verificado". Como es
  esperable por la recencia (la mayoría publicados entre jul-2025 y jul-2026), **ninguna** tiene
  edición en español todavía — las 30 quedan con la nota "solo inglés". 2 casos sin ISBN-10
  clásico (prefijo ISBN-13 979 o directamente sin ISBN) resolvieron con ASIN de Amazon de 10
  caracteres (`human-raised` B0GFZTD3N9, `the-power-of-beliefs` B0FBWLZ56Y); 2 casos (The Genius
  Myth, Read Your Mind) usaron el ISBN-10 de la edición UK por no tener la US un ISBN-10 clásico
  disponible. Títulos: How to Be a Living Thing [0593831667] (Mari Andrew); Finding My Way
  [1668054272] (Malala Yousafzai); Algospeak [0593804074] (Adam Aleksic); The Genius Myth
  [1787333248, ed. UK] (Helen Lewis); Read Your Mind [1915780837, ed. UK] (Oz Pearlman); Anointed
  [166800187X] (Toby Stuart); Playful [0593713400] (Cas Holman); The Balancing Act [0593850742]
  (Nedra Tawwab); Flourish [0525620702] (Daniel Coyle); Mattering [0593850599] (Jennifer Breheny
  Wallace); The Story of Stories [0063438690] (Kevin Ashton); Revealing [0593545389] (Leslie
  John); Your Best Meeting Ever [166806748X] (Rebecca Hinds); Jolted [0593655591] (Anthony Klotz
  — blurb real de Adam Grant en la contratapa); The Other Side of Change [0593713680] (Maya
  Shankar); Politics Without Politicians [0593713982, categoria filosofia] (Hélène Landemore); We
  the Women [0593727029] (Norah O'Donnell y Kate Andersen Brower); The Triangle of Power
  [1967190100] (Alexander Stubb); Human Raised [B0GFZTD3N9] (Dana Suskind); Incorruptible
  [0241692024, ed. UK] (Eric Ries); Leave the Lights On [059385327X] (Elizabeth Dunn y Jiaying
  Zhao); Inside the Box [0593715713] (David Epstein); The Power of Beliefs [B0FBWLZ56Y] (Shawn
  Achor — confirmado como libro distinto de *La felicidad como ventaja*); Why We Talk Funny
  [0593830482] (Valerie Fridland); How to Not Know [1324089458] (Simone Stolzoff); Joyful, Anyway
  [059373419X, título real con coma] (Kate Bowler); Anxietyland [1668004151, novela gráfica]
  (Gemma Correll); You've Been Pooping All Wrong [0593855132] (Trisha Pasricha); The Plunge
  [1668055864] (Chris Ballard); Walk [0306837536, ed. US] (Courtney Conley).
  **30/30 con ASIN real de 10 caracteres** (0 vacíos). Verificación: `asin` de 10 chars OK en las
  30 (chequeo vía Grep sobre las 30 fichas), `recomendadoPor: [adam-grant]` OK, 0 duplicados de
  slug con el resto del catálogo (confirmado por los 30 Glob previos a la reconciliación).
  **Listicle escrito de cero** (`libros-que-recomienda-adam-grant.md`): **36 libros** (6
  originales + 30 nuevo) — la concentración más alta de una sola categoría vista hasta ahora en el
  catálogo (`psicologia` = 21/36, 58%), subdividida en **4 sub-grupos temáticos** ("Repensar cómo
  pensamos: creatividad, cambio y certezas", "Vínculos, confianza y límites", "Jugar, criar y no
  perder la curiosidad", "Cuerpo, mente y bienestar cotidiano") en vez de un bloque único, más
  "Liderazgo, equipos y el mundo del trabajo" (negocios, 5) e "Historia, sociedad y curiosidades
  del mundo" (historia/filosofia/ciencia/memorias fusionadas, 7) — más lead "Por dónde empezar"
  (4: Piénsalo otra vez, El poder de los introvertidos, Personas venenosas, 1929). Verificación:
  36/36 enlaces con `titulo` exacto vía Grep (`### \[` = 36), `adam-grant` presente en
  `recomendadoPor` de las 30 nuevas, 0 huérfanos, 0 extras, sin links de afiliado en el post.
  **Adam Grant: 6 → 36 libros. Catálogo: 526 → 556 libros** (526 + 30 NUEVO). **Blog: 34 → 35
  artículos.** Referentes: sin cambios (44) — es "Profundizar", no alta de referente nuevo.
  **Pendiente:** ninguno formal — el manifiesto de 2026-07-22 quedó 100% procesado (32/32, contando
  los 2 ya resueltos antes). Si Grant publica una nueva tanda de recomendaciones en Granted, se
  puede repetir el ciclo con un discovery chico.

- **2026-08-08 — Acción "Sanear fichas" (sobre-recorte), 3 falsos positivos confirmados.**
  `auditar_fichas.py` flageó `lost-ocean`, `necker-a-virgin-island` y
  `obama-the-historic-presidency-of-barack-obama` por "cuerpo corto o sin '## De que trata'".
  Confirmado con `Read` (no con `bash`, por la regla del mount): en los 3 casos el cuerpo estaba
  completo (intro + atribución + descripción + "Para quién es" + nota de edición, ~250-300
  palabras), pero usaban el encabezado `## Qué es` en vez de `## De qué trata` — criterio editorial
  razonable para libros no narrativos (2 libros de fotografía + 1 libro para colorear, recomendados
  por Richard Branson), pero rompía el regex literal del audit. Fix quirúrgico con `Edit`: se
  renombró el encabezado a `## De qué trata` en los 3, sin tocar una palabra del contenido. Bump de
  `fechaActualizado` a 2026-08-08. No hace falta re-verificar contenido ni ASIN, no cambiaron.
  Pendiente: que Marcelo re-corra el audit en Windows para confirmar 0 `[FIX]` en estos 3.

- **2026-08-15 — Alta de Pedro Almodóvar, referente #46.** Pipeline completo "Nuevo referente"
  siguiendo `NUEVOS-REFERENTES.md`: bio (`autores/pedro-almodovar.md`, fuente: nota de Diario Uno
  reproducida por El Placer de la Lectura, "Las 6 novelas que Pedro Almodóvar recomienda leer una
  vez en la vida") + ámbito Entretenimiento sumado a `ambitos.ts` + verificado con `Read`.
  Manifiesto (`pedro-almodovar-manifiesto.txt`, 6 candidatos) reconciliado por el usuario antes de
  esta sesión: **0 YA-LINKED, 3 CROSS-REF (Bad Habit/La mala costumbre, Steppenwolf/El lobo
  estepario, One Hundred Years of Solitude/Cien años de soledad), 0 REVISAR, 3 NUEVO (Bonjour
  Tristesse, Hopscotch/Rayuela, 2666).**

  Fichas nuevas (MODO LIBRO, las tres verificadas como obras reales antes de escribir, ASIN de
  edición española confirmado vía `WebSearch` en amazon.es): `bonjour-tristesse.md` — *Buenos días,
  tristeza* de Sagan, asin `8483105225` (Tusquets, colección Fábula); `hopscotch.md` — *Rayuela* de
  Cortázar, asin `8437604575` (Cátedra, Letras Hispánicas); `2666.md` — *2666* de Bolaño, asin
  `8433973185` (Anagrama, Compactos). Las tres con cita textual real de Almodóvar sourceada de la
  nota (Bonjour Tristesse y La mala costumbre citadas literalmente; Rayuela como "su libro favorito
  de Cortázar" y 2666 como el libro que "relee todos los años" — ambas también citas directas según
  la fuente).

  Cross-refs (frontmatter + mención en el cuerpo, regla de atribución respetada): `bad-habit.md` —
  sumado `pedro-almodovar` a `recomendadoPor` (ahora 2: Dua Lipa + Almodóvar); sección fusionada a
  `## Por qué lo recomiendan Dua Lipa y Pedro Almodóvar`, con la cita de Almodóvar tejida en un
  segundo párrafo, como pide la regla para dos referentes con razón igual de rica.
  `steppenwolf.md` — sumado `pedro-almodovar` (ahora 2: Vargas Llosa + Almodóvar); se mantuvo la
  sección desarrollada de Vargas Llosa (razón más rica y documentada) y se cerró nombrando a
  Almodóvar, sin inventarle una cita específica para este título (la fuente no trae una).
  `one-hundred-years-of-solitude.md` — sumado `pedro-almodovar` (ahora **6 referentes**: Dua Lipa,
  Branson, Oprah, Allende, Vargas Llosa y Almodóvar — pasa a ser el libro con más consenso del
  catálogo después de *Sapiens*, y queda segundo solo en `/mas-recomendados`); Almodóvar sumado a
  la frase de cierre de la sección de Dua Lipa, junto al resto.

  Listicle nuevo `blog/libros-que-recomienda-pedro-almodovar.md`, 6 libros en lista simple sin
  grupos (bajo el umbral de 8 de MODO LISTICLE).

  **Caveat de fuente:** ni Diario Uno ni El Placer de la Lectura especifican la entrevista o fecha
  exacta en que Almodóvar hizo estas declaraciones; se sourceó tal cual la reprodujeron ambos
  medios (2025), sin poder rastrear la entrevista primaria. Mismo nivel de confiabilidad que
  "Prensa seria que reproduce la lista" en la tabla de fuentes de `NUEVOS-REFERENTES.md` §1 — no es
  la lista/club oficial del propio referente, pero sí una nota con citas directas atribuidas.

  **Pedro Almodóvar: 0 → 6 libros. Referentes: 45 → 46. Catálogo: 1.000 → 1.003 libros.
  Blog: 47 → 48. Ámbito Entretenimiento: 8 → 9 referentes. Fichas con 2+ referentes: 108 → 110.
  Vínculos libro↔referente: 1.159 → 1.165.** Archivos escritos vía el puente a la máquina de
  Marcelo (`device_commit_files`), sin mount FUSE disponible en esta sesión (Modo B) — misma
  disciplina que en la alta de del Toro (verificación con `Read`, sin `git`/`npm`).
  **Pendiente para Marcelo:** `python tools\detectar_duplicados.py src\content\libros`,
  `npm run build`, `git commit && push`, y pedir indexación en Search Console de la URL nueva del
  listicle. Próxima alta en la cola: **Andrew Huberman** (36 candidatos) → **Tyler Cowen** (10),
  ambos con manifiesto ya sourceado.

- **2026-08-15 — Alta de Guillermo del Toro, referente #45.** Pipeline completo "Nuevo referente"
  siguiendo `NUEVOS-REFERENTES.md`: bio (`autores/guillermo-del-toro.md`, fuente readthistwice.com
  vía @RealGDT + su biblioteca "Bleak House") + ámbito Entretenimiento sumado a `ambitos.ts` +
  verificado con `Read`. Manifiesto (`guillermo-del-toro-manifiesto.txt`, 26 candidatos) ya
  reconciliado por el usuario antes de esta sesión: **0 YA-LINKED, 0 CROSS-REF, 0 REVISAR, 26
  NUEVO** — no hizo falta reconciliar de nuevo ni tocar cross-refs. Las 26 fichas se enriquecieron
  vía 3 subagentes Sonnet en paralelo (tandas de 9/9/8), cada uno verificando existencia real del
  libro antes de escribir (0 quedaron sin verificar) y buscando ASIN con preferencia por edición
  española; 12 quedaron en `ficcion`, 6 en `cienciaficcion`, 5 en `historia`, 2 en `espiritualidad`,
  1 en `memorias`. Caso a notar: *A Dictionary of Symbols* es en realidad el original **español**
  de Juan Eduardo Cirlot (*Diccionario de símbolos*, Siruela) — el título en inglés del manifiesto
  es la traducción, no al revés; la ficha quedó con el título español. Dos ASIN (`making-movies`,
  `sandkings`) se derivaron matemáticamente del ISBN-13 al no aparecer el ISBN-10 impreso en la
  búsqueda — vale una segunda mirada de Marcelo antes de publicar. Validación automática (script
  local, no `auditar_fichas.py`) sobre las 26 fichas: frontmatter completo, `asin` de 10 caracteres
  o vacío, `categoria` dentro de las 9 válidas, `recomendadoPor` con `guillermo-del-toro`,
  encabezados obligatorios presentes, sin marcas `NO VERIFICADO` — 0 problemas. Listicle nuevo
  `blog/libros-que-recomienda-guillermo-del-toro.md`, 26 libros en 5 grupos temáticos (Ciencia
  ficción especulativa 6 · Vampiros, folclore y lo sagrado oscuro 6 · Fantasía y mitologías
  inventadas 4 · Terror clásico, monstruos y noir 4 · Oficio: cine, imagen y el arte de hacer
  libros 6) + lead "Por dónde empezar" (Frankenstein, Cementerio de animales, La historia
  interminable, El cine según Hitchcock). **Guillermo del Toro: 0 → 26 libros. Referentes: 44 → 45.
  Catálogo: 974 → 1.000 libros. Blog: 46 → 47. Ámbito Entretenimiento: 7 → 8 referentes.**
  Archivos escritos vía el puente a la máquina de Marcelo (`device_commit_files`), no hubo mount
  FUSE disponible en esta sesión — no aplica la restricción de bash de `CLAUDE.md`, pero se
  mantuvo la misma disciplina (verificación con `Read`, sin `git`/`npm`). **Pendiente para
  Marcelo:** `python tools\detectar_duplicados.py src\content\libros`, `npm run build`,
  `git commit && push`, pedir indexación de la URL nueva del listicle en Search Console, y
  doble-chequear en Amazon los dos ASIN derivados matemáticamente. Próxima alta en la cola:
  **Pedro Almodóvar** (6 candidatos, manifiesto listo).
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

  **7. Menú de acciones (agregado el 2026-08-15).** Para no tener que recordar el nombre exacto de
  cada acción: escribiendo **`menu acciones`** el agente muestra un menú numerado de **15 opciones**
  agrupadas (Crecer el catálogo · Publicar · Mantenimiento · Estado), ya filtrado por el estado real
  del sitio y con ★ en lo que conviene hacer hoy. Implementado en tres piezas: **`MENU.md`** en la
  raíz del repo (protocolo, formato de salida, las 15 opciones y las recetas de las 4 que no estaban
  en `ENRIQUECER.md`: Propagación, ASINs faltantes, Estado y Cola), un **skill instalable**
  (`menu-acciones.skill`) que dispara con "menu acciones" en cualquier sesión, y un puntero en
  `CLAUDE.md` como respaldo si el skill no está. `ACCIONES.md` sumó las 4 acciones nuevas a su tabla.

  **Estado al cierre de esta tanda: 974 fichas · 44 referentes · 46 posts (44 listicles + 2
  best-of) · 970 fichas con ASIN válido.** *(Nota: esta entrada se asienta fuera de orden — el alta
  de Guillermo del Toro del 2026-08-15 ya está registrada más arriba. Con del Toro el catálogo pasó
  a 1.000 fichas · 45 referentes · 47 posts.)*
  **Pendiente para Marcelo en Windows:** `python tools\detectar_duplicados.py src\content\libros`,
  `python tools\auditar_fichas.py src\content\libros src\content\autores`, `npm run build`,
  `git commit && push`, y pedir indexación en GSC del listicle de Malala y del best-of de negocios
  actualizado.

## 2026-08-16 — Alta de Andrew Huberman (referente #47)

Alta completa vía manifiesto ya sourceado (`andrew-huberman-manifiesto.txt`, 36 candidatos curados de
la lista de 47 libros de brainflow.co). Reconciliado por Marcelo con `reconciliar.py`: 13 CROSS-REF,
19 NUEVO del script + 4 REVISAR resueltos como NUEVO tras confirmar (con `Read` sobre las fichas
existentes) que son libros distintos del mismo autor, no traducciones — total real 23 NUEVO.

- **Bio + ámbito:** `autores/andrew-huberman.md` (orden 50) + `ambitos.ts` → Ciencia (pasa a 3 referentes
  en ese ámbito, el más flaco del sitio).
- **Cross-refs (13):** Behave, Sapiens, Por qué dormimos, Mindset, Maestría, La guerra del arte, Fluir,
  No me puedes lastimar, The Rise of Superman, Atrévete a no gustar, Longitud, La inmensidad del mundo,
  El acto de crear. En Behave y Por qué dormimos se desarrolló a Huberman como segundo referente (cita
  con episodio real de Huberman Lab); en el resto se sumó en la frase de cierre de la sección de
  atribución existente, respetando la regla de máximo 2 desarrollados.
- **Fichas nuevas (23):** producidas en 3 tandas vía subagente (Sonnet + WebSearch), MODO LIBRO completo.
  Ningún ASIN inventado — los 23 quedaron con ISBN-10 confirmado por WebSearch (0 vacíos). REVISAR
  resueltos: *The 4-Hour Body* (≠ *The 4-Hour Workweek*), *Deep Work* (≠ *So Good They Can't Ignore
  You*), *The Talent Code* (≠ *El código de la cultura* ni *Flourish*), *The Road to Character*
  (≠ *Cómo conocer a una persona* ni *La segunda montaña*) — los 4 son libros distintos del mismo autor,
  confirmado leyendo las fichas ya existentes antes de escribir.
- **Listicle:** `libros-que-recomienda-andrew-huberman.md`, 36 libros en 6 grupos temáticos (sueño/ritmo/
  energía · neurociencia del comportamiento · rendimiento físico y mental · mentalidad y maestría ·
  meditación y trauma · comunicación y creatividad) + lead "Por dónde empezar".

**Dudas / a confirmar por Marcelo:**
- *The Secret Pulse of Time* (Stefan Klein): ASIN tomado de la edición española "El tiempo: Los secretos
  de nuestro bien más escaso" con ~80% de confianza de que es la misma obra (el original es en alemán,
  2006 es la fecha de la edición en inglés) — vale un vistazo rápido en Amazon antes de darlo por firme.
- *Altered Traits*: editorial confirmada solo como "Penguin Random House" genérico, sin sello ni
  traductor específico.
- *The Molecule of More*, *The Circadian Code*, *Endure*, *The Talent Code*, *Finding Ultra*,
  *Hope for Cynics*, *The Nature of the Beast*, *Trauma: The Invisible Epidemic*: sin edición en español
  confirmada, quedaron con título original y ASIN de la edición inglesa.
- Varias atribuciones a Huberman no tienen cita textual puntual (se usó la fórmula honesta "aparece en
  la lista compilada por brainflow.co, sin declaración textual específica, pero temáticamente encaja");
  las que sí tienen episodio real confirmado por WebSearch: Behave, Por qué dormimos, La vida secreta
  del cerebro, Generación dopamina, Respira, El tiempo (los secretos...), Deep Work, The Nature of the
  Beast, La evolución del deseo, Hope for Cynics, Rasgos alterados, Trauma: The Invisible Epidemic,
  Rompe la barrera del no.

Catálogo pasa de 1.003 a **1.026 fichas** (23 nuevas), **47 referentes**, **49 posts** de blog.

## 2026-08-16 (continuación) — Alta de Tyler Cowen (referente #48)

Alta completa vía manifiesto ya sourceado (`tyler-cowen-manifiesto.txt`, 10 candidatos de su post
"Books which have influenced me most", marginalrevolution.com, 2010). Reconciliado por Marcelo con
`reconciliar.py`: 10 NUEVO, 0 CROSS-REF, 0 REVISAR — sin conflictos con el catálogo existente.

- **Bio + ámbito:** `autores/tyler-cowen.md` (orden 50) + `ambitos.ts` → Negocios e Inversión.
- **Fichas nuevas (10):** The Dialogues of Plato, The Incredible Bread Machine, Capitalism: The
  Unknown Ideal, Individualism and Economic Order, The General Theory of Employment Interest and
  Money, Autobiography of John Stuart Mill, Word and Object, Reasons and Persons, Sexual Personae,
  In Search of Lost Time. Escritas directamente en la sesión (sin subagente, lote chico), con
  WebSearch para cada ASIN — ninguno inventado.
- **Listicle:** `libros-que-recomienda-tyler-cowen.md`, 10 libros en 3 grupos (filosofía · economía y
  libre mercado · memoria y ficción total).

**Dudas / a confirmar por Marcelo:**
- *Individualism and Economic Order* (Hayek): no encontré una edición española de la colección
  **completa** con ISBN confirmado en Amazon — quedó con la edición inglesa (University of Chicago
  Press). Existe en español solo un ensayo suelto de esa colección ("Individualismo: el verdadero y
  el falso", Unión Editorial), que NO es el mismo libro — no lo usé para no confundir ediciones.
- *The Dialogues of Plato* y *In Search of Lost Time*: linkeados a los estuches completos (9 volúmenes
  Gredos y estuche Alianza respectivamente) en vez de a un volumen suelto, porque el ítem del
  manifiesto de Cowen refiere a la obra completa, no a un tomo. Precios de esos estuches son altos —
  vale un vistazo si conviene linkear un volumen individual más barato en su lugar.
- El propio manifiesto trae el caveat de que es una lista "intelectualmente pesada... de baja
  rotación comercial" — a diferencia de Huberman, ninguno de estos 10 títulos es un bestseller
  reciente. Vale la pena vigilar el rendimiento de estas fichas en Search Console.

Catálogo pasa de 1.026 a **1.036 fichas**, **48 referentes**, **50 posts** de blog.

## 2026-08-16 (continuación) — Best-of Ficción

Primer Best-of de la categoría más grande del catálogo: `ficcion` tenía 411 fichas (41% del total)
y era la única entre las grandes sin página hub. Curado con `python tools\armar_bestof.py ficcion`
(corrido por Marcelo), que devolvió 411 fichas enriquecidas ordenadas por consenso: 37 con 2+
referentes, 374 con 1.

- **Archivo nuevo:** `src/content/blog/mejores-libros-de-ficcion.md`.
- **24 títulos en 5 grupos:** Los más recomendados (8 — los 8 títulos con 3+ referentes: *Cien años
  de soledad* 6, *El alquimista* 4, y seis con 3: *El Hobbit*, *Fortuna*, *Grandes esperanzas*, *La
  Biblia envenenada*, *La carretera*, *Un matrimonio americano*) · Clásicos rusos y europeos (5:
  *Anna Karénina*, *Crimen y castigo*, *La Ilíada*, *Lolita*, *El corazón de las tinieblas*) ·
  Clásicos angloamericanos del siglo XX (3: *El gran Gatsby*, *El señor de las moscas*, *Matar a un
  ruiseñor*) · Ficción contemporánea que sigue marcando la conversación (5: *Pachinko*, *El
  ferrocarril subterráneo*, *Un caballero en Moscú*, *Americanah*, *Mil soles espléndidos*) ·
  Fábulas y viajes interiores (3: *El principito*, *Siddhartha*, *Ficciones*).
- **Criterio de curaduría:** los 8 títulos con 3+ referentes entraron todos. Del resto (29 con
  2 referentes) elegí 16 priorizando diversidad de subgénero y evitando amontonar al mismo autor
  cuando ya estaba cubierto por otro título más fuerte. Quedaron afuera 13: *Al este del Edén*
  (Steinbeck), *Historia de dos ciudades* (Dickens, ya está *Grandes esperanzas*), *Las aventuras de
  Huckleberry Finn* (Twain), *Los hermanos Karamázov* (Dostoievski, ya está *Crimen y castigo*),
  *Luz de agosto* y *Mientras agonizo* (Faulkner, sin título de Faulkner en la lista final), *El
  lobo estepario* (Hesse, ya está *Siddhartha*), *La mala costumbre*, *MANIAC*, *Sobre los huesos de
  los muertos*, *Y no quedó ninguno*, *¡Mártir!* y *El pacto del agua*. Es curaduría de criterio
  editorial, no un umbral mecánico — vale que Marcelo la revise.
- Cada entrada nombra a los referentes que lo recomiendan (mismo estilo que los best-of de negocios
  y psicología), sin links de afiliado en el cuerpo, cerrando a `/categorias/ficcion` y `/referentes`.
- **Sin comando de cierre específico** más allá del general (`npm run build` + commit/push). Falta
  pedir indexación en Search Console de la URL nueva y enlazarlo desde `/categorias/ficcion` — queda
  anotado en `ESTADO-CONTENIDO.md` junto con el resto de los enlaces pendientes.

Catálogo sin cambios de fichas: **1.036 fichas**, **48 referentes**, **51 posts** de blog (50 → 51).

## 2026-08-16 (continuación) — Discovery Elon Musk

Primera pasada real de sourcing para Elon Musk, que estaba como "semilla sin discovery real" (7
libros cargados, sin fuente documentada más allá de "sus redes y entrevistas"). No se tocó el
catálogo — solo se generó el manifiesto.

- **Fuentes fetcheadas:** `readthistwice.com/person/elon-musk` (compilado "51 books Elon Musk
  recommended"; 10 de esos con tweet propio y fecha) y `ejorgenson.com/blog/elons-recommended-reading`
  (lista temática de Eric Jorgenson, cruzada para sumar los candidatos que RTT no traía: historia
  militar/romana, un par de ciencia y *Liftoff*, el libro de Eric Berger sobre los primeros años de
  SpaceX que Musk recomienda aunque no sea autobiográfico).
- **Manifiesto:** `elon-musk-manifiesto.txt`, 59 candidatos — 10 con fuente primaria puntual (tweet +
  fecha), 49 de compilaciones de terceros (RTT / Jorgenson) sin cita individual.
- **No se hizo reconciliar todavía.** Con 59 candidatos y solo 7 libros hoy en catálogo, es una "alta
  grande" — conviene reconciliar primero (`python tools\reconciliar.py elon-musk
  elon-musk-manifiesto.txt`) para separar YA-LINKED/CROSS-REF de NUEVO antes de decidir cuántos cargar
  de una (la convención del proyecto es priorizar ~20-25 y dejar el resto en backlog explícito).

Catálogo sin cambios: **1.036 fichas**, **48 referentes**, **51 posts** de blog.

## 2026-08-16 (continuación) — Alta de Elon Musk (7 → 37 libros)

Marcelo corrió `python tools\reconciliar.py elon-musk elon-musk-manifiesto.txt` sobre los 59
candidatos del discovery y pegó el resultado: **YA-LINKED=6, CROSS-REF=4, REVISAR=17, NUEVO=32**.

**Resolución de los 17 REVISAR** (títulos que el reconciliador no pudo clasificar solo, por
coincidencia parcial de título/autor con algo ya en catálogo):

- **15 → NUEVO.** Eran libros genuinamente distintos de autores prolíficos ya presentes: los 5
  restantes de *Canción de Hielo y Fuego* (Martin, solo *Juego de Tronos* contaba como posible match
  parcial), los 5 tomos restantes de Dune (Herbert), 4 novelas de la Cultura de Iain M. Banks (Banks
  ya estaba por *El jugador* — cross-ref, no estos 4), y *Steve Jobs* de Isaacson (Isaacson ya estaba
  por su *Benjamin Franklin*, que es un libro distinto).
- **1 → CROSS-REF.** *Benjamin Franklin: An American Life* (Isaacson) — coincide con la ficha que
  Paul Graham ya tenía cargada. Se sumó `elon-musk` a su `recomendadoPor`.
- **1 → NO-OP, sin acción.** *Structures: Or Why Things Don't Fall Down* (J.E. Gordon) — el
  reconciliador lo marcó REVISAR porque el autor ya existe en catálogo, pero al abrir la ficha
  (`structures-or-why-things-don-t-fall-down.md`) resultó ser exactamente el mismo libro que Musk ya
  tenía cargado desde la semilla original, con `recomendadoPor: [elon-musk]` en solitario. No era un
  cross-ref: era el mismo libro re-detectado. No se tocó.

**Priorización de los 47 NUEVO resultantes** (32 originales + 15 de REVISAR): con ese volumen se
aplicó la convención de "alta grande" — se enriquecieron **25** ahora y quedan **22** en backlog
explícito abajo. Prioridad para los 25: los 4 CROSS-REF ya cuentan aparte; de los NUEVO se priorizó
(a) todo lo sourceado con tweet propio de Musk, (b) títulos mainstream de alta demanda de búsqueda,
y (c) las sagas completas de Canción de Hielo y Fuego y Dune, para consolidar `cienciaficcion` y
`ficcion` de una sola vez en vez de dejarlas a medio completar.

**25 fichas nuevas** (subagentes en paralelo, 5 tandas de 5), todas con ASIN verificado salvo la
excepción marcada:

- *Canción de Hielo y Fuego* completa, los 5 tomos restantes (`ficcion`): *A Clash of Kings*
  [8496208354], *A Storm of Swords* [**8496208982** — ⚠️ ver caveat abajo], *A Feast for Crows*
  [8496208990], *A Dance with Dragons* [8496208583]. (*A Game of Thrones* ya estaba YA-LINKED.)
- *Dune*, saga completa restante (`cienciaficcion`): *Dune Messiah* [8466356967], *Children of Dune*
  [8466357009], *God Emperor of Dune* [8466359443], *Heretics of Dune* [8466359397], *Chapterhouse:
  Dune* [8466359451].
- La Cultura, de Iain M. Banks (`cienciaficcion`): *Consider Phlebas* [8498002990], *The Player of
  Games* ya estaba (cross-ref, ver abajo), *Use of Weapons* [8498004489], *Surface Detail*
  [sin ASIN — ver caveat].
- Otra ciencia ficción (`cienciaficcion`): *Daemon* [8489367752] de Daniel Suarez.
- Ficción contemporánea (`ficcion`): *The Fault in Our Stars* [8415594011] de John Green (Bajo la
  misma estrella).
- Ciencia (`ciencia`): *Human Compatible* [0525558616] de Stuart Russell, *The Big Picture*
  [0525954821] de Sean Carroll.
- Negocios (`negocios`): *El Capital* [8432317667] de Karl Marx, *Screw Business As Usual*
  [0753540592] de Richard Branson.
- Memorias (`memorias`): *Steve Jobs* [8499921183] de Walter Isaacson, *Liftoff* [0008445621] de
  Eric Berger.
- Historia — Will Durant, *The Story of Civilization* (`historia`), 4 tomos: *The Life of Greece*
  [1567310133], *Our Oriental Heritage* [1567310125], *The Age of Napoleon* [1567310222], *The Story
  of Civilization Vol. II: The Medieval World* [1505105749].

⚠️ **Caveats de esta tanda:**
- **`a-storm-of-swords.md`** — ASIN `8496208982` no se verificó directamente contra una página de
  producto de Amazon (a diferencia del resto de la saga, donde sí); se derivó por patrón de
  numeración de la colección. **Pendiente que Marcelo lo confirme en amazon.es antes de publicar.**
- **`surface-detail.md`** — sin edición en español confirmada en Amazon; `asin` queda vacío a
  propósito (misma convención que otras fichas solo-inglés sin ASIN localizable).

**5 cross-ref** (libros que ya estaban en catálogo por otro referente, se sumó `elon-musk` a
`recomendadoPor` y se ajustó la prosa de atribución):

- *The Player of Games* (Banks) — antes solo Zuckerberg, ahora plural. Se sumó una mención a los
  nombres de los drones de SpaceX ("Of Course I Still Love You", "Just Read the Instructions"),
  tomados de nombres de naves de la Cultura.
- *The Wealth of Nations* — antes solo Neil deGrasse Tyson, se mantuvo singular en el título de la
  sección (no se pluralizó a propósito, según precedente) y se sumó un párrafo sobre Musk citándolo
  el mismo día que tuiteó sobre *El Capital*.
- *Vida 3.0* (Tegmark) — antes Andrew Ng + Lex Fridman, se sumó una oración sobre el financiamiento
  de Musk al Future of Life Institute que Tegmark cofundó.
- *El Señor de los Anillos* — antes solo Paul Graham, ahora plural. Se sumó un párrafo sobre el
  interés compartido en mundos de escala épica (Dune, Fundación, la Cultura).
- *Benjamin Franklin: An American Life* — antes solo Paul Graham, ahora plural. Se sumó un párrafo
  sobre el paralelismo entre el pragmatismo inventivo de Franklin y los "primeros principios" de
  Musk.

**Listicle regenerado** (`libros-que-recomienda-elon-musk.md`, `fechaActualizado` 07-10 → 08-16, se
mantuvo `fecha` original 2026-07-09 por convención): de 7 libros en 3 grupos pasó a **37 libros en 8
grupos**: lead "Por dónde empezar" (Dune, De cero a uno, Fundación, Ignition!) · La saga de Dune
completa (6) · La Cultura, de Iain M. Banks (4) · Otra ciencia ficción, con una excepción a la regla
(4: Fundación, Guía del autoestopista galáctico, Daemon, Bajo la misma estrella — este último es el
único título de ficción contemporánea, se fusionó acá en vez de darle grupo propio por regla de
categoría mínima) · Fantasía épica: de Poniente a la Tierra Media (6: los 5 de Canción de Hielo y
Fuego + El Señor de los Anillos) · Ciencia e ingeniería, desde los primeros principios (6) ·
Negocios, poder y economía (4) · Historia a gran escala (4, los tomos de Durant) · Vidas que enseñan
algo (3: Steve Jobs, Benjamin Franklin, Liftoff).

**Backlog explícito — 22 ítems NUEVO que quedaron sin enriquecer** (para una futura pasada de
Profundizar), todos de menor prioridad por ser de nicho, baja demanda de búsqueda esperada, o
disponibilidad ES incierta:

- **6 novelas restantes de la Cultura de Banks:** *The State of the Art*, *Excession*,
  *Inversions*, *Look to Windward*, *Matter*, *The Hydrogen Sonata*.
- **Historia militar/romana y otros Durant/afines** sourceados por Jorgenson que no entraron en esta
  tanda (verificar títulos exactos contra `elon-musk-manifiesto.txt` antes de encarar).
- El resto de los ~16 títulos de compilaciones de terceros (RTT/Jorgenson) que no tenían tweet propio
  de Musk ni encajaban en las sagas priorizadas — quedan listados en el manifiesto original,
  sin re-copiar acá para no duplicar la fuente de verdad.

Verificación: `ls` de las 25 fichas nuevas + spot-check de formato (frontmatter completo, sección
única de atribución, blockquote de cierre) en varias; los 5 cross-ref se releyeron enteros tras la
edición — se detectó y corrigió un error propio (párrafo de atribución mal ubicado en
`the-wealth-of-nations.md`, movido a la sección correcta antes de commitear).

Catálogo pasa de 1.036 a **1.061 fichas** (+25), vínculos libro↔referente de 1.211 a **1.241** (+30:
25 nuevas + 5 cross-ref), Elon Musk pasa de 7 a **37 libros**. Referentes y posts sin cambios: **48
referentes**, **51 posts** de blog (el listicle de Musk se regeneró, no es post nuevo).

## 2026-08-21 — Best-of Ciencia

Segunda categoría grande sin página hub: `ciencia` tenía ~105 fichas (99 enriquecidas con ASIN
válido, según `python tools\armar_bestof.py ciencia` corrido por Marcelo), engordada por las altas
de Huberman y Musk. De esas 99, 17 tienen 2+ referentes (consenso) y 82 tienen 1 solo.

- **Archivo nuevo:** `src/content/blog/mejores-libros-de-ciencia.md`.
- **23 títulos en 5 grupos:** Los más recomendados (5 — *Sapiens* 8 referentes, y cuatro con 3:
  *Superinteligencia*, *Vida 3.0*, *El comienzo del infinito*, *El optimista racional*) ·
  Inteligencia artificial: promesas y riesgos (4: *Inteligencia artificial: un enfoque moderno*,
  *La ola que viene*, *Human Compatible*, *Superpotencias de la inteligencia artificial*) · Física,
  cosmos y el método científico (5: *Historia del tiempo*, *Longitud*, *A New Kind of Science*,
  *Cosmos*, *Uno, dos, tres... infinito*) · Comportamiento humano, talento y sociedad (5:
  *Compórtate*, *Los ángeles que llevamos dentro*, *La generación ansiosa*, *Homo Deus*, *Amplitud
  (Range)*) · Cuerpo, sueño y biología (4: *Por qué dormimos*, *Genoma*, *La inmensidad del mundo*,
  *Respira*).
- **Criterio de curaduría:** entraron los 17 títulos con 2+ referentes (todo el consenso
  disponible) más 6 de 1 referente (*Human Compatible*, *La ola que viene*, *Superpotencias de la
  inteligencia artificial*, *A New Kind of Science*, *Cosmos*, *Uno, dos, tres... infinito*),
  elegidos por relevancia/reconocimiento del título y para que los 5 grupos temáticos quedaran
  parejos (sin ese aporte, "Inteligencia artificial" y "Física, cosmos y método científico" hubieran
  quedado con 1-3 ítems nomás). *Amplitud (Range)* se sumó al grupo de comportamiento/sociedad
  aunque su eje temático (generalistas vs. especialistas) no es estrictamente "ciencia dura" —
  vale que Marcelo lo revise. Quedaron afuera los ~76 títulos restantes de 1 referente.
- Cada entrada nombra a los referentes que la recomiendan (mismo estilo que los otros best-of, texto
  reescrito a partir de la reseña de cada ficha, no copiado literal), sin links de afiliado en el
  cuerpo, cerrando a `/categorias/ciencia` y `/referentes`.
- Dos títulos quedan marcados "solo disponible en inglés" en su reseña (`A New Kind of Science` sin
  traducción oficial, `Human Compatible` con nota de edición Viking): se respetó tal cual figura en
  cada ficha, sin inventar edición ES.
- **Sin comando de cierre específico** más allá del general (`npm run build` + commit/push). Falta
  pedir indexación en Search Console de la URL nueva y enlazarla desde `/categorias/ciencia` —
  sumado a la lista de enlaces pendientes de `ESTADO-CONTENIDO.md` junto con los otros best-of y
  listicles recientes.

Catálogo sin cambios de fichas: **1.061 fichas**, **48 referentes**, **52 posts** de blog (51 → 52).

## 2026-08-25 — Best-of Ciencia Ficción

Tercera categoría sin página hub, y la que más creció proporcionalmente en agosto: `cienciaficcion`
pasó de 32 a 41 fichas con las altas de Guillermo del Toro y Elon Musk. `python tools\armar_bestof.py
cienciaficcion` (corrido por Marcelo) reportó **39 fichas enriquecidas** (2 excluidas por falta de
ASIN): 10 con 2+ referentes y 29 con 1 solo.

- **Archivo nuevo:** `src/content/blog/mejores-libros-de-ciencia-ficcion.md`.
- **23 títulos en 5 grupos:** Los más recomendados (5 — *1984* con 4 referentes, *Un mundo feliz*
  con 4, y tres con 3: *Dune*, *El jugador*, *Fundación*) · Distopías y mundos rotos (5: *El cuento
  de la criada*, *El poder*, *El Ministerio del Futuro*, *Cántico por Leibowitz*, *El día de los
  trífidos*) · Ciencia dura, primer contacto y supervivencia (4: *El problema de los tres cuerpos*,
  *Proyecto Hail Mary*, *El juego de Ender*, *The Moon Is a Harsh Mistress*) · Clásicos que fundaron
  el género (5: *Guía del autoestopista galáctico*, *Veinte mil leguas de viaje submarino*,
  *Planilandia*, *Parque Jurásico*, *Los reyes de la arena*) · Máquinas, mentes y ciencia ficción
  contemporánea (4: *Klara y el Sol*, *Snow Crash*, *El mar de la tranquilidad*, *Un puente sobre el
  tiempo*).
- **Criterio de curaduría:** entraron los 10 títulos con 2+ referentes (todo el consenso disponible)
  más 13 de 1 referente elegidos por reconocimiento del título y para balancear los grupos.
  Decisiones explícitas de qué quedó afuera:
  - **Saga de Dune:** entró solo el primer tomo. *El mesías de Dune*, *Hijos de Dune*, *Dios
    emperador de Dune*, *Herejes de Dune* y *Casa Capitular: Dune* (todos de Musk, 1 referente) se
    dejaron afuera para no comerse el 25% del post con una sola saga; la reseña de *Dune* menciona
    que la saga completa está en el catálogo, sin linkear tomo por tomo.
  - **La Cultura de Banks:** entró *El jugador* (3 referentes). *Pensad en Flebas* y *El uso de las
    armas* (Musk) quedaron afuera por el mismo criterio.
  - **Stephenson:** entró *Snow Crash* (Naval) y quedó afuera *La era del diamante* (Thiel), para no
    repetir autor.
  - **Asimov:** entró *Fundación* (3 referentes) y quedó afuera *Trilogía de la Fundación* (Fridman),
    que es el mismo material en un volumen.
  - Otros que quedaron afuera: *Daemon*, *Dangerous Visions*, *El tapiz del vampiro*, *Las
    crisálidas*, *Los cuclillos de Midwich* (segundo Wyndham, ya estaba *El día de los trífidos*),
    *In Ascension*, *Una súper triste historia de amor verdadero*.
- **Nota de edición:** *The Moon Is a Harsh Mistress* es el único del post con `titulo` en inglés (la
  ficha lo tiene así); la reseña aclara que la edición ES —*La luna es una cruel amante*, La Factoría
  de Ideas, 2003— es difícil de conseguir. No se cambió el idioma de la ficha.
- Cada entrada nombra a los referentes que la recomiendan, con texto reescrito a partir de la reseña
  de cada ficha (no copiado literal), sin links de afiliado en el cuerpo, cerrando a
  `/categorias/cienciaficcion` y `/referentes`.
- **Validación previa al commit:** los 23 slugs existen, los 23 `titulo` y `autorLibro` del post
  coinciden **exactos** con la ficha, los 23 tienen `categoria: cienciaficcion` y ASIN de 10
  caracteres, cero links de Amazon en el cuerpo, cero slugs repetidos.
- **Sin comando de cierre específico** más allá del general (`npm run build` + commit/push). Falta
  pedir indexación en Search Console de la URL nueva y enlazarla desde `/categorias/cienciaficcion`
  — se suma a la lista de enlaces pendientes de `ESTADO-CONTENIDO.md`.

Catálogo sin cambios de fichas: **1.061 fichas**, **48 referentes**, **53 posts** de blog (52 → 53:
48 listicles + 5 best-of de categoría).

## 2026-08-25 — Enlazado interno hacia el blog (templates)

Auditoría del enlazado interno: `grep -rn "/blog" src/pages/` devolvía **una sola coincidencia** en
todo el sitio (`blog/index.astro:38`, el listado). Los 53 posts recibían links internos desde una
única página, mientras que cada post linkea a 20-25 fichas más `/categorias/<x>` y `/referentes`. El
blog era donante neto de autoridad interna. En particular, `/referentes/<slug>` no linkeaba al
listicle del propio referente y `/categorias/<slug>` no linkeaba a su best-of.

**Arreglado por template (2 archivos ⇒ 57 páginas), no post por post:**

- **`src/lib/postsRelacionados.ts` (nuevo).** Dos helpers puros: `slugListicle(referenteId)` →
  `libros-que-recomienda-<id>` y `slugBestOf(categoriaId)` → `mejores-libros-de-<id>` con un mapa de
  excepciones para los dos slugs que no siguen el patrón (`negocios` →
  `mejores-libros-de-negocios-e-inversion`, `cienciaficcion` → `mejores-libros-de-ciencia-ficcion`).
  Se eligió el mapa en `lib/` por sobre sumar un campo `categoriaRelacionada` al esquema del blog:
  cero cambios de contenido y el día que los slugs se normalicen se borra el mapa, el fallback sigue
  andando solo.
- **`src/components/EnlacePost.astro` (nuevo).** Callout con la estética de `TarjetaRecomendado`
  (chip + título + descripción del post). No decide nada: se renderiza solo si la página le pasa un
  post.
- **`src/pages/referentes/[slug].astro`.** `getStaticPaths` carga la colección `blog` una vez y le
  pasa a cada página su listicle (si existe y no es draft). Se renderiza entre la bio y el estante.
- **`src/pages/categorias/[slug].astro`.** Ídem con el best-of de la categoría, entre la descripción
  y el estante.

**Cobertura verificada antes de commitear:** 48/48 referentes matchean su listicle; 5 de las 9
categorías matchean su best-of (negocios, ciencia, ficción, psicología, ciencia ficción) y las 4 sin
best-of —historia, memorias, filosofía, espiritualidad— simplemente no renderizan el callout, sin
romper nada. Cuando se publique el best-of de alguna de esas, el link aparece solo. Ningún post del
blog queda fuera de los dos patrones.

Pendiente de esta línea de trabajo: el enlazado cruzado *dentro* del contenido (que el listicle de
Grant mencione el best-of de psicología, etc.), que sí es edición manual. Y queda abierta la opción
de linkear el best-of de la categoría desde las 1.061 fichas de libro (`libros/[slug].astro`), que
sería el mayor aporte de autoridad pero también un link boilerplate repetido en mil páginas — se
decidió no hacerlo por ahora.

Sin cambios de contenido: **1.061 fichas**, **48 referentes**, **53 posts**.
