// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

// IMPORTANT: cambiá `site` por tu dominio real cuando lo tengas.
// Se usa para generar URLs absolutas en el sitemap, canónicas y Open Graph.
export default defineConfig({
  site: "https://libros-de-referentes.com",
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  // Output estático (SSG) -> ideal para SEO y deploy en Cloudflare Pages.
  output: "static",
});
