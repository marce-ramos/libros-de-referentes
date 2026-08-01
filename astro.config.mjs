// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

// IMPORTANT: cambiá `site` por tu dominio real cuando lo tengas.
// Se usa para generar URLs absolutas en el sitemap, canónicas y Open Graph.
export default defineConfig({
  site: "https://losimperdibles.com",
  // URLs canónicas SIN barra final, consistentes con lo que sirve Cloudflare Pages.
  // Evita que la misma página cuente como dos URLs (/x y /x/) y fragmente el ranking en GSC.
  // Genera archivos planos (/referentes/bill-gates.html). Validado en preview (2026-07-19):
  // sin-barra 200 directo, con-barra 308 en un solo salto, índices OK.
  trailingSlash: "never",
  build: { format: "file" },
  // El sitemap se serializa quitando ".html" de cada URL: con build.format:'file'
  // las rutas generadas terminan en .html, y queremos publicar en el sitemap las
  // URLs limpias (sin .html ni barra) que son las canónicas reales.
  integrations: [
    sitemap({
      serialize(item) {
        item.url = item.url.replace(/index\.html$/, "").replace(/\.html$/, "");
        return item;
      },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  // Output estático (SSG) -> ideal para SEO y deploy en Cloudflare Pages.
  output: "static",
});
