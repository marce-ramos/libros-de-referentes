# Acciones — referencia rápida

Cómo se usa: en una sesión (idealmente **Sonnet**), **nombrá la acción + el referente/categoría**.
No hace falta explicar el procedimiento: está en `ENRIQUECER.md` (Catálogo de acciones + recetas).

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
| **Verificar** | Chequea duplicados, ASINs de 10 caracteres y consistencia del catálogo. |
| **Sanear** | Corrige fichas que no cumplen las reglas: referente del pill sin nombrar, más de 2 secciones "lo recomienda", sin nota de edición o cuerpo sobre-recortado. |

**Regla que se aplica sola a todas:** si cambian los libros de un referente que ya tiene listicle,
hay que **regenerar ese listicle**.

Detalle completo, reglas de oro (ASIN, ediciones ES, no inventar) y qué modelo usa cada paso: **`ENRIQUECER.md`**.
