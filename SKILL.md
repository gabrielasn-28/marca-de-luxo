---
name: marca-de-luxo
description: Cria o pacote completo de uma marca premium — pesquisa da empresa, identidade visual, site cinematográfico (rolagem com animação, 3D, modo dia/noite), apresentação e filme da marca em vídeo — no nível dos sites premiados (Awwwards, FWA). Use sempre que a pessoa pedir site, landing page, identidade visual, rebranding, apresentação comercial ou vídeo institucional "de luxo", "premium", "elegante", "sofisticado", "com animação", "cinematográfico" ou "como os sites premiados", para vinhos, bebidas, alimentos finos, moda, joias, cosméticos, hotelaria, imóveis ou qualquer empresa que quer valorizar o produto — mesmo que ela mande só referências simples, um catálogo em PDF ou o site antigo. Também use para continuar, corrigir ou traduzir um projeto feito com esta skill.
---

# Marca de luxo

Esta skill transforma o material de uma empresa (logo, site antigo, catálogo, fotos, conversas) num pacote coerente: **dossiê da empresa → conceito → identidade → site → apresentação → filme**. Todas as peças contam a mesma história com os mesmos tokens visuais.

Nasceu do projeto Ganesh Vinhos (importadora de vinhos de São Paulo). O pacote completo e testado está em `assets/exemplo-ganesh/` e é o **parâmetro de qualidade**: nada sai abaixo dele. Versão 1.0.

## Por que existe

Pedidos de "site de luxo" costumam virar um template com cores trocadas: capa, faixa de números, cards e abas. Isso tem "cara de IA" e não valoriza o produto. O que separa um site premiado é: uma história que só aquela empresa pode contar, transformada num momento que acontece com a rolagem, e um acabamento sem defeito em celular, computador, tema claro e escuro. Esta skill existe para chegar lá sempre, mesmo quando a pessoa manda referências fracas.

## Mapa do processo

| Fase | O que sai | Leia |
|---|---|---|
| 0. Preparar | Skills e ferramentas conferidas | `references/dependencias.md` |
| 1. Pesquisar | `dossie.md` da empresa | `references/pesquisa-empresa.md` |
| 2. Perguntar | `briefing.md` com as respostas | `references/perguntas.md` |
| 3. Conceber | `conceito.md` (a história e o momento principal) | `references/conceito.md`, `references/padrao-de-qualidade.md` |
| 4. Identidade | Tokens, logo em vetor, fontes | `references/identidade-visual.md` |
| 5. Site | `site/index.html` + `img/` | `references/site-arquitetura.md`, `references/site-qa.md` |
| 6. Apresentação | Deck Slides (PPTX/PDF) | `references/apresentacao.md` |
| 7. Filme | MP4 16:9 de 30 a 60 s | `references/video.md` |
| 8. Entregar | Links, pendências, próximo passo | esta página, seção 8 |

Siga a ordem: cada fase alimenta a seguinte. A pessoa pode pedir só uma peça (por exemplo, só o vídeo); mesmo assim faça as fases 1 a 4 de forma enxuta, porque sem dossiê e conceito a peça sai genérica. Se o projeto já existe (há `dossie.md`, `conceito.md` ou um site feito com esta skill na pasta), leia o que existe e continue de onde parou.

## 0. Preparar

Confira as skills e ferramentas de `references/dependencias.md`. As 19 skills externas vêm dentro desta, em `dependencias/skills.zip`; rode `python scripts/instalar_dependencias.py --verificar` e, se faltar alguma, o mesmo comando sem `--verificar`. Antes de escrever código, leia `frontend-design`, `gsap-scrolltrigger` e `gsap-performance`. Antes do vídeo, leia `hyperframes`. Peça autorização antes de instalar programas (Node, FFmpeg).

Organize a pasta do projeto assim (é o que as outras fases esperam):

```
<EMPRESA>/
├── fontes/        material recebido (PDF, fotos, logo antigo, conversas)
├── marca/         logo em SVG nas versões dourada/branca/escura
├── dossie.md      fase 1
├── briefing.md    fase 2
├── conceito.md    fase 3
├── site/          fase 5 (git próprio; .claude/launch.json aponta para cá)
├── apresentacao/  fase 6 (LINKS.md com os artefatos)
└── video/         fase 7 (projeto HyperFrames)
```

## 1. Pesquisar a empresa (sempre, antes de perguntar)

Ninguém cria a identidade de uma empresa que não entende. Leia tudo o que a pessoa mandou e pesquise a empresa, o setor, os concorrentes e as referências premiadas do setor. O resultado é o `dossie.md`, com a fonte de cada fato. O roteiro e o modelo estão em `references/pesquisa-empresa.md`; o exemplo real é `assets/exemplo-ganesh/dossie.md`.

O dossiê responde: o que a empresa vende e para quem, o que ela faz que os concorrentes não fazem, quais são os ativos reais (logo, fotos, catálogo, números confirmados), quais histórias verdadeiras ela tem e o que ainda precisa ser confirmado. Pergunte só o que a pesquisa não respondeu.

## 2. Perguntar

Use `references/perguntas.md`: rodadas de no máximo 4 perguntas, cada uma com opções e uma recomendada. A rodada 1 é obrigatória (foco, público, primeira entrega, logo). As outras só quando mudam o resultado. Registre as respostas no `briefing.md` (modelo em `assets/modelos/briefing.md`).

Peça sempre os sites de que a pessoa gosta. **Use as referências dela para entender o gosto (cor, clima, tipo de foto) e nunca para baixar o nível.** Diga em uma linha o que vai aproveitar de cada uma.

## 3. Conceber: uma história, não uma lista de seções

Antes de qualquer pixel, escreva o `conceito.md` (modelo em `assets/modelos/conceito.md`): a história que só esta empresa pode contar e como ela vira **o momento principal**, contado pela rolagem no site, pelo slide central na apresentação e pela cena central no filme.

- Ganesh: "A viagem do seu vinho": vinhedo, oceano, porto, gôndola e taça, com uma garrafa 3D atravessando um mapa náutico.
- Outros: a joia lapidada camada a camada; o café do pé até a xícara; o hotel do amanhecer ao jantar; o imóvel da planta até a chave.

Regras (detalhes e exemplos por setor em `references/conceito.md`):
- **A ousadia fica num lugar só**, o momento principal. O resto é silencioso: tipografia grande, muito espaço, filetes finos.
- **O produto é o herói**, num palco de luz (gradiente radial e sombra no chão), nunca dentro de cards.
- **A marca vira forma**: a silhueta da logo serve de moldura de fotos e de transição.
- Rode o teste de "cara de IA" de `references/padrao-de-qualidade.md`. Com três ou mais itens marcados, refaça o conceito.

Mostre o conceito à pessoa em poucas linhas (a história, as 4 a 6 etapas e o objeto herói) antes de construir. Mudar uma ideia custa minutos; mudar um site pronto custa horas.

## 4. Identidade visual

Siga `references/identidade-visual.md`. O essencial:
- Tire as cores da logo e do material real (medidas em pixels, sem chutar).
- Tokens para **noite e dia** desde o início; nenhuma cor literal nos componentes.
- Duas famílias de fonte bem diferentes: display com caráter + texto limpo.
- Logo redesenhada em vetor (`scripts/vetorizar_logo.py`) nas versões dourada, branca e escura.
- Produtos recortados do material da empresa (`scripts/recortar_produtos.py`), nunca imagens de terceiros.

## 5. Site

Comece copiando a estrutura de `assets/exemplo-ganesh/site/index.html`, que já resolve dezenas de armadilhas, e troque o conteúdo e o momento principal. Não comece do zero: cada defeito documentado em `references/site-arquitetura.md` já quebrou um site real.

Estrutura que funciona (adapte, não copie):
1. **Abertura**: título dividido em volta do objeto herói (3D ou foto num palco de luz), revelado linha a linha.
2. **Momento principal**: seção fixa com 4 a 6 etapas, trilha de progresso e câmera que se move.
3. **Portfólio horizontal**: título, contador e setas dentro da parte fixa; três produtos à vista; percurso de até ~3,5 telas.
4. **Pessoas e parceiros**: lista tipográfica com a imagem acompanhando o cursor.
5. **Encerramento**: contato clicável (telefone, WhatsApp com mensagem pronta, mapa) e o símbolo grande ao fundo.

Requisitos que não se negociam:
- Funciona em celular (375px) e computador, nos temas dia e noite, sem rolagem lateral e sem erro no console.
- **"Reduzir movimento" não desliga a experiência**: a rolagem continua guiando a história; saem só os movimentos automáticos. Se o GSAP não carregar, há uma versão estática que ainda mostra o momento principal (o mapa, o objeto).
- Desempenho: 3D desenhado só quando algo muda, ilustrações grandes em WebP, só `transform` e `opacity` animados.
- Dados reais. Nada inventado. Pessoas em fotos só com autorização.

Teste tudo com `references/site-qa.md` antes de mostrar. Mostre provas (capturas, medidas), não promessas.

## 6. Apresentação

A mesma história vira deck no tipo de artefato Slides (exporta PPTX e PDF). Roteiro de 12 slides, ritmo noite/dia/dourado, limitações do formato e traduções: `references/apresentacao.md`. Exemplo: `assets/exemplo-ganesh/apresentacao/`.

## 7. Filme da marca (16:9, 30 a 60 s)

O filme tem a mesma estrutura do site, em tempo: abertura com o objeto herói → o momento principal → os produtos → a prova real → a assinatura. Produção de alto nível: três roteiros só em palavras para a pessoa escolher, `SPEC.md` com cada adjetivo virando número, cortes escondidos em quadros idênticos, som e música, revisão quadro a quadro antes do render. Tudo em `references/video.md`; exemplo em `assets/exemplo-ganesh/video/`.

## 8. Entregar

- Site: publique (Vercel ou artefato) e guarde os arquivos na pasta do projeto com git.
- Apresentação e filme: links e arquivos na pasta, listados num `LINKS.md`.
- Na mensagem final, diga o que foi feito, o que foi verificado e como, **o que não foi verificado** (por exemplo, "não testado num iPhone real"), quais dados a pessoa precisa confirmar e qual é o próximo passo.
- Atualize esta skill com cada lição nova: armadilhas técnicas em `site-arquitetura.md` ou `video.md`, perguntas que faltaram em `perguntas.md`.

## Exemplos e testes

- `assets/exemplo-ganesh/`: o pacote real (dossiê, briefing, conceito, site com imagens, apresentação, SPEC e cenas do vídeo). É a régua.
- `assets/teste-joalheria/`: um briefing de outro setor e o resultado esperado, para provar que a skill não depende de vinho. Use-o para avaliar a skill depois de qualquer mudança grande.
- `evals/`: casos de teste no formato do `claude plugin eval`.
