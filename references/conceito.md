# Fase 3: o conceito

## O que é um conceito aqui

Uma frase-título + uma história com 4 a 6 etapas + um objeto herói que atravessa a história. A história vira o momento principal em todas as peças:

| Peça | Como o momento principal aparece |
|---|---|
| Site | Seção fixa na tela; a rolagem move a câmera pelas etapas; a trilha de progresso mostra onde a pessoa está |
| Apresentação | O slide central (o mais ousado do deck), com a mesma ilustração |
| Filme | A cena central, a mais longa, com a câmera seguindo o objeto |

Se a ideia não funciona nas três, ainda não é o conceito.

## Como encontrar

1. Leia as histórias verdadeiras do dossiê.
2. Escolha a que tem **movimento** (espaço ou tempo) e que só esta empresa pode contar.
3. Dê nome às etapas com palavras do cliente final, não do jargão do setor ("No porto", e não "Logística internacional").
4. Escolha o **objeto herói**: o produto (ou um objeto simbólico da marca, se não houver modelo 3D) que aparece em todas as etapas.
5. Escolha o **cenário**: mapa, corte de terreno, linha do tempo, planta baixa, mesa posta. Precisa ser algo que a câmera possa percorrer.

## Exemplos por setor

| Setor | Conceito | Etapas | Objeto herói | Cenário |
|---|---|---|---|---|
| Importadora de vinhos (Ganesh, feito) | A viagem do seu vinho | vinhedo, oceano, porto, gôndola, taça | garrafa 3D de vidro escuro com o elefante em ouro | mapa náutico gravado em ouro |
| Joalheria autoral | Da pedra bruta à joia | mina, lapidação, cravação, polimento, no corpo | a pedra principal, em 3D, ganhando facetas | corte geológico e bancada do ourives |
| Café especial | Do pé à xícara | altitude, colheita, secagem, torra, xícara | o grão que muda de cor | encosta com curvas de nível |
| Hotel boutique | Um dia na casa | amanhecer, café, tarde, pôr do sol, jantar | a luz (a cor do fundo muda com a hora) | a planta da casa, vista de cima |
| Incorporadora | Da planta à chave | terreno, fundação, estrutura, acabamento, chave | a maquete que se monta | planta baixa que ganha volume |
| Cosmético natural | Do ingrediente à pele | origem, extração, fórmula, frasco, ritual | a gota | mapa botânico |
| Azeite | Do olival à mesa | olival, colheita, prensa, garrafa, prato | a gota de azeite | mapa de altitude do olival |

## Regras de direção

- **A ousadia fica num lugar só.** Abertura, portfólio e contato são silenciosos: tipografia grande, muito espaço, filetes finos. O espetáculo é o momento principal.
- **O produto é o herói.** Palco de luz (gradiente radial + sombra de contato), nunca dentro de cards.
- **A marca vira forma.** A silhueta da logo serve de moldura de fotos (máscara CSS no site, arco ou SVG no deck, transição de máscara no filme).
- **Movimento com intenção.** Cada animação mostra uma mudança da história (a rota que se desenha, o líquido que enche a taça). Movimento decorativo (partículas, brilhos, "surgir subindo" em tudo) é proibido.
- **Uma cor de destaque.** O ouro (ou a cor da marca) marca só o que está ativo: a rota, a etapa atual, o botão principal.

## Modelo do `conceito.md`

```markdown
# Conceito: <frase-título>

## A história em 3 linhas
## Por que só esta empresa pode contar (fatos do dossiê)
## Etapas
1. <nome curto>: <o que a câmera mostra> / <o que o texto diz>
## Objeto herói
## Cenário
## Como aparece no site, no deck e no filme
## O que fica de fora (e por quê)
```

Mostre à pessoa a frase-título, as etapas e o objeto herói antes de construir.
