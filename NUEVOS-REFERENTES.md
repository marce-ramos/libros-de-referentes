# NUEVOS REFERENTES — instrucciones de ejecución

**Para quién:** una sesión **Sonnet** que va a dar de alta un referente nuevo de punta a punta.
**Qué NO es:** no reemplaza a `ENRIQUECER.md` (ahí viven MODO LIBRO / MODO REFERENTE / MODO LISTICLE
y las reglas de oro). Esto es el *runbook* del alta: el orden, la cola concreta y los errores que ya
cometimos y no queremos repetir.

Escrito el **2026-08-14** sobre el catálogo real de ese día: **974 fichas · 44 referentes ·
45 posts de blog · 9 categorías**.

---

## 0. Antes de tocar nada (3 minutos, no salteables)

1. Leé `CLAUDE.md` de la raíz del proyecto → **restricciones del mount FUSE**.
2. Leé `ENRIQUECER.md` → MODO LIBRO, MODO REFERENTE, MODO LISTICLE, regla de atribución, regla del ASIN.
3. Regla de herramientas, repetida porque es la que más se rompe:
   - **Nunca `bash`/`cat`/`grep` de shell para leer o auditar contenido.** El mount devuelve versiones
     viejas o truncadas. Usá **`Glob`, `Grep`, `Read`, `Write`, `Edit`** (tools), que leen el archivo real.
   - **Nunca `git`, `npm run build` ni los scripts de `tools/`.** Eso lo corre Marcelo en Windows y te
     pega la salida.
   - Si `Grep` sugiere un problema, **confirmalo con `Read`** antes de editar. Si `Read` muestra que
     está bien, es un falso positivo del mount.

---

## 1. Precondición innegociable: la fuente

**Sin fuente documentada y fetcheable, no se da de alta el referente.** No importa cuán obvio parezca
que "fulano recomienda X" — el modelo no *recuerda* recomendaciones, las **extrae** de una página real.

Fuentes que ya funcionaron bien, en orden de confiabilidad:

| Tipo | Ejemplo real del catálogo | Nota |
| --- | --- | --- |
| Lista/club oficial del referente | sivers.org/book (Derek Sivers), gatesnotes (Gates), ynharari.com (Harari) | La mejor: cita propia por libro |
| Newsletter propia | adamgrant.substack.com (Adam Grant) | Excelente, pero libros muy recientes → sin edición ES |
| Agregador con fuente primaria por ítem | readthistwice.com, mostrecommendedbooks.com | Buenos: cada ítem trae el tweet/entrevista de origen |
| Prensa seria que reproduce la lista | RPP (Vargas Llosa), The Week (Allende), CNBC (Buffett) | Sirve, verificar 2-3 ítems a mano |
| Listas de comunidad / fan | ⚠️ goop book club vía comunidad (Paltrow) | Usar solo con caveat explícito y verificación por ítem |

**Bandera roja:** si la fuente no permite decir *dónde* dijo el referente que le gustó ese libro,
ese ítem no entra. Es preferible un referente con 8 libros sólidos que uno con 30 dudosos.

---

## 2. Pipeline del alta (el orden importa)

### Paso 1 — Bio del referente
Creá `src/content/autores/<slug>.md` siguiendo **MODO REFERENTE**.
- `slug` = `nombre-apellido` en kebab. **Verificá la ortografía dos veces** (ver §6, caso Gladwell).
- Si el nombre completo se usa habitualmente, usalo entero: el catálogo tiene
  `nassim-nicholas-taleb`, no `nassim-taleb`. **El slug del manifiesto no manda; manda el archivo.**
- `orden: 50` para todo referente nuevo (el top ~10 del marquee se decide aparte).
- Referente fallecido → **bio en pasado** (precedente: Vargas Llosa).
- La bio tiene que nombrar la fuente verificable de sus lecturas. Sin inventar cargos actuales:
  ante la duda, framing atemporal ("fundó…", "ex-profesor de…").

### Paso 2 — Ámbito
Agregá el slug a `src/lib/ambitos.ts`, en el mapa `ambitoDe`, con uno de los 7 ámbitos existentes
(Tecnología · Negocios e Inversión · Escritores · Psicología · Entretenimiento · Política y Sociedad ·
Ciencia). **Este paso se olvidó con Dua Lipa** y quedó fuera del filtro de `/referentes` durante un mes.
Después de editar, `Read` el archivo y confirmá que tu línea está.

### Paso 3 — Manifiesto (discovery)
Si ya existe `<slug>-manifiesto.txt` en la raíz del repo → **usalo, no hagas discovery de nuevo**.
Si no, MODO DESCUBRIR: fetch de la fuente → una línea por libro:

```
Título en inglés (para match por slug)|Autor|fuente
```

Las líneas que empiezan con `#` son comentarios y `reconciliar.py` las ignora — usalas para dejar
asentada la fuente y los caveats.

### Paso 4 — Reconciliar contra el catálogo
Dos caminos, los dos válidos:
- **Script (preferido):** pedile a Marcelo que corra en Windows
  `python tools\reconciliar.py <slug> <manifiesto>.txt src\content\libros` y te pegue la salida.
- **A mano (lo que se usó en las últimas 6 altas):** un `Glob` por candidato contra
  `src/content/libros/`. Es más lento pero no depende de nadie.

Clasificación: **YA-LINKED** (nada que hacer) · **CROSS-REF** (la ficha existe, falta el referente) ·
**REVISAR** (mismo autor, título distinto → ¿traducción o libro nuevo?) · **NUEVO** (crear ficha).

⚠️ El match es por slug derivado del **título en inglés**. Casos que el script no agarra y hay que
mirar a ojo: títulos ES muy distintos del original (*Foster* → *Tres luces*), obras completas vs. un
libro suelto (*The Principia* vs *The System of the World*), y homónimos de distinto autor.

### Paso 5 — Presentar el manifiesto reconciliado **antes** de enriquecer en masa
Mostrá: cuántos YA-LINKED / CROSS-REF / REVISAR / NUEVO, y **proponé un corte**. No enriquezas 40
fichas sin confirmar. El criterio de corte, en orden:
1. Los que tienen **edición en español confirmada** (el sitio monetiza en amazon.es).
2. Los más recientes / más comentados.
3. El resto va a **backlog**, anotado en `PROGRESO.md` con los títulos, no "los que faltan".

### Paso 6 — Cross-refs
Para cada CROSS-REF: sumá el slug del referente al `recomendadoPor` de la ficha existente **y nombralo
en el cuerpo**, respetando la **regla de atribución** (una sola sección de recomendación; si ya hay dos
referentes desarrollados, el nuevo va a la frase de cierre "También lo recomiendan…").
Los cross-refs son lo más valioso del sitio: son los que suben el consenso, que es el dato diferencial
que ningún competidor tiene. Hoy solo **108 de 974 fichas (11%)** tienen 2+ referentes.

### Paso 7 — Enriquecer los NUEVO
MODO LIBRO, en **tandas de ~8 por subagente Sonnet**, 3-4 subagentes en paralelo. Recordatorios:
- **Verificá que el libro exista** antes de escribir una palabra. Si no lo confirmás, dejalo como stub
  y reportalo. Nunca inventes contenido alrededor de un título no verificado.
- **ASIN:** ISBN-10 de la edición **española** si existe; si no, la inglesa; si no lo confirmás, `asin`
  vacío (el botón cae a búsqueda). Nunca inventarlo. ASINs Amazon tipo `B0...` de 10 caracteres son
  aceptables para ediciones muy recientes (ya hay precedentes en el catálogo).
- **Antes de declarar "solo inglés"**, buscá el título traducido probable. Hoy el 36% del catálogo está
  marcado como solo-inglés: si sigue subiendo, el sitio pierde encaje con amazon.es.
- **Citas:** con comillas **solo** si hay fuente primaria. Si no, se cuenta el hecho ("lo sumó a su
  club") sin comillas. Nunca una cita inventada.
- Nota de edición al pie, siempre, en blockquote.

### Paso 8 — Listicle
MODO LISTICLE, archivo `src/content/blog/libros-que-recomienda-<slug>.md`.
- **Solo se enlazan fichas ya enriquecidas** (con `asin` o al menos cuerpo completo). Jamás un stub.
- Grupos **temáticos** balanceados, 3-6 grupos, nunca por año.
- Con 8+ libros: `## <Grupo>`. Con menos: lista simple.
- Lead `## Por dónde empezar` con 3-4 títulos en listas largas (ojo: esos títulos aparecen **dos veces**
  en el post, es esperado — no es un error de conteo).
- Cero links de afiliado. Solo internos.
- **Los libros escritos por el propio referente también van** (decisión tomada, no re-discutir).

### Paso 9 — Cierre
Ver checklist en §5.

---

## 3. Cola priorizada (al 2026-08-14)

Orden elegido: **hispanos primero**, por audiencia amazon.es y diferenciación — casi nadie cubre
referentes hispanohablantes en español.

| # | Referente | Ámbito | Manifiesto | Candidatos | Notas de ejecución |
| --- | --- | --- | --- | --- | --- |
| 1 | **Guillermo del Toro** | Entretenimiento | `guillermo-del-toro-manifiesto.txt` ✅ | 26 | Fuente Read This Twice, cada ítem con tweet de origen. Perfil terror/fantasía + oficio (cine/animación). Alimenta un futuro **best-of de ciencia ficción/terror**. Rotación comercial dispar: verificá edición ES por ficha. Ya hay `frankenstein` y `pet-sematary` en el catálogo → probables cross-ref. |
| 2 | **Pedro Almodóvar** | Entretenimiento | `pedro-almodovar-manifiesto.txt` ✅ | 6 | Alta chica y rápida, 100% hispana. *Cien años de soledad* ya está con 5 referentes → **cross-ref, sube a 6**. *Rayuela*, *2666*, *El lobo estepario* probablemente nuevos. Dos ítems con cita textual suya. Con 6 libros el listicle va **sin grupos** (umbral 8). |
| 3 | **Andrew Huberman** | Ciencia | `andrew-huberman-manifiesto.txt` ✅ | 36 | El de mayor demanda de búsqueda en español de los cuatro. Fuente: compilado brainflow.co con cita por ítem; ya se excluyeron los textbooks. Alimenta el futuro **best-of de divulgación científica**. Varios (*Behave*, *Dopamine Nation*, *Why We Sleep*) probablemente ya están → chequear cross-refs primero. |
| 4 | **Tyler Cowen** | Negocios e Inversión | `tyler-cowen-manifiesto.txt` ✅ | 10 | Lista canónica de Marginal Revolution: filosofía/economía clásica, **baja rotación comercial**. Cortito y de nicho. Si rinde poco, complementar con sus "best of the year" anuales antes de invertirle más. |
| 5 | **Malala Yousafzai** | Política y Sociedad | ❌ no existe | — | **Ya es referente del sitio con 3 libros y sin listicle.** Read This Twice vino vacío y su club (Fearless / Literati) no dio lista limpia. Necesita una pasada de sourcing dedicada a esa fuente antes de nada. Si el sourcing no rinde, la alternativa barata es escribirle el listicle con los 3-4 que tiene y cerrarlo. |

**Descartados / diferidos, no re-abrir sin motivo:**
Vitalik Buterin (SKIP: RTT solo tiene 2 recos y ya está en 8 libros) · Neil Gaiman (riesgo
reputacional) · Donald Trump (polarizante).

**Backlog de referentes nuevos sin manifiesto** (`../CONSOLIDADO_candidatos_referentes.md`):
Sarah Jessica Parker, Florence Welch, Dakota Johnson, Kaia Gerber, Camilla (Queen's Reading Room),
LeVar Burton, top 100 de David Bowie, Jimmy Fallon / Colbert. Todos son clubes o listas documentadas
→ bajo riesgo de alucinación. Las cifras de las listas Grok/Gemini **no son confiables**: sourcear
siempre desde la fuente real.

---

## 4. Cuántas fichas cargar

No hay que agotar el manifiesto. Referencia de lo que ya pasó:

- **Alta chica (≤10 candidatos):** completa de una. Ej. Almodóvar (6), Isabel Allende (6), Cowen (10).
- **Alta media (10-30):** completa, en 3-4 subagentes paralelos. Ej. Derek Sivers (23), del Toro (26).
- **Alta grande (30+):** priorizá 20-25 y dejá backlog explícito en `PROGRESO.md`.
  Ej. Natalie Portman (42 candidatos → 25 ahora + 17 backlog).

Un referente con **8-15 libros bien hechos y listicle publicado** vale más que uno con 40 fichas
flojas: el listicle es la página que rankea, y las fichas son las que convierten.

---

## 5. Checklist de cierre (Definition of Done)

Un alta no está terminada hasta que las 9 líneas dan ✅:

- [ ] `autores/<slug>.md` creado, bio real con fuente, `orden: 50`.
- [ ] Slug agregado a `src/lib/ambitos.ts` **y verificado con `Read`**.
- [ ] Cross-refs aplicados: frontmatter **y** mención en el cuerpo (regla de atribución).
- [ ] Fichas nuevas con `asin` de **10 caracteres** o vacío justificado. Ninguna inventada.
- [ ] Cada ficha nueva tiene nota de edición al pie.
- [ ] Listicle publicado, y **cada libro del `recomendadoPor` del referente aparece enlazado**.
- [ ] **Propagación:** si tocaste fichas de *otros* referentes (cross-refs), regenerá **sus** listicles.
      Este es el paso que más se olvida — hoy hay 3 listicles desfasados por esto.
- [ ] Tanda asentada en `PROGRESO.md` (append-only, con títulos y ASINs, no "se hicieron 20").
- [ ] Conteos actualizados en `PENDIENTES.md` **y** en `ESTADO-CONTENIDO.md`.

Y después, tareas de Marcelo en Windows (pedírselas explícitamente al cerrar):
`python tools\detectar_duplicados.py src\content\libros` · `npm run build` · `git commit && push` ·
pedir indexación de las URLs nuevas en Search Console.

---

## 6. Errores conocidos — no repetirlos

1. **Slug con typo.** `malcom-gladwell` (faltaba una "l") se propagó a 21 fichas, a `ambitos.ts` y a
   Google. Costó un rename + 301 en `public/_redirects`. **Verificá el slug antes de crear la segunda
   ficha**, no después de la vigésima.
2. **Olvidarse de `ambitos.ts`.** Dua Lipa (34 libros) sigue faltando ahí — arreglalo de paso.
3. **Listicle desfasado por cross-ref.** Sumar un libro a un referente que ya tiene listicle y no
   regenerarlo. Pasó con Brené Brown (4 libros afuera), Simon Sinek (2) y Ryan Holiday (1).
4. **Manifiesto en `/tmp`.** El manifiesto de Oprah se perdió por vivir sin versionar y hubo que
   re-fetchear la fuente entera. **Los manifiestos van a la raíz del repo**, versionados.
5. **Conteos "a ojo".** `PENDIENTES.md` decía 556 libros cuando el catálogo real tenía 974. Los números
   se cuentan con `Glob`, no se estiman.
6. **Reescribir fichas con `Write`.** Se pierden secciones. Correcciones = `Edit` quirúrgico, siempre.
7. **Encabezados fuera de norma.** `## Qué es` en vez de `## De qué trata` hace que el audit tire falsos
   positivos. Si un libro no es narrativo, igual usá `## De qué trata`.

---

## 7. Prompt para arrancar la sesión (copiar y pegar)

> Sos editor de contenido de **Los Imperdibles** (losimperdibles.com), el sitio de libros que
> recomiendan referentes mundiales, en español rioplatense.
>
> Tarea: **alta completa del referente `<NOMBRE>`**.
>
> Leé, en este orden: `CLAUDE.md` (restricciones del entorno), `ENRIQUECER.md` (MODO LIBRO / REFERENTE /
> LISTICLE) y `NUEVOS-REFERENTES.md` (el runbook del alta). Seguí el pipeline de §2 paso por paso y no
> cierres hasta tener las 9 líneas del checklist de §5 en ✅.
>
> Reglas duras: nunca uses `bash`, `git` ni `npm` — solo `Read`/`Write`/`Edit`/`Grep`/`Glob`. Nunca
> inventes un ASIN, una cita ni una editorial. Máximo 1-2 `WebSearch` por libro. Todo el contenido
> original, nada de parafrasear contratapas.
>
> Antes de enriquecer en masa, **pará y mostrame el manifiesto reconciliado** con tu propuesta de corte.
>
> Al terminar: asentá la tanda en `PROGRESO.md`, actualizá los conteos en `PENDIENTES.md` y
> `ESTADO-CONTENIDO.md`, y devolveme una tabla `libro | qué hiciste | ASIN | dudas` + la lista de
> comandos que tengo que correr yo en Windows.
