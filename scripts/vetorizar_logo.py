"""Vetoriza uma logo em bitmap (PNG pequeno) para um path SVG.
Uso: python -I vetorizar_logo.py logo.png > path.txt
Requer: pip install potracer numpy pillow  (potracer é potrace em Python puro, sem compilar)
Atenção: se o PNG tiver transparência, componha sobre branco antes (senão o fundo vira preto).
O limiar (a >= 190) marca como "fundo" os pixels claros; ajuste se a logo for clara.
Depois: monte o SVG com fill-rule="evenodd" e confira visualmente no navegador.
"""
import sys, potrace, numpy as np
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert('RGB')
S=10
big = im.resize((im.width*S, im.height*S), Image.LANCZOS).filter(ImageFilter.GaussianBlur(S*0.6))
a = np.asarray(big.convert('L'))
bm = potrace.Bitmap(a >= 190)
path = bm.trace(turdsize=50, alphamax=1.1, opticurve=True, opttolerance=0.3)
parts=[]
for curve in path:
    s=curve.start_point; d=[f"M{s.x/S:.2f},{s.y/S:.2f}"]
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x/S:.2f},{seg.c.y/S:.2f}L{seg.end_point.x/S:.2f},{seg.end_point.y/S:.2f}")
        else:
            d.append(f"C{seg.c1.x/S:.2f},{seg.c1.y/S:.2f} {seg.c2.x/S:.2f},{seg.c2.y/S:.2f} {seg.end_point.x/S:.2f},{seg.end_point.y/S:.2f}")
    parts.append("".join(d)+"Z")
print(" ".join(parts))
