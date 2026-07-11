#!/usr/bin/env python3
"""
Reconcilia un manifiesto de libros descubiertos (MODO DESCUBRIR) contra el catálogo.

Uso:
    python3 tools/reconciliar.py <referente-slug> <manifiesto.txt> [libros_dir]

- <manifiesto.txt>: una línea por libro; campos separados por '|'. El 1º es el TÍTULO
  (normalmente en inglés) y el 2º el AUTOR. Se ignoran los campos siguientes (año, fuente).
- [libros_dir]: por defecto 'src/content/libros'.

Clasifica cada candidato:
    YA-LINKED  → el libro ya existe y el referente ya está en su recomendadoPor. No hacer nada.
    CROSS-REF  → el libro ya existe pero el referente NO está. Agregar el referente (es un cruce).
    REVISAR    → no matchea por slug, pero el AUTOR ya está en el catálogo. Opus decide:
                 ¿es el mismo libro con título traducido (=> cross-ref) o un libro nuevo?
    NUEVO      → no hay match. Crear ficha nueva.

El match principal es por SLUG: como los slugs del catálogo derivan del título en inglés
(p.ej. "Klara and the Sun" -> klara-and-the-sun), slugificar el título descubierto y buscar
ese archivo resuelve el problema de que el catálogo esté en español y el descubrimiento en inglés.
"""
import sys, os, re, unicodedata, glob


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"\s+", " ", strip_accents(s or "").lower()).strip()


def slugify(s):
    s = strip_accents(s or "").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def parse_fiche(path):
    txt = open(path, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = m.group(1) if m else txt
    tit = re.search(r'^titulo:\s*"?(.*?)"?\s*$', fm, re.M)
    aut = re.search(r'^autorLibro:\s*"?(.*?)"?\s*$', fm, re.M)
    recs = []
    rm = re.search(r"^recomendadoPor:\s*\n((?:[ \t]*-[ \t]*.*\n?)+)", fm, re.M)
    if rm:
        recs = re.findall(r"-\s*(\S+)", rm.group(1))
    return (tit.group(1) if tit else ""), (aut.group(1) if aut else ""), recs


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    ref = sys.argv[1]
    manifest = sys.argv[2]
    libros_dir = sys.argv[3] if len(sys.argv) > 3 else "src/content/libros"

    catalog, authors = {}, {}
    for p in glob.glob(os.path.join(libros_dir, "*.md")):
        slug = os.path.basename(p)[:-3]
        tit, aut, recs = parse_fiche(p)
        catalog[slug] = (tit, aut, recs)
        authors.setdefault(norm(aut), []).append(slug)

    counts = {"YA-LINKED": 0, "CROSS-REF": 0, "REVISAR": 0, "NUEVO": 0}
    for line in open(manifest, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [x.strip() for x in line.split("|")]
        title = parts[0]
        author = parts[1] if len(parts) > 1 else ""
        cslug = slugify(title)
        if cslug in catalog:
            _, _, recs = catalog[cslug]
            if ref in recs:
                counts["YA-LINKED"] += 1
                print(f"YA-LINKED  | {title} -> {cslug}")
            else:
                counts["CROSS-REF"] += 1
                print(f"CROSS-REF  | {title} -> agregar '{ref}' a recomendadoPor de {cslug}")
        else:
            amatch = authors.get(norm(author), [])
            if amatch:
                counts["REVISAR"] += 1
                print(f"REVISAR    | {title} — autor '{author}' ya está en: {', '.join(amatch)} "
                      f"(¿mismo libro traducido -> cross-ref, o libro nuevo?)")
            else:
                counts["NUEVO"] += 1
                print(f"NUEVO      | {title} — crear {cslug}.md (recomendadoPor: {ref})")

    print("\nResumen:", ", ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
