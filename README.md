# Libros de Referentes — Scaffold Astro

Sitio de recomendaciones de libros de referentes mundiales (Gates, Obama, Buffett…) con enlaces de afiliado de Amazon. Construido con **Astro 5** (SSG) + **Tailwind v4**, pensado para desplegar gratis en **Cloudflare Pages**.

## Requisitos

- Node.js 18.20+ o 20.3+ (recomendado: Node 20 LTS o superior)

## Arranque rápido

```bash
cd sitio-libros
npm install
npm run dev      # http://localhost:4321
```

Otros comandos:

```bash
npm run build    # genera el sitio estático en dist/
npm run preview  # sirve el build de producción localmente
```

## Qué configurar antes de publicar

1. **`src/config.ts`** — nombre del sitio, dominio (`SITE.url`) y tu **tag de afiliado** de Amazon (`AMAZON.tag`). El tag de ejemplo es `turef-20`.
2. **`astro.config.mjs`** — el campo `site` debe coincidir con tu dominio real (se usa para sitemap, canónicas y Open Graph).
3. **`public/robots.txt`** — actualizá la URL del sitemap con tu dominio.
4. **`src/components/BloqueAudible.astro`** — pegá tu link de bounty de Audible.

## Estructura

```
src/
├── config.ts              # Config central (sitio + afiliados)
├── content.config.ts      # Esquemas de Content Collections (tipados)
├── content/
│   ├── autores/           # 1 archivo .md por referente
│   ├── libros/            # 1 archivo .md por libro
│   ├── categorias/        # 1 archivo .md por categoría
│   └── blog/              # artículos editoriales (SEO de cola larga)
├── layouts/BaseLayout.astro
├── components/            # Seo, BotonAfiliado, BloqueAudible, CardLibro
├── lib/                   # amazon.ts (links) · schema.ts (JSON-LD)
└── pages/                 # rutas: /, /autores, /libros, /categorias, /blog
```

## Cómo agregar contenido

- **Nuevo referente:** creá `src/content/autores/nombre-apellido.md` con su frontmatter.
- **Nuevo libro:** creá `src/content/libros/slug.md`. En `recomendadoPor` poné los IDs de los autores (el nombre de archivo sin `.md`) y en `categoria` el ID de la categoría. La relación muchos-a-muchos genera el interlinking automático.
- **Nuevo artículo:** creá `src/content/blog/slug.md`.

Las páginas (autor, libro, categoría) se generan solas a partir del contenido. No hace falta tocar código para sumar contenido.

## SEO incluido de fábrica

- Sitemap automático (`@astrojs/sitemap`), `robots.txt`, canónicas y Open Graph.
- Datos estructurados JSON-LD: `Book`, `Review`/`ItemList`, `BreadcrumbList`, `Article`, `WebSite`.
- HTML estático con cero JS por defecto → Core Web Vitals en verde.
- Disclosure de afiliados de Amazon en el footer (requisito de su política).
- Links de afiliado con `rel="sponsored nofollow noopener"`.

## Deploy en Cloudflare Pages

1. Subí el repo a GitHub.
2. En Cloudflare Pages: **Create project → Connect to Git**.
3. Build command: `npm run build` · Output directory: `dist`.
4. Conectá tu dominio (idealmente con el DNS ya en Cloudflare).

Cada `git push` despliega automáticamente.

## Notas importantes sobre Amazon

- **Las portadas y precios** deberían venir de la **Product Advertising API (PA-API)**, que se habilita recién tras tus **3 primeras ventas**. Las portadas de ejemplo y el fallback por ASIN son solo para desarrollo.
- **No muestres precios a mano**: contra la política de Amazon. Usá la PA-API.
- **Escribí reseñas 100% originales** (los `.md` de ejemplo traen placeholders): es requisito de Amazon 2026 y evita penalizaciones de contenido duplicado en Google.
