# MENU — cómo atender `menu acciones`

**Este archivo es para vos, agente.** Marcelo escribe **`menu acciones`** (o "menú", "qué puedo
hacer", "opciones") y vos le mostrás el menú de abajo, ya filtrado por el estado real del sitio.
No hace falta que él recuerde el nombre exacto de cada acción: elige un número y vos lo guiás.

El detalle de CÓMO se ejecuta cada acción vive en `ENRIQUECER.md`. Este archivo es el mostrador.

---

## Protocolo (seguilo al pie de la letra)

**Paso 1 — Mirá el estado antes de hablar.** Leé `ESTADO-CONTENIDO.md` (números y gaps) y, si algo
parece desactualizado, contá lo real con `Glob` sobre `src/content/**`. No muestres números de
memoria: el sitio cambia todas las semanas.

**Paso 2 — Mostrá el menú** con el formato de la sección "Formato de salida". Marcá con **★** las
2-4 acciones que hoy conviene hacer, según las reglas de "Cómo decidir qué recomendar".

**Paso 3 — Esperá.** Marcelo responde con un número (`3`), con el nombre (`Profundizar`), o con
número + parámetro (`6 Almodóvar`). **No arranques a trabajar hasta que elija.**

**Paso 4 — Confirmá el alcance en 2-4 líneas antes de ejecutar:** qué vas a tocar, cuántas fichas,
qué se regenera por propagación y qué le va a quedar a él para correr en Windows. Si la acción
necesita un dato que no dio (referente, categoría, lista de slugs), pedíselo ahí — una sola vez,
no de a una pregunta por vez.

**Paso 5 — Ejecutá** siguiendo la receta de `ENRIQUECER.md`, y cerrá con el checklist que
corresponda (para altas, el de `NUEVOS-REFERENTES.md` §5).

**Reglas que aplican siempre, sin importar la opción:**
- Nada de `bash`, `git` ni `npm` — solo `Read`/`Write`/`Edit`/`Grep`/`Glob`. Los scripts de
  `tools/` los corre Marcelo en Windows y te pega la salida.
- Nunca inventar un ASIN, una cita ni una editorial.
- Si cambia la lista de libros de un referente que ya tiene listicle → **regenerar ese listicle**.
  Los best-of de categoría son la excepción: se refrescan solo cuando él lo pide.
- Al cerrar: asentar en `PROGRESO.md` y actualizar los conteos en `ESTADO-CONTENIDO.md`.

---

## Formato de salida

Una línea de estado, después el menú agrupado, después la pregunta. Nada más — no expliques el
protocolo, no repitas las reglas, no escribas preámbulo.

```
📚 Los Imperdibles — <N> fichas · <N> referentes · <N> posts · <N> fichas sin ASIN

CRECER EL CATÁLOGO
 1. Nuevo referente <nombre>    Alta completa desde cero: bio + discovery + fichas + listicle.
 2. Profundizar <referente>     Suma los libros del backlog ya sourceado de un referente.
 3. Discovery <referente>       Busca más libros de un referente en su fuente real. No escribe nada.
 4. Cross-refs <referente>      Suma un referente a fichas que ya existen. Sube el consenso.
 5. Enriquecer <libros>         Convierte fichas nuevas o flojas en fichas completas.

PUBLICAR
 6. Listicle <referente>        Escribe o regenera "Los libros que recomienda X".
 7. Best-of <categoría>         Post nuevo "Mejores libros de <categoría>".
 8. Actualizar Best-of <cat>    Re-cura un best-of ya publicado contra el catálogo de hoy.
 9. Bio <referente>             Reescribe una bio genérica por una real, con fuente.

MANTENIMIENTO
10. Verificar                   Duplicados, ASINs de 10 caracteres, integridad de recomendadoPor.
11. Sanear                      Corrige fichas que no cumplen las reglas de MODO LIBRO.
12. Propagación                 Busca listicles desfasados respecto del catálogo y los regenera.
13. ASINs faltantes             Completa los `asin` vacíos buscando el ISBN-10 real.

ESTADO
14. Estado                      Recuenta el catálogo y actualiza ESTADO-CONTENIDO.md.
15. Cola                        Qué referentes tienen manifiesto listo y qué backlogs quedan abiertos.

Decime un número (o el nombre) y lo arrancamos. Podés agregar el dato en la misma línea: "2 Reese".
```

Las ★ van pegadas al número de las opciones recomendadas, con el motivo entre paréntesis al final
de la línea. Ejemplo: ` 1. ★ Nuevo referente <nombre>   ... (Almodóvar: manifiesto listo, 6 libros)`.

---

## Las 15 opciones en detalle

Para cada una: qué hace · qué dato necesita · dónde está la receta · qué se dispara después.

| # | Acción | Qué hace | Dato que necesita | Receta | Propaga |
| --- | --- | --- | --- | --- | --- |
| 1 | **Nuevo referente** | Alta completa: bio + ámbito + discovery + reconciliar + fichas + listicle | Nombre + fuente fetcheable (o manifiesto ya en la raíz) | `NUEVOS-REFERENTES.md` | — |
| 2 | **Profundizar** | Suma los libros del backlog **ya sourceado** de un referente. No hace discovery nuevo | Referente con backlog en `PROGRESO.md` | `ENRIQUECER.md` § Profundizar | Regenera su listicle |
| 3 | **Discovery** | Encuentra más libros de un referente extrayéndolos de su fuente real → manifiesto. **No escribe en el catálogo** | Referente + su fuente | MODO DESCUBRIR | — |
| 4 | **Cross-refs** | Suma un referente al `recomendadoPor` de fichas que ya existen y lo nombra en el cuerpo | Salida CROSS-REF de un reconciliar | MODO LIBRO + regla de atribución | Regenera los listicles afectados |
| 5 | **Enriquecer** | Ficha nueva o floja → ficha completa (reseña original + ASIN de edición ES) | Slugs, o "los que consideres" | MODO LIBRO | Regenera los listicles afectados |
| 6 | **Listicle** | Escribe o regenera el post "Los libros que recomienda X" | Referente | MODO LISTICLE | — |
| 7 | **Best-of** | Post nuevo "Mejores libros de \<categoría\>", ~20-25 curados por consenso | Categoría | MODO LISTICLE (variante) | — |
| 8 | **Actualizar Best-of** | Re-cura un best-of publicado contra el catálogo actual: suma, saca, re-ordena | Categoría con best-of publicado | `ENRIQUECER.md` § Actualizar Best-of | — |
| 9 | **Bio** | Bio genérica autogenerada → bio real con fuente | Slug del referente | MODO REFERENTE | — |
| 10 | **Verificar** | Duplicados + ASIN de 10 chars + `recomendadoPor` apunta a autores que existen | — | Marcelo corre `detectar_duplicados.py` | — |
| 11 | **Sanear** | Arregla fichas fuera de norma: atribución huérfana, secciones "También lo recomienda" de más, sin nota de edición, cuerpo sobre-recortado | — | `ENRIQUECER.md` § Sanear + `auditar_fichas.py` | — |
| 12 | **Propagación** | Compara, referente por referente, su `recomendadoPor` contra los slugs enlazados en su post, y regenera los que quedaron cortos | — | Ver "Receta de Propagación" abajo | Regenera los listicles cortos |
| 13 | **ASINs faltantes** | Lista las fichas cuyo `asin` no tiene 10 caracteres y busca el ISBN-10 real de cada una | — | Ver "Receta de ASINs faltantes" abajo | — |
| 14 | **Estado** | Recuenta todo y actualiza `ESTADO-CONTENIDO.md` con el corte de hoy | — | Ver "Receta de Estado" abajo | — |
| 15 | **Cola** | Muestra qué manifiestos hay sin procesar en la raíz del repo y qué backlogs siguen abiertos | — | Leer `ESTADO-CONTENIDO.md` + `Glob` de `*-manifiesto.txt` | — |

---

## Cómo decidir qué recomendar (★)

Ordená por costo/beneficio, no por lo que sea más divertido. En este orden:

1. **Un referente sin listicle** → siempre ★. Es contenido a medio publicar.
2. **Listicles desfasados** (opción 12) → ★ si hay alguno. Son minutos de trabajo y hoy el post
   miente sobre el catálogo. **Excepción conocida:** el post de Ryan Holiday excluye a propósito sus
   propios libros y lo declara en la intro — **no es un desfasaje, no lo toques.**
3. **Manifiesto ya sourceado sin procesar** (opción 1) → ★. El trabajo caro —encontrar la fuente—
   ya está hecho; queda solo ejecutar.
4. **Fichas sin ASIN** (opción 13) → ★ si son más de ~10. Cada una es un link de afiliado que hoy
   cae a búsqueda en vez de ir al producto.
5. **Categoría grande sin best-of** (opción 7) → ★ cuando pase de ~100 fichas. Es una página hub
   que no existe.
6. **Backlogs grandes abiertos** (opción 2) → ★ solo si no hay nada de lo anterior pendiente.

Si no hay nada urgente, decilo: "no hay nada que apure — cualquiera de estas suma". Es información
útil, no un fracaso del menú.

---

## Recetas de las opciones que no están en ENRIQUECER.md

### 12 · Propagación
1. Para cada `autores/<slug>.md`, juntá con `Grep` los libros cuyo `recomendadoPor` incluye ese slug.
2. Juntá los slugs enlazados en `blog/libros-que-recomienda-<slug>.md` (patrón `](/libros/<slug>)`).
3. **Comparalo como conjuntos, no por cantidad.** Los posts con lead "Por dónde empezar" enlazan
   3-4 títulos dos veces: contar links da un número inflado y no significa nada.
4. Reportá los que tengan libros del catálogo que no están en el post, y regeneralos con MODO LISTICLE.
5. Antes de sumar un libro escrito por el propio referente, chequeá que la intro del post no declare
   que los excluye.

### 13 · ASINs faltantes
1. El criterio correcto es **`len(valor) == 10`**, no "existe la línea `asin:`". Hay fichas con
   `asin: ""` y fichas sin la línea: las dos cuentan como faltantes.
2. Buscá el ISBN-10 de la edición impresa. Si el `titulo` de la ficha está en español, buscá la
   edición española; si está en inglés, la inglesa — **no cambies el idioma de la ficha** para
   encajar un ASIN.
3. Editá **solo** la línea `asin` y `fechaActualizado`. Nada del cuerpo.
4. Si no lo confirmás con una fuente concreta, **dejalo vacío y reportalo**. Un ASIN inventado es
   peor que un campo vacío.
5. Ojo con los "correctos vacíos": si la nota de la ficha dice que el enlace va a la búsqueda de
   Amazon a propósito, dejalo así.

### 14 · Estado
Recontá con `Glob`/`Grep`: fichas, referentes, posts, vínculos `recomendadoPor`, fichas con 2+
referentes, fichas sin ASIN válido, distribución por categoría, y libros por referente. Actualizá
`ESTADO-CONTENIDO.md` con el corte de hoy y avisá si `PENDIENTES.md` quedó desfasado.

---

## Si Marcelo pide algo que no está en el menú

Atendelo igual. El menú es un atajo, no una jaula: si pide algo razonable que no está listado,
hacelo y, si es algo que va a repetir, ofrecé sumarlo como opción nueva a este archivo.
