import { AMAZON } from "@/config";

/** Un ASIN válido de Amazon son 10 caracteres alfanuméricos. */
export function esAsinValido(asin?: string): boolean {
  return !!asin && /^[A-Z0-9]{10}$/i.test(asin);
}

/**
 * Construye la URL de afiliado de Amazon.
 *
 * - Si hay un ASIN válido -> link directo al producto (/dp/ASIN).
 * - Si no -> búsqueda en Amazon (sección Libros) con el título + autor.
 *   El sitio es en castellano, así que la búsqueda usa el título en español
 *   para que el lector caiga en la edición correcta. Esto es un fallback
 *   seguro: siempre funciona, siempre lleva tu tag, nunca queda roto.
 *   Reemplazá por el ASIN real (manual o vía PA-API) para maximizar conversión.
 *
 * Con OneLink activo, Amazon reescribe estos links a la tienda local del
 * visitante (.es, .com.mx, etc.), donde las ediciones en español son nativas.
 */
export function urlAfiliado(asin?: string, queryEsBusqueda?: string): string {
  if (esAsinValido(asin)) {
    const params = new URLSearchParams({ tag: AMAZON.tag });
    return `https://${AMAZON.storeHost}/dp/${asin}?${params.toString()}`;
  }
  // Fallback: búsqueda dentro de Libros. La query usa el título tal como está
  // en el sitio (en español si hay edición en español, en inglés si no la hay),
  // así el lector cae en la edición correcta sin forzar un idioma equivocado.
  const params = new URLSearchParams({
    k: (queryEsBusqueda ?? "").trim(),
    i: "stripbooks",
    tag: AMAZON.tag,
  });
  return `https://${AMAZON.storeHost}/s?${params.toString()}`;
}

/**
 * Link a la edición Kindle: búsqueda dentro de la tienda Kindle (acceso inmediato).
 * En amazon.es los eBooks Kindle DE PAGO sí comisionan (7%, misma banda que el libro físico);
 * la excepción es promocionar principalmente eBooks Kindle GRATIS (regla anti-spam de Amazon).
 * Aun así, el motor principal sigue siendo el libro físico + los bounties de Audible /
 * Kindle Unlimited; este link es sobre todo conveniencia para el lector y siembra la cookie de 24 h.
 */
export function urlKindle(query: string): string {
  const params = new URLSearchParams({
    k: query,
    i: "digital-text", // índice de la tienda Kindle
    tag: AMAZON.tag,
  });
  return `https://${AMAZON.storeHost}/s?${params.toString()}`;
}

/**
 * Atributos rel recomendados para links de afiliado:
 * - "sponsored": señala a Google que es un enlace pago (obligatorio).
 * - "nofollow": no transfiere autoridad.
 * - "noopener": seguridad al abrir en nueva pestaña.
 */
export const REL_AFILIADO = "sponsored nofollow noopener";
