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
  /**
   * Tu tag de afiliado de amazon.es (programa BASE: España — es donde está el tráfico
   * y las ediciones en español). Los tags de España terminan en "-21".
   * CAMBIAR por el real al darte de alta en afiliados.amazon.es.
   */
  tag: "losimperdibles-21",
  /**
   * Host de la tienda base: amazon.es (España). Paga en EUR; comisión de LIBROS = 7%
   * (más que el 4,5% de EE.UU.). El programa lo opera Amazon Europe Core Sàrl (Luxemburgo),
   * así que para un no residente de España no hay carga impositiva allá (tributa en Argentina).
   */
  storeHost: "www.amazon.es",
  /**
   * OneLink: al activarlo en el panel y vincular otros programas (US, MX, etc.), redirige a
   * cada visitante a SU tienda local con el tag de esa tienda. Mientras esté en false, todos
   * los links apuntan a amazon.es con el tag de arriba (ideal porque el tráfico es español).
   */
  oneLinkEnabled: false,
} as const;
