# ESTADO DEL CONTENIDO — Los Imperdibles

**Corte: 2026-08-21** (actualizado tras el Best-of Ciencia). Números de esta sección 1 sin cambios
de fichas desde el 08-16 (el Best-of no toca el catálogo, solo agrega un post); la fila de `ciencia`
en la sección 2 se actualizó con el conteo real de `armar_bestof.py` (99 fichas enriquecidas con
ASIN, 1 excluida) y su columna de Best-of. El resto de la sección 2 y la sección 3 (consenso)
**todavía reflejan el corte del 08-15/08-16** — no se recalcularon del todo, hace falta correr
`revision_general.py` para refrescarlas. Complementa a `PENDIENTES.md` (plan y decisiones) y
`PROGRESO.md` (bitácora append-only).

> ⚠️ **Corrección importante (detectada el 2026-08-14):** `PENDIENTES.md` venía declarando **556
> libros / 35 posts** cuando el catálogo real de ese día era de **974 libros / 45 posts**. La
> diferencia son las tandas del 06 al 10 de agosto, que se
> ejecutaron pero nunca se asentaron en los conteos. `PROGRESO.md` tampoco tiene entradas posteriores
> al 2026-08-08, así que el detalle de esas tandas (Kasparov, Paltrow, Sinek, Taleb, Neil deGrasse
> Tyson, Paul Graham, Marc Andreessen, best-of psicología) vive solo en la memoria de sesión.
> **Confianza en la reconstrucción de esas tandas: media** — los números del catálogo son exactos,
> la atribución de qué tanda sumó qué no.

---

## 1. Números gruesos

| Métrica | Valor |
| --- | --- |
| Fichas de libro | **1.061** (+23 Huberman, +10 Cowen, +25 Musk) |
| Referentes | **48** |
| Posts de blog | **52** (48 listicles de referente + 4 best-of de categoría) |
| Categorías | **9** |
| Vínculos libro↔referente | **1.241** (+36 Huberman, +10 Cowen, +30 Musk: 25 nuevas + 5 cross-ref) |
| Fichas con 2+ referentes (consenso) | **124** (12%) — Cowen no sumó cross-refs, solo NUEVO; Musk sumó 5 cross-ref |
| Fichas sin ASIN usable | **5** (0,5%) — +1: `surface-detail` (Iain M. Banks, alta de Musk) sin edición ES confirmada, `asin` vacío a propósito |
| Fichas sin resumen o sin `recomendadoPor` | **0** |
| Fichas marcadas "solo en inglés" | **375** (35%) — +9 Huberman, +2 Cowen (Hayek e Incredible Bread Machine), +9 Musk (Durant x4, Big Picture, Human Compatible, Screw Business As Usual, Liftoff, Surface Detail)
| Tamaño mediano de ficha | ~2.700 bytes (≈380 palabras) |

**Lectura rápida:** el catálogo está sano —cero stubs, cero campos requeridos vacíos, 99,6% con ASIN—
pero **plano**: el 89% de las fichas tiene un solo referente. El consenso es el único dato que ningún
competidor tiene y hoy está subexplotado.

> **Ojo con el chequeo de ASIN:** el conteo "12 sin ASIN" del primer corte era erróneo porque contaba
> `asin: ""` como campo presente. El chequeo correcto es **longitud del valor = 10**, no "existe la
> línea". Con ese criterio eran 36; tras el saneado del 08-14 quedan 4.

---

## 2. Distribución por categoría

| Categoría | Fichas | % | Best-of publicado |
| --- | --- | --- | --- |
| ficcion | 411 → 417 con Musk (+5 ASOIAF, +1 Fault in Our Stars) | ~41% | ✅ 2026-08-16 (24 títulos, 5 grupos, previo al alta de Musk) |
| negocios | 115 → 117 con Musk (+El Capital, +Screw Business As Usual) | ~12% | ✅ re-curado el 2026-08-14 |
| memorias | 107 → 109 con Musk (+Steve Jobs, +Liftoff) | ~11% | ❌ |
| psicologia | 102 | 10% | ✅ 2026-08-09 |
| ciencia | 87 → ~103 con Huberman → ~105 con Musk (+Human Compatible, +The Big Picture); 99 enriquecidas con ASIN según `armar_bestof.py` | ~10% | ✅ 2026-08-21 (23 títulos, 5 grupos) |
| historia | 86 → 90 con Musk (+4 tomos de Durant) | ~9% | ❌ |
| filosofia | 49 | 5% | ❌ |
| cienciaficcion | 32 → 41 con Musk (+9: saga de Dune completa + Culture de Banks) | ~4% | ❌ (candidato mucho más fuerte del catálogo tras del Toro + Musk) |
| espiritualidad | 15 | 2% | ❌ |

Ficción concentra 4 de cada 10 fichas —efecto Oprah (122), Reese (56), Portman (35), Jenna (31)— y no
tiene best-of. Es la categoría más grande del sitio sin página hub. Ciencia ficción es la que más
creció proporcionalmente en la sesión (32 → 41, +28%) gracias a la saga de Dune y la Cultura de Banks
en la alta de Musk.

---

## 3. Distribución del consenso

| Referentes por libro | Fichas |
| --- | --- |
| 1 | 893 |
| 2 | 79 |
| 3 | 19 |
| 4 | 6 |
| 5 | 4 |
| 6 | 1 |
| 7 | 1 |

**Top del ranking (`/mas-recomendados`):**

1. **Sapiens** (7) — Gates, Obama, Clear, Naval, Zuckerberg, Sivers, Fridman
2. **Cien años de soledad** (6) — Dua Lipa, Branson, Oprah, Allende, Vargas Llosa, Almodóvar
3. **El hombre en busca de sentido** (5) — Altman, Peterson, Sinek, Naval, Holiday
4. **Meditaciones** (5) — Holiday, Ferriss, Naval, Clear, Altman
5. **Pensar rápido, pensar despacio** (5) — Kahneman, Clear, Altman, Harari, Andreessen
6. **De cero a uno** (5) — Thiel, Ng, Musk, Altman, Andreessen

---

## 4. Referentes (47) — libros y listicle

| Referente | Ámbito | Libros | Listicle | Estado |
| --- | --- | ---: | --- | --- |
| Oprah Winfrey | Entretenimiento | 122 | ✅ 07-31 | Backlog cerrado (excluidos 3 infantiles de Cosby) |
| Richard Branson | Negocios | 70 | ✅ 07-24 | Cerrado (70/70) |
| Barack Obama | Política | 61 | ✅ 07-13 | Cerrado hasta su lista de verano 2026 |
| Reese Witherspoon | Entretenimiento | 56 | ✅ 07-13 | **Backlog ~73 (2017-2022)** |
| Mario Vargas Llosa | Escritores | 46 | ✅ 07-31 | Cerrado |
| Bill Gates | Tecnología | 40 | ✅ 07-13 | Cerrado hasta su lista de verano 2026 |
| Ryan Holiday | Escritores | 39 | ✅ 08-06 | Excluye sus propios libros **por decisión declarada en la intro del post** — no es un desfasaje |
| Adam Grant | Psicología | 36 | ✅ 08-04 | Cerrado (100% del manifiesto) |
| James Clear | Escritores | 36 | ✅ 07-23 | Backlog viejo de 131 ítems nunca recuperado |
| Natalie Portman | Entretenimiento | 35 | ✅ 08-03 | **Backlog 17** + Tertulia sin fetchear del todo |
| Dua Lipa | Entretenimiento | 34 | ✅ 07-14 | `ambitos.ts` corregido el 08-14 |
| Paul Graham | Tecnología | 34 | ✅ 08-09 | Cerrado. Demanda real en GSC |
| Emma Watson | Entretenimiento | 32 | ✅ 07-24 | Cerrado |
| Marc Andreessen | Negocios | 32 | ✅ 08-07 | Cerrado (excluidos títulos políticamente cargados) |
| Jenna Bush Hager | Entretenimiento | 31 | ✅ 08-01 | **Backlog histórico ~55 (2019-2023)** |
| Derek Sivers | Negocios | 27 | ✅ 08-03 | Cerrado |
| Guillermo del Toro | Entretenimiento | 26 | ✅ 08-15 | Alta recién creada, referente #45 |
| J.K. Rowling | Escritores | 25 | ✅ 07-16 | — |
| Brené Brown | Psicología | 24 | ✅ 08-14 | Regenerado a 24, grupo nuevo "Creatividad y coraje para crear" |
| Stephen King | Escritores | 24 | ✅ 07-16 | — |
| Mark Zuckerberg | Tecnología | 23 | ✅ 07-13 | Cerrado ("A Year of Books") |
| Naval Ravikant | Negocios | 23 | ✅ 07-16 | — |
| Sam Altman | Tecnología | 22 | ✅ 07-17 | — |
| Angela Duckworth | Psicología | 21 | ✅ 07-23 | — |
| Malcolm Gladwell | Escritores | 21 | ✅ 07-17 | Slug corregido + 301 activo |
| Satya Nadella | Tecnología | 20 | ✅ 07-14 | Cerrado |
| Warren Buffett | Negocios | 18 | ✅ 07-15 | Cerrado (cartas a accionistas) |
| Jeff Bezos | Negocios | 17 | ✅ 08-03 | Cerrado |
| Lex Fridman | Tecnología | 17 | ✅ 08-08 | Cerrado |
| Simon Sinek | Negocios | 15 | ✅ 08-14 | Regenerado a 15 (sumados sus dos libros propios) |
| Gwyneth Paltrow | Entretenimiento | 14 | ✅ 08-10 | Fuente de comunidad — verificar picks |
| Neil deGrasse Tyson | Ciencia | 14 | ✅ 08-09 | *How to Lie with Statistics* sin cita primaria |
| Garry Kasparov | Política | 13 | ✅ 08-10 | Cerrado |
| Yuval Noah Harari | Escritores | 13 | ✅ 07-20 | Cerrado |
| Nassim N. Taleb | Escritores | 11 | ✅ 08-09 | Cerrado |
| Peter Thiel | Negocios | 11 | ✅ 07-23 | — |
| Andrew Ng | Tecnología | 9 | ✅ 07-22 | — |
| Daniel Kahneman | Ciencia | 9 | ✅ 07-23 | — |
| Vitalik Buterin | Tecnología | 8 | ✅ 07-22 | SKIP profundizar (fuente agotada) |
| Elon Musk | Tecnología | 37 (7 semilla + 25 nuevas + 5 cross-ref) | ✅ 08-16 (regenerado, 8 grupos temáticos) | Alta recién cerrada. Manifiesto sourceado (readthistwice.com + ejorgenson.com), 17 REVISAR resueltos (15→NUEVO, 1→CROSS-REF, 1→NO-OP ya cubierto). Backlog explícito de 22 ítems en PROGRESO.md, ASIN de `a-storm-of-swords` sin verificar directamente en Amazon |
| Isabel Allende | Escritores | 6 | ✅ 07-31 | Cerrado |
| Pedro Almodóvar | Entretenimiento | 6 | ✅ 08-15 | Alta recién creada, referente #46. 3 cross-refs (incluido Cien años de soledad, que pasa a 6 referentes) |
| Jordan Peterson | Psicología | 5 | ✅ 07-10 | Semilla, sin discovery real |
| Tim Ferriss | Negocios | 5 | ✅ 07-10 | Semilla, sin discovery real |
| Ray Dalio | Negocios | 4 | ✅ 07-09 | Semilla, sin discovery real |
| Malala Yousafzai | Política | 3 | ✅ 08-14 | Listicle nuevo (3 libros, lista simple). Sigue sin fuente para profundizar |
| Andrew Huberman | Ciencia | 36 (13 cross-ref + 23 nuevas) | ✅ 08-16 | Alta recién creada, referente #47. Manifiesto ya sourceado (brainflow.co), 4 REVISAR resueltos como NUEVO (libros distintos de autores ya en catálogo) |
| Tyler Cowen | Negocios e Inversión | 10 (10 nuevas, 0 cross-ref) | ✅ 08-16 | Alta recién creada, referente #48. Manifiesto ya sourceado ("Books which have influenced me most", 2010), lista de baja rotación comercial por diseño (filosofía/economía clásica) |

**Los 48 referentes tienen listicle.**

**Ámbitos:** Tecnología 9 · Negocios e Inversión 11 · Escritores 8 · Entretenimiento 9 ·
Psicología 5 · Política y Sociedad 3 · Ciencia 3.
Ciencia sigue siendo el ámbito más flaco (3 referentes) tras la alta de Huberman; Negocios e
Inversión pasa a ser el más grande (11) con la alta de Cowen.

---

## 5. Gaps abiertos, por costo/beneficio

### ✅ Hechos el 2026-08-14
1. ~~**Dua Lipa en `ambitos.ts`**~~ — agregada bajo Entretenimiento.
2. ~~**Regenerar listicles desfasados**~~ — Brené Brown 20 → 24, Simon Sinek 13 → 15. **Ryan Holiday
   no se tocó a propósito:** la intro de su post declara que excluye sus propios libros, así que
   *El obstáculo es el camino* está bien afuera.
3. ~~**Listicle de Malala**~~ — publicado con sus 3 libros, lista simple. Blog 45 → 46.
4. ~~**Fichas sin ASIN**~~ — eran **36** (no 12) con el criterio correcto; **31 resueltos**, quedan 4:
   `a-history-of-medieval-europe` (la autoría de la ficha no coincide con la de Amazon: dice John H.
   Mundy, Amazon lo atribuye a R.H.C. Davis — **hay que resolver eso primero**), `dare-to-lead` y
   `in-defense-of-food` (no se confirmó ISBN-10 de la edición española) y `the-planiverse`
   (**correcto que quede vacío**: la nota de la ficha manda a la búsqueda de Amazon a propósito).
5. ~~**Sincronizar `PROGRESO.md`**~~ — asentadas las tandas 08-06 → 08-10 y esta sesión.
6. ~~**Actualizar Best-of Negocios**~~ — re-curado contra las 112 fichas de negocios con ASIN:
   24 títulos en 5 grupos, 9 sumados, 2 sacados.

### ✅ Hecho el 2026-08-15
7. ~~**Alta de Guillermo del Toro**~~ — referente #45, 26 libros + bio + listicle. Detalle en
   PROGRESO.md. Dos ASIN derivados matemáticamente (`making-movies`, `sandkings`) — pendiente que
   Marcelo los confirme en Amazon antes de darlos por definitivos.
8. ~~**Alta de Pedro Almodóvar**~~ — referente #46, 6 libros (3 nuevos + 3 cross-refs) + bio +
   listicle. *Cien años de soledad* pasa a 6 referentes. Detalle en PROGRESO.md. Caveat de fuente:
   Diario Uno / El Placer de la Lectura no especifican la entrevista original de Almodóvar.

### ✅ Hecho el 2026-08-16
9. ~~**Alta de Andrew Huberman**~~ — referente #47, 36 libros (13 cross-ref + 23 nuevos) + bio +
   ámbito Ciencia + listicle en 6 grupos temáticos. Detalle y dudas abiertas en `PROGRESO.md`.
10. ~~**Alta de Tyler Cowen**~~ — referente #48, 10 libros (todos NUEVO) + bio + ámbito Negocios e
    Inversión + listicle en 3 grupos. Ojo: *Individualism and Economic Order* de Hayek quedó sin
    edición ES confirmada en Amazon — detalle en `PROGRESO.md`.
11. ~~**Best-of Ficción**~~ — primer hub de la categoría más grande del catálogo (411 fichas, 41%):
    24 títulos en 5 grupos, curados con `armar_bestof.py ficcion` sobre 37 fichas con 2+ referentes.
    Detalle de qué quedó afuera y por qué en `PROGRESO.md`.
12. ~~**Discovery + alta de Elon Musk**~~ — de 7 a 37 libros (25 nuevas fichas + 5 cross-ref),
    listicle regenerado en 8 grupos temáticos. Backlog explícito de 22 ítems (Culture de Banks
    restante, títulos de baja disponibilidad ES) y ASIN de `a-storm-of-swords` pendiente de
    verificación manual — ambos detallados en `PROGRESO.md`.

### ✅ Hecho el 2026-08-21
13. ~~**Best-of Ciencia**~~ — segunda categoría grande (99 fichas enriquecidas de ~105) sin página
    hub: 23 títulos en 5 grupos, curados con `armar_bestof.py ciencia` (17 con 2+ referentes + 6 de
    1 referente elegidos por relevancia). Detalle de la curaduría en `PROGRESO.md`.

### Lo que sigue
14. **Best-of nuevos:** ciencia ficción (del Toro + Musk la engordaron a 41, candidato fuerte ya).
15. **Enlazar el best-of de psicología** desde `/categorias/psicologia` y desde los listicles de Grant y
    Clear + pedir indexación en GSC (quedó pendiente el 08-09). Ídem para el listicle de Malala, el
    best-of de negocios actualizado, el Best-of Ficción, el Best-of Ciencia recién publicado, y los
    listicles nuevos de Guillermo del Toro, Pedro Almodóvar, Andrew Huberman y Elon Musk (regenerado).

### Grandes (varias sesiones)
10. **Backlogs sin cerrar:** Reese ~73 · Jenna ~55 · Natalie 17 · James Clear (131, manifiesto perdido).
11. **Semillas sin discovery real:** Peterson (5), Ferriss (5), Dalio (4). Musk ya salió de esta lista
    (discovery hecho el 08-16, 7→37). Son nombres de alta demanda con catálogo mínimo — cada uno vale
    un discovery propio.
12. **Fotos de referentes** (Wikimedia CC) + página de créditos.

---

## 6. Riesgos de contenido a vigilar

- **36% del catálogo es solo-inglés.** El sitio monetiza en amazon.es y vende ediciones en español;
  cada tanda de libros muy recientes (Adam Grant: 30/30 sin edición ES) empuja ese número para arriba.
  Vale la pena revisar cada 3-4 meses si aparecieron traducciones de los marcados como solo-inglés.
- **Fuentes de comunidad:** Gwyneth Paltrow (goop) se cargó con caveat. Si alguna vez se cuestiona una
  atribución, esa es la primera a auditar.
- **Atribuciones sin cita primaria:** quedaron marcadas explícitamente en ficha (8 de Brené Brown,
  *How to Lie with Statistics* de Tyson). Está bien resuelto, pero es deuda editorial.
- **Deriva de la documentación.** Es la segunda vez que los conteos de `PENDIENTES.md` quedan lejos de
  la realidad. Regla: los números se actualizan **en la misma sesión** que se cargan las fichas.

---

## 7. Estado de monetización (contexto, no contenido)

- Alta en **afiliados.amazon.es**: ❌ pendiente. El tag `losimperdibles-21` en `src/config.ts` es
  **placeholder**. Ningún link genera comisión hoy.
- Comisión libros amazon.es: **7%** (físico y Kindle de pago).
- Regla del programa: **3 ventas en 180 días** o cierran la cuenta → conviene darse de alta con algo
  de tráfico ya corriendo.
- PA-API (portadas y precios reales): se habilita recién tras esas 3 ventas.
- Cobro desde Argentina: Takenos (0%) / Belo (0,5%); a volumen, Wallbit + Factura E.

**Con 1.061 fichas y 51 posts, el motor de contenido está muy por delante del motor de ingresos.**
El cuello de botella ya no es contenido: es tráfico + alta de afiliados.
