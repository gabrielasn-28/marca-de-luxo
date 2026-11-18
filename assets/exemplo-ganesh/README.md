# Exemplo de referência: Ganesh Vinhos

O pacote real que originou a skill. É a **régua de qualidade**: qualquer projeto novo é comparado com ele.

| Arquivo | O que é | O que observar |
|---|---|---|
| `dossie.md` | Pesquisa da empresa | Fatos com fonte; a história que virou conceito; a lista "a confirmar" |
| `briefing.md` | Respostas da cliente | Como cada resposta mudou o projeto |
| `conceito.md` | "A viagem do seu vinho" | Etapas, objeto herói, cenário, e como aparecem nas 3 peças |
| `marca/` | Símbolo redesenhado em vetor | Três versões: dourada, branca, escura |
| `site/index.html` + `img/` | Site final (publicado em ganesh-vinhos-site.vercel.app) | Abertura com garrafa 3D, viagem fixada no mapa, portfólio horizontal com contador e setas, lista de produtores com imagem no cursor, contato clicável, tema dia/noite, modos sem 3D e sem GSAP |
| `apresentacao/` | Deck de 12 slides para produtores (PT; também houve ES e IT) | Ritmo noite/dia/dourado, o slide da viagem como momento principal |
| `video/` | Filme de 42 s: SPEC, `index.html`, 5 cenas, fontes | SPEC com números, costuras em quadros idênticos, garrafa 3D renderizada por quadro |

## Como abrir
- Site: `python -m http.server 8765 --directory site` e abra `http://localhost:8765`.
- Filme: copie `video/` para uma pasta de trabalho, rode `npx hyperframes preview` (veja `references/video.md`). As imagens que as cenas usam estão em `video/assets/img/`.

## Limites conhecidos (não copie sem pensar)
- A foto do estande do Covabra mostra a promotora; o consentimento ainda precisava ser confirmado.
- A `og:image` não foi definida porque o domínio final não existia.
- O filme saiu sem trilha (catálogo de música exigia login na HeyGen).
