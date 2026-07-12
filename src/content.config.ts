import { defineCollection, reference, z } from "astro:content";
import { glob } from "astro/loaders";

/**
 * Content Collections (Astro 5 - Content Layer API).
 * Modelo de datos del sitio. Las relaciones muchos-a-muchos entre
 * libros y autores generan el interlinking automático que premia Google.
 */

// --- AUTORES (referentes) ---
const autores = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/autores" }),
  schema: z.object({
    nombre: z.string(),
    profesion: z.string(), // ej: "Cofundador de Microsoft"
    bio: z.string(), // resumen corto para la cabecera de su página
    foto: z.string().optional(), // ruta en /public, ej: "/referentes/bill-gates.jpg"
    destacado: z.boolean().default(false), // aparece en la home
    orden: z.number().default(99), // orden de aparición
  }),
});

// --- LIBROS ---
const libros = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/libros" }),
  schema: z.object({
    titulo: z.string(),
    autorLibro: z.string(), // autor del libro (no confundir con el referente)
    // ASIN de Amazon. Opcional: si falta, el botón usa una búsqueda con tu tag
    // (fallback seguro). Reemplazá por el ASIN real (manual o vía PA-API).
    asin: z.string().optional(),
    portada: z.string().optional(), // URL de la portada (vía PA-API o manual)
    categoria: reference("categorias"),
    recomendadoPor: z.array(reference("autores")), // muchos-a-muchos
    anio: z.number().optional(), // año de publicación
    resumen: z.string(), // 1-2 frases para listados y meta description
    destacado: z.boolean().default(false),
    fechaActualizado: z.coerce.date().optional(),
  }),
});

// --- CATEGORIAS ---
const categorias = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/categorias" }),
  schema: z.object({
    nombre: z.string(),
    descripcion: z.string(),
    orden: z.number().default(99),
  }),
});

// --- BLOG (artículos editoriales / SEO de cola larga) ---
const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/blog" }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    fecha: z.coerce.date(),
    fechaActualizado: z.coerce.date().optional(),
    autor: z.string().default("Libros de Referentes"),
    imagen: z.string().optional(),
    keywords: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { autores, libros, categorias, blog };
