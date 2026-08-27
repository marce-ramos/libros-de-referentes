#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
revision_general.py — Auditoría ESTRUCTURAL del catálogo de Los Imperdibles.

Complementa a auditar_fichas.py (que mira la prosa: referente sin nombrar, secciones,
nota de edición, sobre-recorte). Este script mira la INTEGRIDAD DE DATOS, que es donde
un subagente suele meter errores silenciosos:

  1. Frontmatter completo (titulo, autorLibro, categoria, recomendadoPor, resumen).
  2. ASIN presente y con formato válido (10 caracteres alfanuméricos en mayúscula).
  3. recomendadoPor: cada slug DEBE existir como autores/<slug>.md   <-- rompe interlinking si falla.
  4. categoria: debe ser una de las categorías reales (categorias/<id>.md).
  5. recomendadoPor sin duplicados y sin vacíos.
  6. Cuerpo: al menos una sección "## ", nota de edición, y largo mínimo (sobre-recorte).
  7. Atribución: más de un encabezado "## ...recomienda/eligió..." => patrón viejo (una sola sección).
  8. Referentes huérfanos: autor sin ningún libro que lo cite.

Sin dependencias externas (solo stdlib). Correr en Windows, nativo:

    python tools\\revision_general.py

O con rutas explícitas:

    python tools\\revision_general.py src\\content\\libros src\\content\\autores src\\content\\categorias
"""

import os, re, sys

def frontmatter_and_body(text):
    """Devuelve (dict_frontmatter_crudo, cuerpo). Parse simple, sin PyYAML."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw_fm, body = parts[1], parts[2]
    fm = {}
    lines = raw_fm.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                # ¿lista YAML en las líneas siguientes?
                items = []
                j = i + 1
                while j < len(lines) and re.match(r"^\s*-\s*", lines[j]):
                    items.append(re.sub(r"^\s*-\s*", "", lines[j]).strip().strip('"').strip("'"))
                    j += 1
                if items:
                    fm[key] = items
                    i = j
                    continue
                fm[key] = ""
            else:
                fm[key] = val.strip('"').strip("'")
        i += 1
    return fm, body

def slugs_de_dir(d):
    if not os.path.isdir(d):
        return set()
    return {f[:-3] for f in os.listdir(d) if f.endswith(".md")}

def main():
    libros = sys.argv[1] if len(sys.argv) > 1 else os.path.join("src", "content", "libros")
    autores = sys.argv[2] if len(sys.argv) > 2 else os.path.join("src", "content", "autores")
    categorias = sys.argv[3] if len(sys.argv) > 3 else os.path.join("src", "content", "categorias")

    autor_slugs = slugs_de_dir(autores)
    cat_ids = slugs_de_dir(categorias)
    if not autor_slugs:
        print(f"[!] No encontré autores en {autores} — revisá la ruta.")
    if not cat_ids:
        print(f"[!] No encontré categorias en {categorias} — revisá la ruta.")

    ASIN_RE = re.compile(r"^[0-9A-Z]{10}$")
    EDICION_RE = re.compile(r"(?mi)^>\s*.*(edici|espa[nñ]|ingl)")
    # Encabezados de atribución. Se exige la FORMA del encabezado ("Por qué ... recomienda/eligió"
    # o "También lo recomienda"), no la simple presencia de la palabra: el patrón anterior
    # (".*(recomien|eligi|elige|también)") daba falsos positivos con "inteligencia" (contiene
    # "eligi"), con "no se elige" y con cualquier "también" en un título de sección.
    H2_REC_RE = re.compile(
        r"(?mi)^##\s*(?:por\s+qu[eé]\b[^\n]*\b(?:recomiend\w+|eligi[oó]|elige[n]?)\b"
        r"|tambi[eé]n\s+l[oa]s?\s+(?:recomiend\w+|eligi[oó])\b)"
    )
    REQUERIDOS = ["titulo", "autorLibro", "categoria", "recomendadoPor", "resumen"]

    problemas = {k: [] for k in [
        "frontmatter_incompleto", "asin_faltante", "asin_malformado",
        "referente_inexistente", "categoria_invalida", "recomendadopor_duplicado",
        "sin_seccion", "sin_nota_edicion", "cuerpo_corto", "doble_seccion_recomendacion",
    ]}
    referentes_usados = set()
    total = 0

    for fn in sorted(os.listdir(libros)):
        if not fn.endswith(".md"):
            continue
        total += 1
        path = os.path.join(libros, fn)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm, body = frontmatter_and_body(text)

        faltantes = [k for k in REQUERIDOS if not fm.get(k)]
        if faltantes:
            problemas["frontmatter_incompleto"].append(f"{fn}: falta {', '.join(faltantes)}")

        asin = fm.get("asin", "")
        if not asin:
            problemas["asin_faltante"].append(fn)
        elif not ASIN_RE.match(str(asin)):
            problemas["asin_malformado"].append(f"{fn}: '{asin}'")

        cat = fm.get("categoria", "")
        if cat and cat_ids and cat not in cat_ids:
            problemas["categoria_invalida"].append(f"{fn}: '{cat}'")

        rec = fm.get("recomendadoPor", [])
        if isinstance(rec, str):
            rec = [rec] if rec else []
        if len(rec) != len(set(rec)):
            problemas["recomendadopor_duplicado"].append(f"{fn}: {rec}")
        for slug in rec:
            referentes_usados.add(slug)
            if autor_slugs and slug not in autor_slugs:
                problemas["referente_inexistente"].append(f"{fn}: '{slug}'")

        if "## " not in body:
            problemas["sin_seccion"].append(fn)
        if not EDICION_RE.search(body):
            problemas["sin_nota_edicion"].append(fn)
        if len(body.strip()) < 700:
            problemas["cuerpo_corto"].append(f"{fn}: {len(body.strip())} chars")
        if len(H2_REC_RE.findall(body)) > 1:
            problemas["doble_seccion_recomendacion"].append(fn)

    huerfanos = sorted(autor_slugs - referentes_usados) if autor_slugs else []

    # ---- Reporte ----
    print("=" * 60)
    print(f"REVISIÓN GENERAL — {total} fichas de libro · {len(autor_slugs)} referentes · {len(cat_ids)} categorías")
    print("=" * 60)
    etiquetas = {
        "frontmatter_incompleto": "Frontmatter incompleto",
        "asin_faltante": "Sin ASIN (botón cae a búsqueda)",
        "asin_malformado": "ASIN con formato raro (no 10 alfanum.)",
        "referente_inexistente": "recomendadoPor apunta a un autor que NO existe (rompe interlink)",
        "categoria_invalida": "Categoría inválida",
        "recomendadopor_duplicado": "recomendadoPor con slugs duplicados",
        "sin_seccion": "Sin ninguna sección '## '",
        "sin_nota_edicion": "Sin nota de edición",
        "cuerpo_corto": "Cuerpo corto (<700 chars, posible sobre-recorte)",
        "doble_seccion_recomendacion": "Doble encabezado de recomendación (usar 1 sola sección)",
    }
    total_flags = 0
    for k, items in problemas.items():
        if items:
            total_flags += len(items)
            print(f"\n### {etiquetas[k]} — {len(items)}")
            for it in items[:60]:
                print(f"   - {it}")
            if len(items) > 60:
                print(f"   ... (+{len(items) - 60} más)")

    if huerfanos:
        print(f"\n### Referentes SIN ningún libro (revisar) — {len(huerfanos)}")
        print("   " + ", ".join(huerfanos))

    print("\n" + "=" * 60)
    if total_flags == 0 and not huerfanos:
        print("OK — 0 problemas estructurales. Catálogo limpio.")
    else:
        print(f"TOTAL: {total_flags} flags estructurales" + (f" + {len(huerfanos)} referentes huérfanos" if huerfanos else ""))
        print("(Los flags de 'nota de edición' y 'doble sección' pueden tener falsos positivos;")
        print(" confirmá con el archivo real antes de editar — mismo criterio que el mount.)")
    print("=" * 60)

if __name__ == "__main__":
    main()
