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
  // Genera archivos planos (/referentes/bill-gates.html). PROBAR en un preview de Cloudflare
  // antes de mergear a producción (ojo con las páginas índice).
  trailingSlash: "never",
  build: { format: "file" },
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  // Output estático (SSG) -> ideal para SEO y deploy en Cloudflare Pages.
  output: "static",
});
