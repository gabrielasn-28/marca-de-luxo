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
- **Som**: filme com mais de 15 s que conta uma história leva trilha e som nas ações visíveis (a rolha, o líquido, o vento no mapa). Leia `hyperframes/references/sound.md`. Sem login na HeyGen, use música livre do Openverse (CC0 ou CC BY): veja "Trilha e mistura de áudio" abaixo. Só entregue sem som se nada servir, e avise.
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
- **Música**: o catálogo grátis da HeyGen exige o programa `heygen`, que não tem versão para Windows (só WSL). A primeira versão saiu sem som; a final usa trilha do Openverse (seção abaixo).
- **Versões em outros idiomas**: só os textos mudam; use as traduções de `apresentacao.md`.

## Locução sincronizada (método testado no filme da Ganesh)
- Pergunte antes: voz (gênero, idade, tom), relação com o texto da tela ("a voz conta, a tela resume" é o padrão), ferramenta (ElevenLabs, HeyGen ou locutor) e idiomas. Pergunte também como a empresa pronuncia o próprio nome.
- **Uma fala por momento do filme, cada uma gerada como arquivo separado.** Uma locução corrida com pausas acumula erro de ritmo e dessincroniza. Cada fala tem: segundo de início (2 a 3 quadros antes da palavra-chave aparecer na tela), tempo-limite (a próxima transição), texto e direção de voz. Para cada uma, deixe também um texto curto de reserva.
- Ritmo de cálculo em português: cerca de 2,4 palavras por segundo com speed 0.92.
- ElevenLabs: modelo Multilingual v2 (o v3 ignora `<break time="0.3s" />`), stability 55%, similarity 80%, style 20%. Escreva nomes estrangeiros como se pronunciam (`Champanhe`, `Bordô`).
- No HyperFrames, cada fala vira um `<audio>` com `data-start`. Meça cada arquivo com `npx hyperframes audio <arquivo> --json` antes do render. A música abaixa sob a voz e fica cheia nos respiros (valores medidos na seção "Trilha e mistura de áudio").
- Modelo completo: `GANESH/video/LOCUCAO.md` (copie para `assets/exemplo-ganesh/video/` ao atualizar o exemplo).
- **Se a pessoa gerar a locução numa peça só** (comum: o modelo v3 ignora as pausas e o áudio fica curto), não tente acertar pausas. Rode `ffmpeg -af silencedetect=noise=-38dB:d=0.25`, case os trechos de voz com as falas do roteiro, corte cada fala com 0,05 s de folga e fades curtos, e ponha cada uma como `<audio>` no segundo da sua transição. Alterne faixas (`data-track-index` 2 e 3) quando as caudas se sobrepõem. Para provar, misture as falas com `adelay` e meça os inícios com `silencedetect`.

## Trilha e mistura de áudio (lições de 18/11/2026)
- **Voz sumida ou efeitos mais altos que ela**: meça com `ffmpeg -af loudnorm=print_format=json` antes de renderizar. No filme da Ganesh a voz chegou em −31 LUFS e os efeitos ficaram até 18 dB acima dela. Tratamento que resolveu: corte de graves em 75 Hz, compressão leve 2,5:1, **um único ganho para todas as falas** (preserva o equilíbrio entre elas), limitador a −1,5 dBFS. Meta da locução: −16 LUFS; filme final entre −16 e −14 LUFS, pico até −1 dBTP. Guarde os originais e ponha os tratados numa pasta `voz/tratada/`.
- **Efeitos**: 8 a 15 dB abaixo da voz durante a fala, sozinhos nos respiros. Efeito com pico alto e corpo fraco (líquido servindo) ganha uma cópia nivelada.
- **Silêncios**: renderize e rode `silencedetect`. Meta: nenhum silêncio acima de 0,4 s num filme narrado. Respiro inevitável se cobre com efeito sonoro (mar, sopro de câmera), entrando um pouco antes da imagem.
- **Falas de ligação**: se a voz deixa buracos de 1,5 a 3 s entre as falas, escreva falas curtas extras para preenchê-los e regenere a locução inteira com a mesma voz.
- **Voz indisponível**: a voz de biblioteca pode sumir da conta. Regenere tudo com outra voz (Multilingual v2, speed 1.0) em vez de misturar vozes.
- **Música livre sem login**: procure no Openverse (`api.openverse.org`) licenças **CC0 ou CC BY**. Não use CC BY-NC nem ND. Salve o original, a edição e um `CREDITS.md`. **CC BY exige o crédito em todo lugar onde o filme for publicado**; avise a pessoa na entrega.
- **Edição da trilha para a duração do filme**: use a introdução suave nos primeiros segundos, emende a 0,3 s escondida sob um efeito ou a voz, e posicione o clímax da música no clímax visual. Fade-out nos últimos 1,5 a 2 s.
- **Ducking manual** no `data-automation` do `<audio>` da trilha: volume cheio nos respiros, cerca de 0.28 sob a voz e 0.21 sob o clímax; confira que a música fica ~13 dB abaixo da voz. Não ligue o carve automático junto: as curvas se somam.
- **Render**: use sempre `--no-best-effort`. Um render com aviso `media_readiness_timeout` perdeu o desfoque de movimento em 1 de cada 4 quadros. Compare com o render bom anterior por SSIM e confira o áudio final com `loudnorm` e `silencedetect`.
- **Pronúncia**: pergunte e escreva o nome da marca como se fala (Ganesh → `Ganésh`, tônica em "nésh").
- **Sem Python 64 bits não há MusicGen local**: não prometa música gerada; use banco livre.
