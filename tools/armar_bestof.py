#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
armar_bestof.py — Arma el "material crudo" para un Best-of de categoría.

Dada una categoría, lista sus fichas ENRIQUECIDAS (con asin) ordenadas por consenso
(cantidad de referentes en recomendadoPor). Esa salida es la base desde la que Opus
CURA el manifiesto (~20-25 títulos) que después Sonnet convierte en el post (MODO LISTICLE).

Por qué script: es determinista (no alucinable) y a 0 tokens. Correr en Windows, nativo:

    python tools\\armar_bestof.py psicologia
    python tools\\armar_bestof.py negocios        # también sirve para ACTUALIZAR un best-of

Sin dependencias externas (solo stdlib).
"""

import os, re, sys

def frontmatter(text):
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm, lines = {}, parts[1].splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", lines[i])
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                items, j = [], i + 1
                while j < len(lines) and re.match(r"^\s*-\s*", lines[j]):
                    items.append(re.sub(r"^\s*-\s*", "", lines[j]).strip().strip('"').strip("'"))
                    j += 1
                if items:
                    fm[key] = items; i = j; continue
                fm[key] = ""
            else:
                fm[key] = val.strip('"').strip("'")
        i += 1
    return fm

def main():
    if len(sys.argv) < 2:
        print("Uso: python tools\\armar_bestof.py <categoria> [ruta_libros]")
        sys.exit(1)
    cat = sys.argv[1]
    libros = sys.argv[2] if len(sys.argv) > 2 else os.path.join("src", "content", "libros")

    filas = []
    sin_asin = 0
    for fn in os.listdir(libros):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(libros, fn), encoding="utf-8") as fh:
            fm = frontmatter(fh.read())
        if fm.get("categoria") != cat:
            continue
        rec = fm.get("recomendadoPor", [])
        if isinstance(rec, str):
            rec = [rec] if rec else []
        if not fm.get("asin"):
            sin_asin += 1
            continue  # el playbook prohíbe enlazar stubs (fichas sin asin)
        filas.append((len(rec), fn[:-3], fm.get("titulo", ""), rec))

    # Orden: más consenso primero; luego alfabético por título.
    filas.sort(key=lambda r: (-r[0], r[2].lower()))

    print("=" * 72)
    print(f"BEST-OF crudo — categoría '{cat}': {len(filas)} fichas enriquecidas"
          + (f" ({sin_asin} sin asin, excluidas)" if sin_asin else ""))
    print("Ordenadas por consenso (nº de referentes). Curar ~20-25 desde arriba.")
    print("=" * 72)
    print(f"{'#ref':>4}  {'slug':<42}  título / referentes")
    print("-" * 72)
    for n, slug, titulo, rec in filas:
        print(f"{n:>4}  {slug:<42}  {titulo}")
        print(f"{'':>4}  {'':<42}  ↳ {', '.join(rec)}")
    print("-" * 72)
    con2 = sum(1 for f in filas if f[0] >= 2)
    print(f"Con 2+ referentes (consenso): {con2}  ·  con 1: {len(filas) - con2}")

if __name__ == "__main__":
    main()
