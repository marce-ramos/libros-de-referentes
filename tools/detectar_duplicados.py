#!/usr/bin/env python3
"""
Detecta posibles fichas duplicadas en el catálogo (red de seguridad post-barrido).

Uso:
    python3 tools/detectar_duplicados.py [libros_dir]

Reporta:
    [DUP] dos o más fichas con el MISMO autor normalizado + título normalizado -> duplicado casi
          seguro (el mismo libro cargado dos veces, p.ej. una con título EN y otra con título ES).
    [REV] autores con 2+ libros -> informativo, para eyeballear que no sea el mismo libro con
          títulos distintos (la mayoría serán autores legítimos con varias obras).

Corré esto después de cada barrido de descubrimiento/enriquecimiento.
"""
import sys, os, re, unicodedata, glob
from collections import defaultdict


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", "", re.sub(r"\s+", " ", strip_accents(s or "").lower())).strip()


def parse_fiche(path):
    txt = open(path, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = m.group(1) if m else txt
    tit = re.search(r'^titulo:\s*"?(.*?)"?\s*$', fm, re.M)
    aut = re.search(r'^autorLibro:\s*"?(.*?)"?\s*$', fm, re.M)
    return (tit.group(1) if tit else ""), (aut.group(1) if aut else "")


def main():
    libros_dir = sys.argv[1] if len(sys.argv) > 1 else "src/content/libros"
    exact = defaultdict(list)      # (autor_norm, titulo_norm) -> [slugs]
    by_author = defaultdict(list)  # autor_norm -> [(slug, titulo)]
    for p in glob.glob(os.path.join(libros_dir, "*.md")):
        slug = os.path.basename(p)[:-3]
        tit, aut = parse_fiche(p)
        exact[(norm(aut), norm(tit))].append(slug)
        by_author[norm(aut)].append((slug, tit))

    dups = {k: v for k, v in exact.items() if len(v) > 1}
    print(f"=== [DUP] título+autor idénticos ({len(dups)}) ===")
    for (a, t), slugs in dups.items():
        print(f"  DUP: '{t}' / '{a}' -> {', '.join(slugs)}")
    if not dups:
        print("  (ninguno)")

    multi = {a: bs for a, bs in by_author.items() if len(bs) > 1 and a}
    print(f"\n=== [REV] autores con 2+ libros ({len(multi)}) — revisar que no sean el mismo ===")
    for a in sorted(multi):
        libros = "; ".join(f"{t} ({s})" for s, t in multi[a])
        print(f"  {a}: {libros}")


if __name__ == "__main__":
    main()
