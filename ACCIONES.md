# Acciones — referencia rápida

Cómo se usa: en una sesión (idealmente **Sonnet**), **nombrá la acción + el referente/categoría**.
No hace falta explicar el procedimiento: está en `ENRIQUECER.md` (Catálogo de acciones + recetas).

> **Antes de arrancar cualquier tanda:** leé `ESTADO-CONTENIDO.md` (números reales del catálogo, gaps
> abiertos y backlogs) en vez de fiarte de los conteos de `PENDIENTES.md`, que se desincronizan.
> Para un **alta de referente nuevo**, el runbook paso a paso es `NUEVOS-REFERENTES.md`.

| Comando | Qué hace (en una línea) |
| --- | --- |
| **Enriquecer** `<libros>` | Convierte fichas nuevas o stubs en fichas completas (reseña original + ASIN de edición española). |
| **Discovery** `<referente>` | Busca más libros que recomienda ese referente, desde su fuente real, y arma un manifiesto. |
| **Reconciliar** `<referente>` | Compara un manifiesto contra el catálogo: qué ya está, qué es cruce, qué revisar y qué es nuevo. |
| **Cross-refs** `<referente>` | Suma ese referente a libros que ya existen y también recomienda (sube el consenso). |
| **Profundizar** `<referente>` | Agrega los libros del backlog ya identificado de ese referente (sin volver a hacer discovery). |
| **Nuevo referente** `<nombre>` | Alta completa desde cero: bio + discovery + reconciliar + fichas + listicle. |
| **Bio** `<referente>` | Reescribe la bio genérica del referente por una real, con fuente. |
| **Listicle** `<referente>` | Escribe o actualiza el post "Los libros que recomienda X". |
| **Best-of** `<categoría>` | Escribe el post "Mejores libros de \<categoría\>". |
| **Actualizar Best-of** `<categoría>` | Re-cura un Best-of de categoría ya publicado contra el catálogo actual (on-demand): suma los nuevos que califiquen, saca los viejos, re-ordena y bumpea la fecha. |
| **Verificar** | Chequea duplicados, ASINs de 10 caracteres y consistencia del catálogo. |
| **Sanear** | Corrige fichas que no cumplen las reglas: referente del pill sin nombrar, más de 2 secciones "lo recomienda", sin nota de edición o cuerpo sobre-recortado. |

**Regla que se aplica sola a todas:** si cambian los libros de un referente que ya tiene listicle,
hay que **regenerar ese listicle**. Los **Best-of de categoría** son la excepción: no se regeneran
solos; se refrescan con **Actualizar Best-of** cuando vos querés.

Detalle completo, reglas de oro (ASIN, ediciones ES, no inventar) y qué modelo usa cada paso: **`ENRIQUECER.md`**.

## Scripts — correr en Windows (no en el sandbox)

Los scripts deterministas se corren **nativos en Windows** (Python 3, sin dependencias), desde la
carpeta `sitio-libros`. El agente no usa bash: vos corrés el script y pegás la salida.

```
# Audit de saneado (fichas a corregir)
python tools\auditar_fichas.py src\content\libros src\content\autores

# Reconciliar un manifiesto de discovery contra el catálogo
python tools\reconciliar.py <referente-slug> manifiesto.txt src\content\libros

# Detectar duplicados
python tools\detectar_duplicados.py src\content\libros
```

