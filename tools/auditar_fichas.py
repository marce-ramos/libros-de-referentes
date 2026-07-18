#!/usr/bin/env python3
"""
Audita las fichas de libro contra la Regla de atribución (ENRIQUECER.md · MODO LIBRO):
- Todo referente en `recomendadoPor` debe estar NOMBRADO en el cuerpo (sección o línea consolidada).
- Máximo 2 secciones "## Por qué/También lo recomienda ...".

Uso:
    python3 tools/auditar_fichas.py [libros_dir] [autores_dir]

Salida: por cada ficha con problemas, los referentes NO nombrados y/o el exceso de secciones.
Es un pre-chequeo determinístico (0 tokens) para alimentar la acción "Sanear".
"""
import sys, os, re, glob, unicodedata


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"\s+", " ", strip_accents(s).lower()).strip()


def split_fm_body(txt):
    txt = txt.replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    return (m.group(1), m.group(2)) if m else ("", txt)


def recomendados(fm):
    rm = re.search(r"^recomendadoPor:\s*\n((?:[ \t]*-[ \t]*.*\n?)+)", fm, re.M)
    return re.findall(r"-\s*(\S+)", rm.group(1)) if rm else []


def nombre_de(path):
    fm, _ = split_fm_body(open(path, encoding="utf-8", errors="replace").read())
    m = re.search(r'^nombre:\s*"?(.*?)"?\s*$', fm, re.M)
    return m.group(1) if m else ""


def nombrado(nombre, body_norm):
    if not nombre:
        return True  # sin nombre no se puede chequear; no lo marcamos
    n = norm(nombre)
    if n in body_norm:
        return True
    toks = [t for t in n.split(" ") if len(t) >= 4]
    return any(t in body_norm for t in toks)


def main():
    libros_dir = sys.argv[1] if len(sys.argv) > 1 else "src/content/libros"
    autores_dir = sys.argv[2] if len(sys.argv) > 2 else "src/content/autores"

    nombres = {}
    for p in glob.glob(os.path.join(autores_dir, "*.md")):
        nombres[os.path.basename(p)[:-3]] = nombre_de(p)

    total, con_problema = 0, 0
    for p in sorted(glob.glob(os.path.join(libros_dir, "*.md"))):
        total += 1
        slug = os.path.basename(p)[:-3]
        fm, body = split_fm_body(open(p, encoding="utf-8", errors="replace").read())
        refs = recomendados(fm)
        body_norm = norm(body)
        faltan = [r for r in refs if not nombrado(nombres.get(r, ""), body_norm)]
        # Anti-patrones de atribución (debe haber UNA sola sección "Por qué lo recomienda(n)"):
        tambien_h2 = len(re.findall(r"(?m)^##\s+Tambi[eé]n lo recomienda", body))
        mpq = re.search(r"(?m)^##\s+Para qui[eé]n es", body)
        orphan = bool(mpq and re.search(r"(?m)^Tambi[eé]n lo recomiend", body[mpq.end():]))
        # Nota de edición (o "solo inglés") al pie:
        sin_edicion = not re.search(r"^>\s*(Edici[oó]n|Por ahora|Disponible)", body, re.M)
        # Sobre-recorte: cuerpo muy corto o sin "## De qué trata".
        corta = len(body.strip()) < 700 or not re.search(r"^##\s+De qu[eé] trata", body, re.M)
        if faltan or tambien_h2 or orphan or sin_edicion or corta:
            con_problema += 1
            print(f"[FIX] {slug}")
            if faltan:
                print(f"      referentes en el pill sin nombrar: {', '.join(faltan)}")
            if tambien_h2:
                print(f"      {tambien_h2} encabezado(s) '## Tambien lo recomienda' -> unificar en 'Por que lo recomienda(n)'")
            if orphan:
                print("      atribucion huerfana tras 'Para quien es' -> moverla a la seccion de recomendacion")
            if sin_edicion:
                print("      sin nota de edicion (> Edicion en espanol / solo ingles)")
            if corta:
                print("      cuerpo corto o sin '## De que trata' -> posible sobre-recorte")

    print(f"\nResumen: {con_problema}/{total} fichas a sanear.")


if __name__ == "__main__":
    main()
