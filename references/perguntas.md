# Fase 2: perguntas

Pergunte depois de pesquisar e só o que a pesquisa não respondeu. No máximo 4 perguntas por vez, cada uma com 2 a 4 opções e uma recomendada ("(Recomendado)" e em primeiro lugar). Cada pergunta precisa mudar o resultado; se não muda, decida você e avise em uma linha.

Registre as respostas no `briefing.md` (modelo em `assets/modelos/briefing.md`).

## Rodada 1: o rumo (obrigatória)
1. **Foco**: "O site novo deve focar em quê?" Opções tiradas do dossiê. Ex.: "Linha de vinhos (Recomendado)", "Os dois negócios separados", "Só o negócio antigo".
2. **Público** (várias respostas): "Quem o site precisa convencer?" Ex.: fornecedores e produtores estrangeiros, lojas e restaurantes (B2B), consumidor final, investidores.
3. **Primeira entrega**: site, apresentação, identidade ou filme. Recomende a que destrava as outras (quase sempre o site, porque ele fixa conceito e tokens).
4. **Logo**: "Tem a logo em alta (SVG, AI, PDF ou PNG grande)?" Opções: "Vou mandar" ou "Pode redesenhar em vetor (Recomendado se só houver imagem pequena)".

## Rodada 2: o gosto e os fatos (quando fizer diferença)
- **Referências**: "Tem sites, marcas ou vídeos de que gosta? Mande links ou prints." Avise que vai usar o gosto e manter o nível dos premiados.
- **Tom**: clássico e silencioso, contemporâneo e ousado, ou caloroso e próximo.
- **Tema**: noite, dia ou os dois com botão (recomendado: os dois). E qual abre por padrão: dia, noite ou o do aparelho.
- **Idiomas**: português apenas, ou também inglês, espanhol, italiano (pense no público da rodada 1).
- **Contatos oficiais**: telefone, WhatsApp, e-mail, Instagram, endereço. Nunca invente.
- **Números grandes**: confirme cada número que vai aparecer em destaque (anos, produtores, rótulos, lojas, clientes).
- **Fotos com pessoas**: as pessoas autorizaram? Se não, só fotos sem rosto.
- **3D**: existem modelos 3D dos produtos (GLB, Blender)? Se não, um objeto simbólico da marca, sem imitar o rótulo de um terceiro.
- **Domínio e publicação**: onde o site vai morar (domínio próprio, Vercel). A imagem de compartilhamento (`og:image`) depende disso.

## Rodada 3: o filme (antes da fase 7)
- **Uso**: site e YouTube, apresentação para parceiros, feira, redes sociais.
- **Duração**: 30, 45 ou 60 s (padrão: 45 s, 16:9, 1920×1080, 30 fps).
- **Roteiro**: apresente 3 roteiros em palavras e peça para escolher um.
- **Som**: trilha do catálogo HeyGen (exige login dela), trilha própria ou sem música. Voz em off: sim ou não.
- **Versões**: idiomas da legenda e do texto na tela.

## Perguntas de ajuste (depois de ver a primeira versão)
Quando a pessoa reclama de algo vago, transforme a reclamação em hipóteses testáveis antes de mexer:
- "Ficou com cara de IA": rode o teste de `padrao-de-qualidade.md` e refaça o conceito, não só as cores.
- "Está muito longe / demora": meça o percurso das seções fixas (`st.end - st.start`) e o tamanho da página.
- "No celular não aparece X": pergunte o aparelho (iPhone ou Android) e o que aparece no lugar (nada, pontos sem fundo, só texto). Suspeite de "Reduzir movimento" ligado ou de camada grande demais na memória de vídeo.

## As perguntas feitas no projeto Ganesh (e as respostas)
| Pergunta | Resposta | Consequência |
|---|---|---|
| Foco do site | Ganesh Vinhos (não o comércio exterior) | ganlog.com.br só no rodapé |
| Público | Produtores estrangeiros e B2B (lojas, restaurantes) | Linguagem de parceria, deck para produtores, versões ES e IT |
| Primeira entrega | Site, depois apresentação institucional para produtores | Tokens e conceito fixados no site |
| Logo | Redesenhar em vetor | `marca/ganesh-simbolo-*.svg` |
| Referências | Fontana, 56° North, Scotch Me, BeerStrasse, MODO, Aakriti, Horizonte | Palco de luz, botões de contorno, nome gigante no fundo, arco como moldura |
| v1 aprovada? | Não: "cara de IA" | Conceito refeito: "A viagem do seu vinho" com mapa e garrafa 3D |
| Portfólio | "A rolagem horizontal está muito longe" | Percurso de 11 telas reduzido para 3,4; título e controles dentro da parte fixa |
| Celular | iPhone: "não aparece o mapa, nem a animação, ele só pula" | "Reduzir movimento" não desliga mais a viagem; o mapa nunca some |
| Fotos do Covabra com clientes | Sem autorização confirmada | Só a foto do estande; consentimento da promotora a confirmar |
| Exemplo da skill | Ganesh + teste de outro setor | `assets/teste-joalheria/` |
| Vídeo padrão | Filme da marca 16:9, 30 a 60 s | `video.md` |
| Celular: produtores | "Ao clicar nos nomes dos vinhos não aparece o vinho" | Toque abre o vinho embaixo do nome |
| Tema padrão | Dia | Site abre no dia em qualquer aparelho; noite pelo botão |

## Como tratar referências fracas
A pessoa pode mandar um template genérico, um site de outro setor ou algo datado.
1. Diga o que vai aproveitar: clima, cor, tipo de foto, uma ideia de estrutura.
2. Ignore em silêncio o que rebaixa o nível: cards iguais, ícones genéricos, carrossel automático, banco de imagens com pessoas posando.
3. Entregue no padrão de `padrao-de-qualidade.md`. Se ela insistir num elemento, faça esse elemento com o acabamento do padrão.
