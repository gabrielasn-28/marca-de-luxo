"""Gera o mapa "náutico gravado" em WebP transparente (mundo + detalhe), a partir do
Natural Earth 110m (domínio público):
https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson
Uso: python -I mapa_raster.py countries.geojson <pasta_saida>
Por que imagem e não SVG: SVG grande dentro de um elemento com transform/scale é
redesenhado a cada quadro e trava a rolagem. Imagem só é movida pela GPU.
Ajuste: recorte (L0, T), países destacados (ORIG), cores (GOLD, CH) e a janela de detalhe.
"""
import json,sys
from PIL import Image, ImageDraw
g=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]
L0,T=-100,62
ORIG={'Argentina','Chile','Croatia','Spain','France','Italy','Portugal','Brazil'}
GOLD=(143,119,73); CH=(214,193,144)
def render(x0,y0,w,h,ppu,ss,fn,lw):
    W,H=int(w*ppu*ss),int(h*ppu*ss); k=ppu*ss
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    P=lambda lon,lat:(((lon-L0)*10-x0)*k,((T-lat)*10-y0)*k)
    # graticule dashed
    for lon in range(-90,41,15):
        X=((lon-L0)*10-x0)*k
        for y in range(0,H,int(8*k)): d.line([(X,y),(X,y+2*k)],fill=GOLD+(40,),width=max(1,int(.8*k)))
    for lat in range(-45,61,15):
        Y=((T-lat)*10-y0)*k
        for x in range(0,W,int(8*k)): d.line([(x,Y),(x+2*k,Y)],fill=GOLD+(40,),width=max(1,int(.8*k)))
    for f in g['features']:
        geo=f['geometry']; hl=f['properties']['NAME'] in ORIG
        polys=geo['coordinates'] if geo['type']=='MultiPolygon' else [geo['coordinates']]
        for p in polys:
            pts=[P(a,b) for a,b in p[0]]
            if len(pts)<3: continue
            d.polygon(pts,fill=(GOLD+(42,)) if hl else (GOLD+(14,)))
            d.line(pts+[pts[0]],fill=(CH+(190,)) if hl else (GOLD+(105,)),width=max(1,int(lw*k)),joint='curve')
    im=im.resize((W//ss,H//ss),Image.LANCZOS)
    im.save(fn,'WEBP',quality=88,method=6); print(fn,im.size)
render(0,0,1400,1070,2,3,out+'/mapa-mundo.webp',.9)
render(420,760,260,200,7,2,out+'/mapa-brasil.webp',.35)
