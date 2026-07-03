import { SITE } from "@/config";

/**
 * Helpers para generar datos estructurados JSON-LD (Schema.org).
 * Mejoran las chances de rich snippets en Google (estrellas, imágenes, listas).
 *
 * Estos objetos se serializan con JSON.stringify dentro de un
 * <script type="application/ld+json"> en el <head> (ver BaseLayout/Seo).
 */

export function schemaBook(opts: {
  titulo: string;
  autorLibro: string;
  portada?: string;
  url: string;
  resumen: string;
}) {
  return {
    "@context": "https://schema.org",
    "@type": "Book",
    name: opts.titulo,
    author: { "@type": "Person", name: opts.autorLibro },
    ...(opts.portada ? { image: opts.portada } : {}),
    url: opts.url,
    description: opts.resumen,
  };
}

export function schemaItemList(opts: {
  nombre: string;
  items: { url: string; nombre: string }[];
}) {
  return {
    "@context": "https://schema.org",
    "@type": "ItemList",
    name: opts.nombre,
    itemListElement: opts.items.map((it, i) => ({
      "@type": "ListItem",
      position: i + 1,
      url: it.url,
      name: it.nombre,
    })),
  };
}

export function schemaBreadcrumb(items: { nombre: string; url: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((it, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: it.nombre,
      item: it.url,
    })),
  };
}

export function schemaWebSite() {
  return {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: SITE.name,
    url: SITE.url,
    description: SITE.description,
    inLanguage: SITE.lang,
  };
}
