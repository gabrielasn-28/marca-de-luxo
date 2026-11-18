"""Recorta fotos de produto (garrafas) de páginas de catálogo com fundo de cor sólida,
gerando PNG com fundo transparente.
Uso: python -I recortar_produtos.py <pasta_com_paginas_jpg> <pasta_saida>
Ajuste G (cor do fundo do painel, RGB) e as páginas a pular (capa/contracapa).
Agrupa produtos por faixas horizontais; depois converta para WebP (qualidade 88, altura máx. 900px).
Monte uma folha de contato para escolher os melhores recortes antes de usar.
"""
import sys, glob, os, numpy as np
from PIL import Image, ImageFilter, ImageDraw
out=sys.argv[2]
G=np.array([139,114,60],float)
for f in sorted(glob.glob(sys.argv[1]+'/p*_0.jpg')):
    pg=os.path.basename(f)[1:3]
    if pg in ('01','30'): continue
    im=Image.open(f).convert('RGB'); a=np.asarray(im).astype(float)
    W=a.shape[1]
    # find gold panel start: column where most pixels are gold
    d=np.sqrt(((a-G)**2).sum(2))
    colgold=(d<30).mean(0)
    x0=int(np.argmax(colgold>0.5)); 
    panel=a[:,x0:]; dp=d[:,x0:]
    fg=dp>38
    rows=fg.mean(1)>0.01
    # group rows
    groups=[];start=None
    for y,r in enumerate(rows):
        if r and start is None: start=y
        if not r and start is not None:
            if y-start>60: groups.append((start,y))
            start=None
    if start is not None and len(rows)-start>60: groups.append((start,len(rows)))
    for gi,(y0,y1) in enumerate(groups):
        sub=fg[y0:y1]; cols=np.where(sub.mean(0)>0.005)[0]
        if len(cols)==0: continue
        cx0,cx1=max(cols.min()-6,0),min(cols.max()+6,panel.shape[1])
        y0b,y1b=max(y0-6,0),min(y1+6,a.shape[0])
        rgb=Image.fromarray(panel[y0b:y1b,cx0:cx1].astype('uint8'))
        dd=dp[y0b:y1b,cx0:cx1]
        alpha=np.clip((dd-22)/(48-22),0,1)*255
        al=Image.fromarray(alpha.astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
        # despill: push edge pixels away from gold
        arr=np.asarray(rgb).astype(float); A=np.asarray(al).astype(float)[...,None]/255
        safe=np.where(A>0.05,(arr-(1-A)*G)/np.maximum(A,0.05),arr)
        rgba=np.dstack([np.clip(safe,0,255),np.asarray(al)]).astype('uint8')
        Image.fromarray(rgba,'RGBA').save(f'{out}/p{pg}_{gi}.png')
