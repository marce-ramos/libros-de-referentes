# Seguimiento — ronda de indexación manual (agosto/septiembre 2026)

Plan: `indexacion-manual-2026-08-27.md` · URLs: `indexacion-manual-2026-08-27-urls.txt`
Verificación previa: **✅ 2026-08-27 — las 50 devuelven 200 directo, 0 redirecciones.**
Con eso queda confirmado que los 7 "Error de redirección" son residuo de julio y que
no hay ningún bug vivo que arreglar antes de pedir.

---

## Pedidos — GSC → Inspeccionar cualquier URL → Solicitar indexación

Marcá con `[x]` a medida que las pedís. Si salta "Has superado la cuota", cortá ahí y
seguí al día siguiente desde donde quedaste (no reinicies la tanda).

### [ ] Tanda 1 — jue 27-ago — **los 10 listicles ciegos**
```
[X] 1  /blog/libros-que-recomienda-satya-nadella      (error redir · sin rastrear desde 14-jul)
[x] 2  /blog/libros-que-recomienda-elon-musk          (error redir · sin rastrear desde 08-jul)
[x] 3  /blog/libros-que-recomienda-warren-buffett     (error redir · sin rastrear desde 05-jul)
[x] 4  /blog/libros-que-recomienda-barack-obama       (error redir · sin rastrear desde 05-jul)
[x] 5  /blog/libros-que-recomienda-sam-altman         (error redir · sin rastrear desde 10-jul)
[x] 6  /blog/libros-que-recomienda-reese-witherspoon  (error redir · sin rastrear desde 13-jul)
[x] 7  /blog/libros-que-recomienda-jordan-peterson    (error redir · sin rastrear desde 08-jul)
[x] 8  /blog/libros-que-recomienda-garry-kasparov     (nunca rastreada)
[x] 9  /blog/libros-que-recomienda-gwyneth-paltrow    (nunca rastreada)
[x] 10 /blog/libros-que-recomienda-natalie-portman    (nunca rastreada)
```
Fecha real: ________  ·  Cuántas entraron antes del corte de cuota: ____

### [ ] Tanda 2 — vie 28-ago — 7 referentes + 3 fichas top
Fecha real: ________  ·  Entraron: ____

### [ ] Tanda 3 — sáb 29-ago — ficción y ciencia ficción
Fecha real: ________  ·  Entraron: ____

### [ ] Tanda 4 — dom 30-ago — negocios
Fecha real: ________  ·  Entraron: ____

### [ ] Tanda 5 — lun 31-ago — psicología y ciencia
Fecha real: ________  ·  Entraron: ____

---

## Re-mediciones

### [ ] ~lun 07-sep — **el check rápido y más importante**
GSC → Indexación de páginas → "Error de redirección" → Exportar.

| Resultado | Lectura |
|---|---|
| 7 → **0** | Ganamos. Los 7 listicles top volvieron al rastreo. |
| 7 → 3-6 | Va lento pero avanza. Volver a pedir los que quedan. |
| sigue en 7 | Hay algo que no vemos. Usar Inspeccionar URL → **Probar URL publicada** en `satya-nadella` y mirar qué responde Googlebot en vivo. |

### [ ] ~jue 17-sep — el check estructural (3 semanas)
Exportar los dos: cobertura completa + drilldown de "Descubierta: actualmente sin indexar".

| Métrica | Base 20-ago | Objetivo | Si no se mueve |
|---|---|---|---|
| Páginas indexadas | 706 | 750+ | — |
| Cola "Descubierta" | 663 | <600 | Los pedidos no alcanzan → ir por la **poda del catálogo** |
| URLs únicas con ≥1 impresión/semana | ~20 | 40+ | Métrica de la recuperación de julio |

⚠ GSC tiene 2-3 días de retraso en los datos. Un export del 07-sep muestra hasta ~04-sep.

---

## Mientras corren las tandas — qué SÍ producir

Regla vigente desde este análisis: **cero fichas de libro nuevas** hasta que la cola baje.
Cada lote nuevo agranda una cola que en seis semanas movió dos páginas.

Lo que sí:
- [ ] Best-of de **filosofía**
- [ ] Best-of de **historia**
- [ ] Best-of de **memorias**
- [ ] Best-of de **espiritualidad**
- [ ] Enlazar `/blog/mejores-libros-de-ficcion` desde `/categorias/ficcion` (pendiente viejo)
- [ ] Ampliar listicles existentes que ya rankean

---

## Cerrado en este análisis — no volver sobre esto

- **139 "Duplicada: otra canónica"** → las 139 terminan en barra final, cero excepciones,
  ninguna de sus canónicas está en la cola. Es la migración de julio funcionando bien.
  **Ninguna acción.**
- **358 "Página con redirección"** + **5 "alternativa con canónica"** → mismo caso.
- Total: **502 de las 1193 "sin indexar" son ruido contable (42%).** El problema real
  eran 670 URLs, y de esas las 7 críticas ya están en la tanda 1.
