# Fase 5: arquitetura técnica do site e armadilhas já resolvidas

## Pilha (versões fixas, testadas)
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
```
O Three.js r160 não tem mais build UMD; use o importmap e `<script type="module">`.

## Garrafa/objeto 3D fixo atravessando a página
- `<canvas id="cena">` fixo em tela cheia, com `z-index` acima das seções e `pointer-events:none`. Ele não pode ficar abaixo, porque a seção fixada pelo ScrollTrigger cria o próprio contexto de empilhamento.
- O estado fica num objeto JS compartilhado (`window.GARRAFA = {x,y,rz,giro,s,op,sujo}`). O GSAP anima esse objeto, e o loop do Three.js lê e desenha.
- Converta a posição de um elemento HTML em coordenadas 3D com câmera de fov 30 e z 16: `visH = 2*16*tan(15°)`, `x = (fração - .5) * visW` e `y = -(fração - .5) * visH`. Assim o objeto encaixa num espaço reservado do layout (`#lugar-garrafa`).
- Um objeto simbólico também funciona bem: LatheGeometry com o perfil da garrafa, cápsula dourada e a logo como textura (canvas a partir do SVG) num cilindro parcial.

## Desempenho (o site travava; isto resolveu)
1. **Desenhar sob demanda:** só chame `renderer.render` quando `sujo` for verdadeiro. Todo `onUpdate` do GSAP marca `sujo = true`.
2. `setPixelRatio(min(dpr, 1.5))`; antialias desligado no celular; geometria com menos segmentos no celular.
3. MeshStandardMaterial com envMap forte imita bem o vidro. Evite MeshPhysicalMaterial com clearcoat e transmission, que custam caro.
4. **Mapa: imagem e não SVG.** Um SVG de 80 KB dentro de um elemento com `transform: scale` era redesenhado a cada quadro. Agora são duas WebP: o mundo em 2x e um detalhe em alta para o zoom, que aparece por cima com máscara radial para esconder a emenda.
5. Anime só `transform` e `opacity`; coloque `will-change: transform` só na câmera e no trilho.
6. Animação contínua, como o balanço do objeto, fica pausada quando a abertura sai da tela.
7. Lenis só com `(pointer: fine)`. No toque, a rolagem nativa é mais fluida. Integração: `lenis.on('scroll', ScrollTrigger.update)`, `gsap.ticker.add(t => lenis.raf(t*1000))` e `gsap.ticker.lagSmoothing(0)`.
8. `scrub: .6` (em vez de 1), `anticipatePin: 1`, imagens com `loading="lazy"` e `decoding="async"` fora da primeira tela.

## Armadilhas reais (cada uma já quebrou o site)
- **Faltava `<meta charset="utf-8">`**: os acentos quebram no servidor local. Inclua também a meta de viewport, senão o celular renderiza com 980px.
- **`fromTo` com `immediateRender: false`** na saída da abertura. Com `to` simples, a animação guardava o valor de antes da entrada e o objeto ficava preso.
- Posicione o objeto **depois de `document.fonts.ready`** e chame `ScrollTrigger.refresh()`. A troca de fonte muda a altura do layout.
- Título revelado com máscara (`overflow: hidden`): use `padding: .14em 0 .16em` com margem negativa igual, senão acentos e descendentes ficam cortados.
- Imagem que acompanha o cursor: esconda também no `mouseleave` da lista e na rolagem. Sem isso, ela fica presa na tela.
- **Tudo que depende de hover precisa de um equivalente no toque.** No celular a garrafa que segue o cursor nunca aparecia (a Gabriela tocava nos produtores e nada acontecia). Com `(hover: none)`, cada item abre a imagem embaixo do nome (`grid-template-rows: 0fr → 1fr`, imagem `loading="lazy"` dentro do bloco escondido, `role=button`, `aria-expanded`, Enter/Espaço), com um "+" que gira; abrir um fecha o anterior.
- `history.scrollRestoration = "manual"` evita abrir no meio da seção fixada.
- Cabeçalho fixo transparente se sobrepõe ao texto. Use um gradiente da cor de fundo para transparente.
- A trilha de etapas no celular vira 5 barras finas no topo. O texto fica embaixo, sobre um véu em gradiente (`--veu`).
- Rótulos de SVG dentro da câmera escalam junto. Calcule o tamanho da fonte para o zoom final (no zoom de 3,4x, fonte de 3,4).

## Portfólio horizontal (a Gabriela reclamou que "ficava muito longe")
A v1 tinha 10 painéis de 76vw: 9.536 px de rolagem vertical (11 telas) só para atravessar o portfólio. A versão atual usa 2.930 px.
- **Meça o percurso**: `st.end - st.start` deve ficar em até ~3,5 alturas de tela. Colunas estreitas (`clamp(270px,27vw,400px)`) deixam três produtos à vista e encurtam o trilho. Mapeamento 1 px vertical para 1 px horizontal.
- **Título dentro da parte fixa**: o cabeçalho da seção (título, contador "01 / 10", barra de progresso e setas ← →) fica dentro do `#faixa` fixado. Título solto acima do trilho cria um vão e parece que o carrossel está longe.
- **Modo nativo por padrão**: o trilho tem `overflow-x:auto` com `scroll-snap`. O GSAP só adiciona `.fixa` dentro do `gsap.matchMedia()` e devolve uma limpeza que remove a classe. Assim, sem JS, com "reduzir movimento" ou sem WebGL, o portfólio continua navegável (antes ficava preso no 1º produto).
- Setas, teclado (← → quando a seção está no meio da tela) e gesto lateral do trackpad (`wheel` com `deltaX` dominante vira rolagem vertical) vão de cartão em cartão: posição = `cartao.offsetLeft - paddingLeft(trilho)`, convertida para rolagem com `st.start + x * len / dist`.
- O contador segue o progresso da **animação** (`onUpdate(){ this.progress() }`), não o do ScrollTrigger; com `scrub` o trilho vem atrasado e o número pularia na frente.
- Nome do país em contorno: uma vez por grupo, com tamanho `min(7.4vw, calc(var(--cw) * var(--g) * 1.4 / var(--c)))` (`--g` = produtos do país, `--c` = letras). Sem isso, países com um produto só se sobrepõem.
- `dist = trilho.scrollWidth - document.documentElement.clientWidth` (não `innerWidth`, que inclui a barra de rolagem do Windows).

## Mais armadilhas (rodada do portfólio)
- **`onUpdate` roda durante a criação do ScrollTrigger.** Referenciar a própria `const` (`mov.progress()`) dá "Cannot access before initialization" e quebra todas as seções fixas. Use `function(){ this.progress() }`.
- **Lenis mede o limite de rolagem antes dos pin-spacers.** Adicione `ScrollTrigger.addEventListener("refresh", () => lenis.resize())`.
- **`lenis.targetScroll` só vale durante rolagem suave** (`lenis.isScrolling === "smooth"`); fora disso use `scrollY`, senão um clique depois de rolar pelo teclado leva a página para trás.
- **Entrada e saída do objeto 3D em propriedades separadas** (`op` da abertura × `fim` antes do portfólio). Com uma só, quem clica no menu logo ao abrir vê o objeto por cima do portfólio.
- **Canvas 3D com altura estável (lvh).** Com `position:fixed; inset:0`, o canvas muda de altura no iPhone quando a barra do Safari aparece ou some, a projeção muda e o objeto escorrega para cima do texto (a Gabriela viu a garrafa "bem no meio da escrita"). Use `#cena{top:0;height:100vh;height:100lvh}`, meça essa altura com uma sonda (`window.ALTURA3D()`, um div fixo de `100lvh`) e use-a no `renderer.setSize`, no `camera.aspect`, em `visW` e nas frações `fy()`.
- **Posição de descanso no celular a partir de medidas, não de palpite.** Em 390×664 os nomes do mapa iam até ~35% da altura e o texto da etapa começava em ~60%: a garrafa fica à direita, em `fy(.5)`. Teste também 375×667 e 430×740.
- **No celular, confira cada etapa com caixas**: calcule o retângulo do objeto 3D (`cx = (.5 + x/visW) * W`, meia largura `s * W/visW`, meia altura `2.72 * s * H/visH`) e compare com rótulos e fotos. A garrafa cobria "Santos" e a foto do Covabra.
- Cabeçalho recolhe ao descer e volta ao subir (`.recolhido:not(:focus-within)`); o menu marca a seção atual com `aria-current` via IntersectionObserver (`rootMargin: "-50% 0px -50% 0px"`).
- Contato clicável: `tel:`, `wa.me/...?text=` com mensagem pronta diferente por botão, endereço com link do Google Maps. Inclua favicon SVG, `theme-color` por tema e Open Graph (a `og:image` exige URL absoluta, então só depois do domínio).

## Tema dia/noite
- Estrutura de tokens: escuro no `:root`; claro em `@media (prefers-color-scheme: light) :root:not([data-theme="dark"])` e em `:root[data-theme="light"]`.
- Nenhuma cor literal nos componentes: brilho, contorno, sombra e véu também são tokens.
- Botão alterna `data-theme` e salva no `localStorage` com try/catch. Um script no topo aplica o tema salvo antes de pintar a página.
- **Tema padrão é decisão da cliente** (pergunte na rodada 2). A Ganesh escolheu o **dia como padrão**: o script do topo aplica `data-theme` = tema salvo ou `"light"`, ignorando o modo escuro do aparelho; o botão só alterna entre `light` e `dark`. Use uma única `<meta name="theme-color" id="cor-barra">` e troque o `content` junto com o tema. Com padrão automático, mantenha os blocos `prefers-color-scheme`.
- Mapas em WebP transparente com traço dourado funcionam nos dois temas.

## Sem movimento
- **"Reduzir movimento" não desliga a experiência** (a Gabriela usa iPhone com ele ligado e queria ver a animação): a viagem guiada pela rolagem continua; saem só movimentos automáticos (entrada do título, balanço, pulso, Lenis, parallax). `sem-movimento` fica só para GSAP fora do ar. **Nunca esconda o mapa**: a Gabriela abriu no iPhone (provavelmente com "Reduzir movimento" ligado) e a viagem "pulava", sem mapa. Agora a `.camera` vira bloco estático (`position:relative; aspect-ratio:1400/1070; transform:none!important`), com rotas já traçadas e portos visíveis; no celular, recorte no Atlântico (`width:150vw; margin-left:-27vw`) e sem rótulos.
- Sem WebGL é outra classe, `sem-3d`: só a garrafa vira foto e o mapa continua animado. Se o 3D não desenhar em 5 s (iOS antigo sem importmap), entra `sem-3d`; o primeiro `render` remove a classe.
- No celular a `.camera` usa `will-change:auto`: camada fixa de 1400px com imagem 2x ampliada estoura a memória de vídeo do iPhone e o mapa some.
- Teste o modo sem animação com uma cópia `_previa-*.html` (ignorada no git) com `const reduz=true`.
