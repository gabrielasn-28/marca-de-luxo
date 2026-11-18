# Fase 4: identidade visual

## Cores
- Meça as cores na logo e no material real (Pillow: cor dominante dos pixels não transparentes). Nunca chute.
- Monte os tokens dos dois temas desde o início:
  - **Noite**: um fundo escuro com temperatura (a adega #120F0C na Ganesh, nunca preto puro).
  - **Dia**: um papel quente (o catálogo #FAF7F1), nunca branco puro.
  - **Marca**: a cor da logo (#8F7749) igual nos dois temas, mais uma versão clara para destaque no escuro (#D6C190) e uma escura para destaque no claro (#7A6234).
  - Texto principal, texto 2, sutil e apagado, com contraste AA sobre o fundo de cada tema.
  - Também são tokens: linha, brilho (palco de luz), contorno, sombra, véu (gradiente sob o texto) e a cor do produto (o vinho #5E1A26).
- Nenhuma cor literal dentro dos componentes; tudo passa pelos tokens. Assim o tema claro funciona sem retrabalho.

## Tipografia
- Duas famílias bem diferentes: **display com caráter** (Bodoni Moda na Ganesh; alternativas: Cormorant, Playfair Display com cuidado, Fraunces, Italiana) e **texto limpo** (Jost; alternativas: Manrope, Inter Tight, Work Sans).
- Display grande e leve (400), com itálico para a segunda metade de uma frase, nunca uma palavra solta colorida.
- Texto em 300 a 400, 17px no corpo, `line-height` 1,65.
- Google Fonts com `display=swap` no site; no filme, os woff2 baixados para `assets/fonts` com `@font-face`.

## Logo
- Se a pessoa não tiver vetor, redesenhe com `scripts/vetorizar_logo.py` (limiar + contorno) e gere três versões: dourada, branca e escura. Confira o resultado aumentado; ajuste à mão o que o traçado errou.
- Mantenha a forma original. O redesenho limpa, não reinventa, a menos que a pessoa peça um rebranding.
- A silhueta da logo vira recurso: moldura de foto (`mask: url(logo.svg)`), textura no objeto 3D, transição no filme, marca d'água grande e apagada no encerramento.

## Imagens
- Produtos: recorte do catálogo com `scripts/recortar_produtos.py` (fundo removido, WebP com transparência, ~500px de altura).
- Mapas e ilustrações grandes: WebP rasterizado (`scripts/mapa_raster.py`), em 2x para o zoom.
- Fotos com pessoas: só com autorização confirmada no `briefing.md`.

## Guia de identidade (entrega opcional)
Uma página com: logo nas três versões e área de respiro, as cores dos dois temas com os valores, as duas fontes com a escala, a silhueta usada como moldura e 2 exemplos de aplicação. Use as mesmas variáveis CSS do site.
