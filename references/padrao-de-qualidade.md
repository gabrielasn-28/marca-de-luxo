# Padrão de qualidade

O nível mínimo é o de um site do dia (SOTD) no Awwwards ou no FWA, e o pacote Ganesh em `assets/exemplo-ganesh/` é a régua concreta. Use as referências abaixo como medida, sem copiar nenhuma.

## A régua por entrega

Antes de mostrar qualquer peça, dê uma nota de 0 a 2 em cada linha (0 = falta, 1 = feito, 2 = no nível da Ganesh ou acima). **Abaixo de 2 em qualquer linha marcada com ★, a peça não sai.**

| Entrega | Critério |
|---|---|
| Dossiê | ★ Cada fato tem fonte; nada inventado. Há pelo menos 3 histórias verdadeiras e uma lista "a confirmar". |
| Conceito | ★ A história só serve para esta empresa (troque o nome por um concorrente: se ainda servir, refaça). Tem 4 a 6 etapas, um objeto herói e um cenário que a câmera percorre. |
| Identidade | ★ Cores medidas da logo; tokens nos dois temas com contraste AA; duas fontes que contrastam; logo em vetor nas três versões. |
| Site | ★ Momento principal guiado pela rolagem e funcionando no celular e no iPhone com "Reduzir movimento". ★ Nenhum erro no console, nenhuma rolagem lateral, nada cortado nos temas dia e noite. Portfólio em até ~3,5 telas. Contato clicável. Imagens em WebP e 3D desenhado só quando algo muda. |
| Apresentação | ★ Mesma história e mesmos tokens do site; nada passa da margem de 128px; números confirmados; sem notas internas nas versões enviadas a terceiros. |
| Filme | ★ Mesma estrutura do site; `SPEC.md` com números; `check` sem erros; cada linha de texto legível pelo tempo mínimo; quadros de QA revisados; cortes escondidos; som ou aviso explícito de que saiu sem som. |
| Entrega | ★ Diz o que não foi verificado e o que a cliente precisa confirmar. |

## Referências premiadas

| Site | Por que é referência | O que levar |
|---|---|---|
| Campo alle Comete (aquest.it), vinícola, Awwwards SOTD | O visitante explora a propriedade em 3D | Explorar o terroir ou o lugar de origem cria vínculo |
| Chartogne-Taillet (immersive-g.com), champagne, SOTD Awwwards/FWA/CSSDA | Mapa animado que conta a origem | Mapa como narrativa da origem até o cliente |
| Pasqua Wines, Awwwards SOTM jun/2023 | Three.js e Blender a serviço da marca | 3D que soma à tradição sem parecer brinquedo |
| Ruinart × David Shrigley, Awwwards SOTM jan/2022 | Galeria de arte em 3D em tempo real | Associar o produto a arte e exclusividade |
| Chandon Garden Spritz (cher-ami.tv) | O visitante gira a garrafa para descobrir o produto | Ficha técnica vira interação |
| Conti Ducco, Awwwards SOTD | Rolagem horizontal em capítulos | Ritmo de livro, catálogo integrado |
| Volcán Tequila (wild.as), SOTD Awwwards/FWA | Profundidade 3D em fotos comuns | Efeito de luxo sem modelo 3D |
| Top Up Wines, Good Design 2025 | Garrafa 3D girando e detalhes vivos | Pequenos detalhes que parecem feitos à mão |
| Pinea (Awwwards) | A garrafa se transforma na próxima | A troca de produto vira um momento |
| Bonollo 1908, Awwwards 2025 | Narrativa imersiva de uma história centenária | História longa sem texto longo |

## Outros setores
A tabela acima é de bebidas, porque foi onde a skill nasceu. Para outro setor, pesquise na fase 1 de 3 a 5 sites premiados do setor (Awwwards: filtre por categoria, como "Fashion", "Architecture", "Food & Drink"; FWA; CSSDA) e acrescente-os ao `dossie.md` com a mesma coluna "O que levar". Não cite prêmio que você não confirmou.

O que costuma funcionar por setor:
- **Joias e relógios**: macro extremo do material, luz que desliza pelo metal, o processo artesanal em etapas, muito preto ou muito branco.
- **Moda**: tipografia gigante e editorial, fotografia que respira, transição entre looks como corte de filme.
- **Hotelaria**: a luz do dia mudando o tema, planta da casa vista de cima, som ambiente opcional.
- **Imóveis**: a maquete que se monta, a planta que ganha volume, a vista real de cada andar.
- **Alimentos e cosméticos**: a origem no mapa, a matéria-prima em macro, a textura (gota, grão, pó).

## Referências de estrutura que a Gabriela trouxe (gosto, não nível)
Os 14 prints estão em `assets/exemplo-ganesh/referencias/`, com a tabela do que se aproveitou e do que ficou de fora de cada um.
- **Fontana**: palco de luz, garrafas escuras, botões só com contorno dourado.
- **BeerStrasse e 56° North**: linha de garrafas com nome e teor; fotos redondas da colheita.
- **Scotch Me**: faixa com as marcas parceiras.
- **MODO, Aakriti e Horizonte**: nome gigante no fundo da capa; arco grande como moldura.

## Teste rápido de "cara de IA"
Se três ou mais itens forem verdade, refaça o conceito:
- [ ] Capa, faixa de números, cards em grade e abas, nessa ordem.
- [ ] Todos os títulos com uma etiqueta pequena em cima.
- [ ] Uma palavra do título em outra cor ou em itálico só para enfeitar.
- [ ] Cards com o mesmo raio e a mesma sombra em tudo.
- [ ] Animação de "surgir subindo" em toda seção.
- [ ] Separadores com pontinhos (A · B · C) e setas "→" em todo link.
- [ ] Nada no site que só esta empresa poderia ter.
- [ ] Partículas, brilhos de lente ou cartões de vidro sem função na história.
- [ ] Textos genéricos ("tradição", "excelência", "paixão") sem um fato junto.
