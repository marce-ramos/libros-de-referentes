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
2-4 acciones que hoy conviene hacer, según las reglas de "Cómo decidir qué recomendar", y con **🐍**
las que necesitan que Marcelo corra un script antes.

**Paso 3 — Esperá.** Marcelo responde con un número (`3`), con el nombre (`Profundizar`), o con
número + parámetro (`6 Almodóvar`). **No arranques a trabajar hasta que elija.**

**Paso 4 — SEGUNDA CONFIRMACIÓN: el comando previo.** Este paso no se saltea nunca. Respondé con la
plantilla de "Formato de la confirmación": qué vas a hacer, **el comando de Python exacto que él
tiene que correr en Windows antes**, qué se regenera por propagación, y qué comandos le van a quedar
al final. Después **frenás y esperás** que te pegue la salida del script.
- Si la acción **no** lleva comando previo, escribí explícitamente **"Sin comando previo"** y pedile
  un "dale" para arrancar. Nunca lo dejes adivinando si tiene que hacer algo o no.
- Si te falta un dato (referente, categoría, slugs), pedíselo **en esa misma respuesta**, no en una
  ronda aparte.

**Paso 5 — Ejecutá** con la salida del script en mano, siguiendo la receta de `ENRIQUECER.md`, y
cerrá con el checklist que corresponda (para altas, el de `NUEVOS-REFERENTES.md` §5) más los
comandos de cierre.

**Reglas que aplican siempre, sin importar la opción:**
- **Vos no corrés los scripts.** Nada de `bash`, `git` ni `npm` — solo `Read`/`Write`/`Edit`/`Grep`/
  `Glob`. Los scripts de `tools/` los corre Marcelo en Windows, nativo, y te pega la salida.
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
   🐍 = necesita que corras un script antes    ★ = conviene hacerlo hoy

CRECER EL CATÁLOGO
 1. Nuevo referente <nombre> 🐍  Alta completa desde cero: bio + discovery + fichas + listicle.
 2. Profundizar <referente>  🐍  Suma los libros del backlog ya sourceado de un referente.
 3. Discovery <referente>        Busca más libros de un referente en su fuente real. No escribe nada.
 4. Cross-refs <referente>   🐍  Suma un referente a fichas que ya existen. Sube el consenso.
 5. Enriquecer <libros>          Convierte fichas nuevas o flojas en fichas completas.

PUBLICAR
 6. Listicle <referente>         Escribe o regenera "Los libros que recomienda X".
 7. Best-of <categoría>      🐍  Post nuevo "Mejores libros de <categoría>".
 8. Actualizar Best-of <cat> 🐍  Re-cura un best-of ya publicado contra el catálogo de hoy.
 9. Bio <referente>              Reescribe una bio genérica por una real, con fuente.

MANTENIMIENTO
10. Verificar                🐍  Duplicados, ASINs de 10 caracteres, integridad de recomendadoPor.
11. Sanear                   🐍  Corrige fichas que no cumplen las reglas de MODO LIBRO.
12. Propagación                  Busca listicles desfasados respecto del catálogo y los regenera.
13. ASINs faltantes          🐍  Completa los `asin` vacíos buscando el ISBN-10 real.

ESTADO
14. Estado                   🐍  Recuenta el catálogo y actualiza ESTADO-CONTENIDO.md.
15. Cola                         Qué manifiestos hay listos y qué backlogs quedan abiertos.

Decime un número (o el nombre) y te paso el comando que hay que correr antes.
Podés agregar el dato en la misma línea: "2 Reese".
```

Las ★ van pegadas al número, con el motivo entre paréntesis al final de la línea. Ejemplo:
` 1. ★ Nuevo referente <nombre> 🐍  ... (Almodóvar: manifiesto listo, 6 libros)`.

---

## Formato de la confirmación (Paso 4)

Cuando elige una opción, respondé exactamente con esta forma. Corta, sin adornos:

```
▶ Acción <N> · <Nombre> <parámetro>

🐍 Corré esto primero, desde la carpeta sitio-libros\ :

    python tools\reconciliar.py reese-witherspoon manifiesto-reese.txt

Pegame la salida tal cual y sigo.

Alcance: <qué voy a tocar, cuántas fichas, en cuántas tandas>
Propaga: <qué listicles se regeneran, o "nada">
Al cerrar te voy a pedir: python tools\revision_general.py · python tools\detectar_duplicados.py
```

Si no lleva comando previo:

```
▶ Acción 6 · Listicle Reese Witherspoon

Sin comando previo — armo el manifiesto leyendo el catálogo con Grep.

Alcance: <...>
Propaga: nada
Al cerrar te voy a pedir: npm run build · git commit && push
```

**Siempre en sintaxis Windows** (`python tools\script.py`, barra invertida), que es donde los corre.
Si el comando necesita un archivo que todavía no existe (un manifiesto, por ejemplo), decíselo en la
misma respuesta y ofrecé la acción que lo genera.

---

## Las 15 opciones en detalle

| # | Acción | Qué hace | 🐍 Comando PREVIO | Comando de CIERRE |
| --- | --- | --- | --- | --- |
| 1 | **Nuevo referente** | Alta completa: bio + ámbito + discovery + reconciliar + fichas + listicle | `python tools\reconciliar.py <slug> <manifiesto>.txt` (si ya hay manifiesto; si no, arranca por Discovery y el comando va después) | `revision_general.py` + `detectar_duplicados.py` |
| 2 | **Profundizar** | Suma los libros del backlog **ya sourceado**. No hace discovery nuevo | `python tools\reconciliar.py <slug> <manifiesto>.txt` | `detectar_duplicados.py` |
| 3 | **Discovery** | Extrae más libros de la fuente real del referente → manifiesto. **No escribe en el catálogo** | ninguno | ninguno (el reconciliar viene después, con la acción 2) |
| 4 | **Cross-refs** | Suma un referente al `recomendadoPor` de fichas que ya existen y lo nombra en el cuerpo | `python tools\reconciliar.py <slug> <manifiesto>.txt` — su salida CROSS-REF **es** la entrada | `revision_general.py` |
| 5 | **Enriquecer** | Ficha nueva o floja → ficha completa (reseña original + ASIN de edición ES) | ninguno (opcional `revision_general.py` para elegir cuáles) | `revision_general.py` |
| 6 | **Listicle** | Escribe o regenera el post "Los libros que recomienda X" | ninguno | ninguno |
| 7 | **Best-of** | Post nuevo "Mejores libros de \<categoría\>", ~20-25 curados por consenso | `python tools\armar_bestof.py <categoria>` | ninguno |
| 8 | **Actualizar Best-of** | Re-cura un best-of publicado contra el catálogo actual | `python tools\armar_bestof.py <categoria>` | ninguno |
| 9 | **Bio** | Bio genérica autogenerada → bio real con fuente | ninguno | ninguno |
| 10 | **Verificar** | QA del catálogo | `python tools\revision_general.py` **y** `python tools\detectar_duplicados.py src\content\libros` — **los dos son la acción**; con su salida yo interpreto y arreglo | ninguno |
| 11 | **Sanear** | Arregla fichas fuera de norma (atribución huérfana, secciones de más, sin nota de edición, sobre-recorte) | `python tools\auditar_fichas.py src\content\libros src\content\autores` — la lista `[FIX]` es la worklist | re-correr `auditar_fichas.py` hasta que dé 0 |
| 12 | **Propagación** | Regenera los listicles que quedaron cortos respecto del catálogo | ninguno (se resuelve con `Grep`) | ninguno |
| 13 | **ASINs faltantes** | Busca el ISBN-10 real de las fichas con `asin` vacío o mal formado | `python tools\revision_general.py` (reporta ASIN faltante y formato inválido) | re-correr `revision_general.py` |
| 14 | **Estado** | Recuenta todo y actualiza `ESTADO-CONTENIDO.md` | `python tools\revision_general.py` | ninguno |
| 15 | **Cola** | Muestra manifiestos sin procesar y backlogs abiertos | ninguno | ninguno |

**Cierre común a toda acción que toque archivos** (agregalo siempre al final, además de lo de la
tabla): `npm run build` y después `git add . && git commit && git push`. Y si publicaste una URL
nueva, pedir indexación en Search Console.

---

## Los 5 scripts de `tools/` — sintaxis exacta

Todos son Python 3 puro, sin dependencias, y se corren **desde la carpeta `sitio-libros\`**.

| Script | Comando | Qué devuelve |
| --- | --- | --- |
| `reconciliar.py` | `python tools\reconciliar.py <referente-slug> <manifiesto>.txt` | Clasifica cada candidato del manifiesto en **YA-LINKED** / **CROSS-REF** / **REVISAR** / **NUEVO**. El match es por slug derivado del título en inglés. El tercer argumento (`src\content\libros`) es opcional. |
| `armar_bestof.py` | `python tools\armar_bestof.py <categoria>` | Las fichas enriquecidas de esa categoría ordenadas por consenso. Es el material crudo del best-of; la curaduría la hago yo sobre esa salida. Sirve igual para crear y para actualizar. |
| `revision_general.py` | `python tools\revision_general.py` | Auditoría **estructural**: frontmatter incompleto, ASIN ausente o con formato inválido, `recomendadoPor` apuntando a autores que no existen, categorías inválidas, cuerpos sobre-recortados, referentes huérfanos. |
| `auditar_fichas.py` | `python tools\auditar_fichas.py src\content\libros src\content\autores` | Auditoría de **prosa**: referentes del pill que no están nombrados en el cuerpo y exceso de secciones "también lo recomienda". Es la worklist de Sanear. |
| `detectar_duplicados.py` | `python tools\detectar_duplicados.py src\content\libros` | `[DUP]` mismo autor+título (duplicado casi seguro) y `[REV]` autores con 2+ libros (informativo). Correr después de cada barrido. |

**`revision_general.py` vs `auditar_fichas.py`:** el primero mira los datos, el segundo mira el
texto. Se complementan; ninguno reemplaza al otro.

Si Marcelo dice que un comando falló o que no tiene Python, no improvises corriéndolo vos: seguí
con la parte que se pueda hacer sin esa salida y decile claramente qué queda sin verificar.

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
1. La worklist sale de `revision_general.py`. Si querés contarlo vos, el criterio es
   **`len(valor) == 10`**, no "existe la línea `asin:`": hay fichas con `asin: ""` y fichas sin la
   línea, y las dos cuentan como faltantes.
2. Buscá el ISBN-10 de la edición impresa. Si el `titulo` de la ficha está en español, buscá la
   edición española; si está en inglés, la inglesa — **no cambies el idioma de la ficha** para
   encajar un ASIN.
3. Editá **solo** la línea `asin` y `fechaActualizado`. Nada del cuerpo.
4. Si no lo confirmás con una fuente concreta, **dejalo vacío y reportalo**. Un ASIN inventado es
   peor que un campo vacío.
5. Ojo con los "correctos vacíos": si la nota de la ficha dice que el enlace va a la búsqueda de
   Amazon a propósito, dejalo así.

### 14 · Estado
Corré la lectura sobre la salida de `revision_general.py` y complementá con `Glob`/`Grep`: fichas,
referentes, posts, vínculos `recomendadoPor`, fichas con 2+ referentes, fichas sin ASIN válido,
distribución por categoría y libros por referente. Actualizá `ESTADO-CONTENIDO.md` con el corte de
hoy y avisá si `PENDIENTES.md` quedó desfasado.

---

## Si Marcelo pide algo que no está en el menú

Atendelo igual. El menú es un atajo, no una jaula: si pide algo razonable que no está listado,
hacelo y, si es algo que va a repetir, ofrecé sumarlo como opción nueva a este archivo — con su
comando previo, si lleva.
