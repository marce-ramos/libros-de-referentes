/**
 * Enlazado interno hacia el blog.
 *
 * Los posts del blog siguen dos patrones de slug derivables:
 *   - listicle de referente → `libros-que-recomienda-<slug-del-autor>`  (48/48 exactos)
 *   - best-of de categoría  → `mejores-libros-de-<id-de-categoria>`     (con 2 excepciones)
 *
 * Las excepciones viven en BESTOF_POR_CATEGORIA. Si algún día los slugs se
 * normalizan, se borra el mapa y el fallback sigue funcionando solo.
 */

/** Categorías cuyo best-of NO se llama `mejores-libros-de-<id>`. */
const BESTOF_POR_CATEGORIA: Record<string, string> = {
  negocios: "mejores-libros-de-negocios-e-inversion",
  cienciaficcion: "mejores-libros-de-ciencia-ficcion",
};

/** Slug del post best-of que le corresponde a una categoría. */
export function slugBestOf(categoriaId: string): string {
  return BESTOF_POR_CATEGORIA[categoriaId] ?? `mejores-libros-de-${categoriaId}`;
}

/** Slug del listicle que le corresponde a un referente. */
export function slugListicle(referenteId: string): string {
  return `libros-que-recomienda-${referenteId}`;
}
