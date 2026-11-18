# Fase 7: filme da marca (16:9, 30 a 60 s)

O filme é o site contado em tempo. Mesmas cores, fontes, logo, objeto herói e cenário; a mesma história; a mesma regra de que a ousadia fica num lugar só. Ele é feito em HTML com GSAP e renderizado quadro a quadro pelo HyperFrames, por isso sai idêntico a cada render e reaproveita o código do site.

Exemplo real: `assets/exemplo-ganesh/video/` (SPEC, `index.html`, 5 cenas em `compositions/`, fontes). O MP4 renderizado (42 s, 1920×1080, 30 fps) fica no projeto da Ganesh, em `GANESH/video/renders/`.

## Formato padrão
- 1920×1080, 30 fps, 30 a 60 s (padrão 45 s). Outros formatos só se a pessoa pedir.
- Áreas seguras: texto a pelo menos 96px das bordas; nada importante nos 5% de cada lado.
- Saída: MP4 H.264 + um quadro de capa (poster) em PNG no melhor momento do filme.

## Estrutura: a mesma do site

| Ato | No site | No filme | Tempo (45 s) |
|---|---|---|---|
| 1. Abertura | Título em volta do objeto herói | O objeto herói em macro, a luz percorrendo, o título revelado palavra por palavra | 0–6 s |
| 2. O momento principal | Seção fixa com 4 a 6 etapas | A cena mais longa: a câmera percorre o cenário seguindo o objeto | 6–24 s |
| 3. A prova real | Foto real na moldura da logo | A foto real (loja, ateliê, campo) entrando pela silhueta da logo | 24–30 s |
| 4. O produto em uso | Portfólio, taça | O produto chegando ao destino (a taça que enche, a joia no corpo) | 30–36 s |
| 5. Assinatura | Encerramento com o símbolo grande | O símbolo e a frase final, parados pelo menos 3 s | 36–45 s |

## Padrão de produção (o que faz parecer filme e não slideshow)
- **Cortes escondidos**: cada passagem de cena acontece num quadro idêntico dos dois lados (ouro vira ouro, vinho vira vinho, a silhueta da logo cresce até virar o fundo). Nada de fade preto entre cenas.
- **Uma câmera que se move**: o espectador sente que viaja. Movimentos de câmera em `power2.inOut`; chegadas em `expo.out` ou `power4.out`; mergulhos em `power3.in`.
- **Um só movimento contínuo** (o balanço do objeto); todo o resto anda e para. Texto que pousou fica parado.
- **Texto de cinema**: entrada por palavra com desfoque de 6px → 0 e opacidade, 0,08 s entre palavras, sem subir. Cada linha fica na tela 0,5 s + 0,3 s por palavra no mínimo.
- **Luz com direção**: luz principal quente de cima à direita, contraluz da cor da marca atrás. Sombra de contato sob o objeto. Sem vinheta além do palco de luz e sem grão.
- **Som**: filme com mais de 15 s que conta uma história leva trilha e som nas ações visíveis (a rolha, o líquido, o vento no mapa). Leia `hyperframes/references/sound.md`. Sem trilha disponível, entregue sem som e avise.
- **Proibido**: partículas flutuando, brilho de lente, cartões de vidro, três cards em fila, rótulos 01/02, logo parada num canto, rótulo inventado no produto, rosto de cliente sem autorização.

## Fluxo
1. Leia `hyperframes/SKILL.md`; para filme de marca, também `hyperframes/references/types/launch.md` e `references/story.md`.
2. **Três roteiros só em palavras**, diferentes de verdade (por exemplo: "A viagem", "Um dia na adega", "Cinco taças"). Cada um com 5 linhas, uma por ato. A pessoa escolhe.
3. **`SPEC.md`**: cada adjetivo vira número. Modelo em `assets/modelos/spec-video.md`; exemplo real em `assets/exemplo-ganesh/video/SPEC.md`. Seções: GOAL, OUTPUT, TIME, LOOK (cores, fontes e tamanhos em px e % da altura, luz), OBJECTS, MOTION (curvas e durações), SHOTS (cada plano com tempo de início e fim e a costura com o seguinte), BANNED, QA (os quadros que serão conferidos).
4. **Projeto**: `npx hyperframes init video --skip-skills --skill=hyperframes`. Em `assets/`: logo SVG, imagens WebP do site e as fontes woff2 com `@font-face` (só as fontes do pacote resolvem pelo nome).
5. **Cenas**: uma sub-composição por ato em `compositions/`; o `index.html` só monta as cenas, o áudio e as fábricas compartilhadas (como a do objeto 3D).
6. **Revisão**: `check --json` sem erros → `snapshot --review` nos tempos do QA → `REVIEW.md` com o que corrigir → `preview` para a pessoa aprovar.
7. **Render** só depois da aprovação. Confira o arquivo com `ffprobe` (duração, 1920×1080, 30 fps, faixa de áudio se houver) e assista ao MP4 inteiro antes de entregar.

## Ferramentas e requisitos
- Node.js 22+ e FFmpeg/FFprobe (instalação só com autorização; veja `dependencias.md`). `npx hyperframes doctor --json` antes de tudo; o Chrome vem com `npx hyperframes browser ensure`.
- Comando da skill: `node <skills>/hyperframes/scripts/plugin-cli.mjs <comando>`, dentro da pasta do vídeo.
- Prévia: `preview --background --port 3017`, em `http://localhost:3017/#project/video`.

## Regras do contrato do HyperFrames que mais pegam
- Todo elemento com tempo tem `class="clip"`, `data-start` e `data-duration`. Uma linha do tempo pausada por composição, registrada em `window.__timelines[id]`.
- Nada de `Date.now()`, `Math.random()` sem semente, `repeat:-1`, `fetch` ou timers: o render precisa dar o mesmo quadro sempre.
- Não anime `display`, `visibility` nem `autoAlpha` no `.clip`; anime um filho dele.

## Lições do filme da Ganesh (42 s, "A viagem")
- **Three.js no render**: r147 em script comum (`build/three.min.js` + `examples/js/environments/RoomEnvironment.js`) no `<head>` do `index.html`. A fábrica do objeto (`window.GaneshGarrafa`) fica no `index.html`; cada cena cria a sua com `preserveDrawingBuffer: true` e desenha no `onUpdate` da linha do tempo, o que funciona com o seek. Registre `window.__hf.buildReady[id] = promessa` para texturas que carregam (o elefante).
- **Luz na r147**: com `physicallyCorrectLights = true`, a intensidade do site deixa o vidro verde e claro. Use SpotLight 60, vidro `0x020302`, metalness 0.35 e envMapIntensity 1.5.
- **Fontes**: woff2 latino do Google Fonts em `assets/fonts`, com `@font-face` em **cada** cena, ou o lint falha.
- **Avisos do `check` e a solução**:
  - `first_frame_empty`: o objeto já visível no quadro 0.
  - `dead_stretch` (mais de 3 s sem mudança): um elemento que conta a história, como o navio percorrendo a rota com `getPointAtLength` no `onUpdate`, ou a aproximação lenta da foto.
  - `line_unread`: segure cada linha 0,5 s + 0,3 s por palavra.
  - `text_occluded`: rótulos sob o véu do texto; reenquadre.
  - `duplicate_media_discovery_risk`: duas `<img>` com o mesmo arquivo; use uma cópia com outro nome.
- **Transições que funcionaram**: o elefante da garrafa cresce até virar o fundo dourado (o objeto vira o mundo); zoom pelo ponto de destino no mapa; a silhueta da logo se abre sobre a foto real; chicote lateral com desfoque casando a velocidade; o vinho transborda e cobre a tela, depois escoa revelando a assinatura.
- **Música**: o catálogo grátis exige login na HeyGen (`auth login`). Sem login, o filme saiu sem som e isso foi dito na entrega.
- **Versões em outros idiomas**: só os textos mudam; use as traduções de `apresentacao.md`.

## Locução sincronizada (método testado no filme da Ganesh)
- Pergunte antes: voz (gênero, idade, tom), relação com o texto da tela ("a voz conta, a tela resume" é o padrão), ferramenta (ElevenLabs, HeyGen ou locutor) e idiomas. Pergunte também como a empresa pronuncia o próprio nome.
- **Uma fala por momento do filme, cada uma gerada como arquivo separado.** Uma locução corrida com pausas acumula erro de ritmo e dessincroniza. Cada fala tem: segundo de início (2 a 3 quadros antes da palavra-chave aparecer na tela), tempo-limite (a próxima transição), texto e direção de voz. Para cada uma, deixe também um texto curto de reserva.
- Ritmo de cálculo em português: cerca de 2,4 palavras por segundo com speed 0.92.
- ElevenLabs: modelo Multilingual v2 (o v3 ignora `<break time="0.3s" />`), stability 55%, similarity 80%, style 20%. Escreva nomes estrangeiros como se pronunciam (`Champanhe`, `Bordô`).
- No HyperFrames, cada fala vira um `<audio>` com `data-start`. Meça cada arquivo com `npx hyperframes audio <arquivo> --json` antes do render. Música a cerca de 0.14 sob a voz e cheia nos intervalos sem fala.
- Modelo completo: `GANESH/video/LOCUCAO.md` (copie para `assets/exemplo-ganesh/video/` ao atualizar o exemplo).
- **Se a pessoa gerar a locução numa peça só** (comum: o modelo v3 ignora as pausas e o áudio fica curto), não tente acertar pausas. Rode `ffmpeg -af silencedetect=noise=-38dB:d=0.25`, case os trechos de voz com as falas do roteiro, corte cada fala com 0,05 s de folga e fades curtos, e ponha cada uma como `<audio>` no segundo da sua transição. Alterne faixas (`data-track-index` 2 e 3) quando as caudas se sobrepõem. Para provar, misture as falas com `adelay` e meça os inícios com `silencedetect`.
