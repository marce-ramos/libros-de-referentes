/**
 * Configuración central del sitio.
 * Cambiá estos valores y se propagan a todo el sitio (SEO, afiliados, etc.).
 */
export const SITE = {
  /** Nombre/marca del sitio. */
  name: "Los Imperdibles",
  /** Dominio con protocolo, sin barra final. Debe coincidir con `site` en astro.config.mjs. */
  url: "https://losimperdibles.com",
  /** Descripción por defecto para meta tags cuando una página no define la suya. */
  description:
    "Los imperdibles según los grandes referentes del mundo: los libros que recomiendan Bill Gates, Barack Obama, Warren Buffett y más.",
  /** Idioma del contenido. */
  lang: "es",
  /** Locale para Open Graph. */
  locale: "es_ES",
  /** Autor/editor del sitio. */
  author: "Los Imperdibles",
} as const;

/**
 * Configuración de afiliados de Amazon.
 * El `tag` es tu ID de afiliado (Store ID / Tracking ID), ej: "turef-20".
 * El `store` define a qué tienda Amazon apuntás por defecto.
 */
export const AMAZON = {
  /** Tu tag de afiliado de Amazon.com. CAMBIAR por el real al darte de alta. */
  tag: "turef-20",
  /** Host de la tienda base (Amazon.com = EE.UU., paga en USD). */
  storeHost: "www.amazon.com",
  /**
   * OneLink: si lo activás en tu panel de Amazon, pegá acá el snippet/ID.
   * Mientras esté vacío, los links apuntan a la tienda base con tu tag.
   */
  oneLinkEnabled: false,
} as const;
