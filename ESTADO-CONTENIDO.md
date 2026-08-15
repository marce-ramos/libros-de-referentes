# ESTADO DEL CONTENIDO — Los Imperdibles

**Corte: 2026-08-15** (actualizado tras la alta de Guillermo del Toro, referente #45). Números
contados sobre `src/content/**` (no estimados). Complementa a `PENDIENTES.md` (plan y decisiones) y
`PROGRESO.md` (bitácora append-only).

> ⚠️ **Corrección importante:** `PENDIENTES.md` venía declarando **556 libros / 35 posts**. El catálogo
> real es **974 libros / 45 posts**. La diferencia son las tandas del 06 al 10 de agosto, que se
> ejecutaron pero nunca se asentaron en los conteos. `PROGRESO.md` tampoco tiene entradas posteriores
> al 2026-08-08, así que el detalle de esas tandas (Kasparov, Paltrow, Sinek, Taleb, Neil deGrasse
> Tyson, Paul Graham, Marc Andreessen, best-of psicología) vive solo en la memoria de sesión.
> **Confianza en la reconstrucción de esas tandas: media** — los números del catálogo son exactos,
> la atribución de qué tanda sumó qué no.

---

## 1. Números gruesos

| Métrica | Valor |
| --- | --- |
| Fichas de libro | **1.000** |
| Referentes | **45** |
| Posts de blog | **47** (45 listicles de referente + 2 best-of de categoría) |
| Categorías | **9** |
| Vínculos libro↔referente | **1.159** |
| Fichas con 2+ referentes (consenso) | **108** (11%) |
| Fichas sin ASIN usable | **4** (0,4%) — eran 36 antes del saneado del 08-14 |
| Fichas sin resumen o sin `recomendadoPor` | **0** |
| Fichas marcadas "solo en inglés" | **347** (36%) |
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
| ficcion | 407 | 41% | ❌ |
| negocios | 115 | 12% | ✅ re-curado el 2026-08-14 (24 títulos, 5 grupos) |
| memorias | 107 | 11% | ❌ |
| psicologia | 102 | 10% | ✅ 2026-08-09 |
| ciencia | 87 | 9% | ❌ (candidato fuerte: Huberman lo engorda) |
| historia | 86 | 9% | ❌ |
| filosofia | 49 | 5% | ❌ |
| cienciaficcion | 32 | 3% | ❌ (del Toro sumó 6 — candidato más fuerte del catálogo) |
| espiritualidad | 15 | 2% | ❌ |

Ficción concentra 4 de cada 10 fichas —efecto Oprah (122), Reese (56), Portman (35), Jenna (31)— y no
tiene best-of. Es la categoría más grande del sitio sin página hub.

---

## 3. Distribución del consenso

| Referentes por libro | Fichas |
| --- | --- |
| 1 | 892 |
| 2 | 77 |
| 3 | 19 |
| 4 | 6 |
| 5 | 5 |
| 7 | 1 |

**Top del ranking (`/mas-recomendados`):**

1. **Sapiens** (7) — Gates, Obama, Clear, Naval, Zuckerberg, Sivers, Fridman
2. **El hombre en busca de sentido** (5) — Altman, Peterson, Sinek, Naval, Holiday
3. **Meditaciones** (5) — Holiday, Ferriss, Naval, Clear, Altman
4. **Cien años de soledad** (5) — Dua Lipa, Branson, Oprah, Allende, Vargas Llosa
5. **Pensar rápido, pensar despacio** (5) — Kahneman, Clear, Altman, Harari, Andreessen
6. **De cero a uno** (5) — Thiel, Ng, Musk, Altman, Andreessen

*(Con Almodóvar, Cien años de soledad pasa a 6 y queda segundo solo.)*

---

## 4. Referentes (45) — libros y listicle

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
| Elon Musk | Tecnología | 7 | ✅ 07-10 | Semilla, sin discovery real |
| Isabel Allende | Escritores | 6 | ✅ 07-31 | Cerrado |
| Jordan Peterson | Psicología | 5 | ✅ 07-10 | Semilla, sin discovery real |
| Tim Ferriss | Negocios | 5 | ✅ 07-10 | Semilla, sin discovery real |
| Ray Dalio | Negocios | 4 | ✅ 07-09 | Semilla, sin discovery real |
| Malala Yousafzai | Política | 3 | ✅ 08-14 | Listicle nuevo (3 libros, lista simple). Sigue sin fuente para profundizar |

**Los 45 referentes tienen listicle.**

**Ámbitos:** Tecnología 9 · Negocios e Inversión 10 · Escritores 8 · Entretenimiento 8 ·
Psicología 5 · Política y Sociedad 3 · Ciencia 2.
Ciencia con 2 referentes es el ámbito más flaco → **Huberman lo duplica**.

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

### Lo que sigue
8. **Altas nuevas** — Almodóvar (6) → Huberman (36) → Cowen (10). Ver `NUEVOS-REFERENTES.md`.
9. **Best-of nuevos:** ficción (407 fichas, la categoría más grande y sin hub) · ciencia ficción
   (del Toro la engordó a 32, ya es candidato viable) · divulgación científica (Huberman la engorda).
10. **Enlazar el best-of de psicología** desde `/categorias/psicologia` y desde los listicles de Grant y
    Clear + pedir indexación en GSC (quedó pendiente el 08-09). Ídem para el listicle de Malala, el
    best-of de negocios actualizado y el listicle nuevo de Guillermo del Toro.

### Grandes (varias sesiones)
10. **Backlogs sin cerrar:** Reese ~73 · Jenna ~55 · Natalie 17 · James Clear (131, manifiesto perdido).
11. **Semillas sin discovery real:** Musk (7), Peterson (5), Ferriss (5), Dalio (4). Son nombres de alta
    demanda con catálogo mínimo — cada uno vale un discovery propio.
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

**Con 1.000 fichas y 47 posts, el motor de contenido está muy por delante del motor de ingresos.**
El cuello de botella ya no es contenido: es tráfico + alta de afiliados.
