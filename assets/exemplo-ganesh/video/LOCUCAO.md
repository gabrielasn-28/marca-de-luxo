# Locução do filme "A viagem do seu vinho" (Ganesh Vinhos, 42 s)

Voz feminina, madura e calorosa. A voz conta, a tela resume: a palavra-chave que aparece na tela é dita no mesmo instante. Gerar no ElevenLabs, **uma fala por vez** (cada fala vira um arquivo), para cada uma começar no segundo exato da sua transição.

## Configuração no ElevenLabs

| Item | Valor |
|---|---|
| Modelo | **Eleven Multilingual v2** (o v3 não respeita as pausas `<break>`) |
| Voz | Voice Library → filtros: Language **Portuguese**, Accent **Brazilian**, Gender **Female**, Age **Middle aged**; procure por "narration", "warm" ou "elegant". Ouça as amostras e escolha uma voz grave, calma e sem sotaque de propaganda de varejo. |
| Stability | 55% |
| Similarity | 80% |
| Style exaggeration | 20% |
| Speaker boost | ligado |
| Speed | 0.92 (se uma fala passar do tempo-limite, suba para 1.0) |
| Formato | MP3 44,1 kHz 192 kbps ou WAV |

Use a **mesma voz e as mesmas configurações em todas as falas**. Gere cada fala 2 ou 3 vezes e fique com a mais natural.

## As falas (copie o texto da coluna "Texto para colar" exatamente como está)

O "Começa em" é o segundo do filme em que o arquivo deve começar a tocar. O "Termina até" é o limite: se a fala passar, use o texto curto da linha abaixo dela.

| # | Arquivo | Começa em | Termina até | O que acontece na tela | Texto para colar | Direção da voz |
|---|---|---|---|---|---|---|
| 1 | `voz-01.mp3` | **0,4 s** | 2,2 s | Macro da cápsula dourada, a garrafa girando e a luz correndo no vidro | `Toda garrafa faz uma viagem.` | Baixo, íntimo, quase um segredo. |
| 2 | `voz-02.mp3` | **2,3 s** | 5,8 s | "Do vinhedo" (2,35 s) e "à mesa brasileira." (2,7 s) surgem ao lado da garrafa; depois a câmera mergulha no elefante dourado | `Do vinhedo onde ela nasce... <break time="0.3s" /> até a mesa brasileira.` | Calmo, com orgulho. "mesa brasileira" um pouco mais aberto. |
| 3 | `voz-03a.mp3` … `voz-03d.mp3` *(opcional)* | **7,35 s / 7,95 s / 8,55 s / 9,15 s** | 0,5 s cada | Montagem: a câmera salta entre as regiões e o nome aparece grande | `Champanhe.` · `Bordô.` · `Douro.` · `Toscana.` | Sussurrado, elegante, uma palavra só. Cada nome é um arquivo. |
| 4 | `voz-04.mp3` | **9,75 s** | 12,5 s | Europa inteira; aparece "Começa com quem faz o vinho." (9,9 s) | `Tudo começa com quem faz o vinho.` | Caloroso, firme. Ênfase leve em "quem faz". |
| 5 | `voz-05.mp3` | **14,1 s** | 17,4 s | A câmera segue o navio cruzando o Atlântico; aparece "Atravessa o oceano…" (14,3 s) | `Atravessa o oceano com a nossa própria logística.` | Seguro, um pouco mais de movimento, como quem viaja. |
| 6 | `voz-06.mp3` | **19,0 s** | 23,0 s | Chegada ao litoral; os portos acendem; aparece "Chega ao porto sem intermediários." (19,15 s) | `Chega ao porto sem intermediários... <break time="0.2s" /> e segue direto para quem vende.` | Firme na primeira parte; mais leve em "direto para quem vende". |
| 7 | `voz-07.mp3` | **25,2 s** | 28,9 s | O elefante dourado vira moldura da foto do Covabra; aparece "Ganha a gôndola." (25,3 s) | `Ganha a gôndola... <break time="0.2s" /> e a atenção de quem escolhe.` | Sorriso na voz. |
| 8 | `voz-08.mp3` | **31,25 s** | 35,9 s | A garrafa chega girando e serve; aparece "E termina na taça…" (31,35 s); a taça enche e o vinho toma a tela | `E termina na taça de quem prova o seu vinho... <break time="0.2s" /> pela primeira vez.` | Lento, emocionado, sem dramatizar. "pela primeira vez" quase sussurrado. |
| 9 | `voz-09.mp3` | **37,45 s** | 38,3 s | O ouro sobe dentro do elefante e as letras de GANESH se aproximam | `Ganésh.` | Uma palavra, assinada, com calma. |
| 10 | `voz-10.mp3` | **38,7 s** | 41,8 s | Aparece "O seu vinho já tem uma casa no Brasil." palavra por palavra | `O seu vinho já tem uma casa no Brasil.` | A frase mais quente do filme. Terminar com a voz descendo, sem pressa. |

### Textos curtos (use se a fala passar do "Termina até")

| # | Texto curto |
|---|---|
| 2 | `Do vinhedo... <break time="0.2s" /> à mesa brasileira.` |
| 4 | `Começa com quem faz o vinho.` |
| 5 | `Atravessa o oceano com a nossa logística.` |
| 6 | `Chega ao porto sem intermediários.` |
| 7 | `Ganha a gôndola.` |
| 8 | `E termina na taça de quem prova o seu vinho.` |
| 10 | `O seu vinho tem casa no Brasil.` |

## Pronúncia

- **Ganesh**: a empresa pronuncia **Ga-NÉSH** (confirmado). Escreva sempre `Ganésh` no texto da voz para ela acentuar o "né".
- **Champagne** e **Bordeaux** vão escritos como se falam (`Champanhe`, `Bordô`), para a voz não ler em inglês.
- Se alguma palavra sair errada, reescreva como se fala; o texto na tela continua com a grafia correta.

## Mixagem (feita no projeto do vídeo)

- Música por baixo da voz em torno de 14% de volume (sobe para 100% nos trechos sem fala: 6–9,7 s, 17,4–19 s, 23–25,2 s, 29–31,2 s e no final).
- Cada fala com o pico 1 quadro depois da imagem a que ela se refere (a luz chega antes do som).
- Volume final entre −16 e −14 LUFS, pico máximo −1 dBTP.

## Entrega dos arquivos

Salve os arquivos em `GANESH/video/assets/voz/` com os nomes da tabela. A sincronização no vídeo é feita no projeto do HyperFrames: cada arquivo vira um `<audio>` com o `data-start` da coluna "Começa em", e a duração real de cada um é medida antes do render.

## Como foi sincronizado (18/11/2026)
O áudio do ElevenLabs veio numa peça só, com 32,4 s e as pausas ignoradas (todos os silêncios com ~0,4 s, sinal de geração no modelo v3). Os 17 trechos de voz foram detectados com `ffmpeg silencedetect`, cortados em 13 arquivos (`assets/voz/voz-*.wav`, começando 0,05 s antes da voz e com fades de 20 ms e 60 ms) e postos no `index.html` como `<audio>` no segundo de cada transição. Uma mistura de teste mediu cada início: todos batem com o planejado, ao centésimo de segundo.

## Falas de ligação (preenchem os silêncios; geradas em 18/11/2026)
Mesma voz e configurações das outras falas (Multilingual v2, speed 0.92: a aceleração de 8% é aplicada depois, no corte). Gere cada uma como arquivo separado.

| Arquivo | Começa em | Cabe até | Na tela | Texto para colar | Direção |
|---|---|---|---|---|---|
| `voz-05b.mp3` | 16,3 s | 18,1 s | O navio termina a travessia e a câmera desce para o litoral | `Cada contêiner, acompanhado de perto.` | Confiante, tranquilo. |
| `voz-06b.mp3` | 22,3 s | 24,3 s | A câmera mergulha no ponto do Covabra e o elefante dourado nasce dele | `Até o interior de São Paulo.` | Leve, com sorriso. |
| `voz-07b.mp3` | 27,4 s | 30,2 s | A foto do Covabra no elefante, antes do chicote para a taça | `Com degustação... e alguém contando a sua história.` | Próximo, caloroso; pequena pausa depois de "degustação". |

## Versão final da voz (18/11/2026)
Voz original ficou indisponível na conta. Locução inteira regenerada com **Fabi - Portuguese (BR)** (Voice Library), Eleven Multilingual v2, velocidade 1.0, já com as falas de ligação. Arquivo bruto: `assets/voz/locucao-fabi-original.mp3` (50 s). Cortada em 16 falas e posta no `index.html`; a voz corre contínua de 13,3 s a 34,7 s e só restam 3 respiros > 1 s (5,2 s, 11,6 s e 34,7 s), todos cobertos por efeitos sonoros.

## Mixagem corrigida (18/11/2026, manhã)
O render de 17/11 23h04 tinha 6 silêncios totais de 1,7 a 3,2 s (só voz, −23 LUFS). Na versão com a voz Fabi, a voz estava em −31 LUFS e os efeitos chegavam a 18 dB acima dela (o grave da taça em −14 LUFS).
- **Voz**: `assets/voz/tratada/` = as mesmas 16 falas com corte de graves em 75 Hz, compressão leve (2,5:1) e um ganho único de +18 dB, para manter o equilíbrio entre as falas; limitador a −1,5 dBFS. Locução em −16 LUFS. Os originais seguem em `assets/voz/`.
- **Efeitos**: 8 a 15 dB abaixo da voz durante a fala; sozinhos nos respiros. O vinho servido ganhou uma cópia nivelada (`assets/sfx/liquido-servindo-nivelado.wav`), porque o original tinha picos altos e corpo em −36 LUFS.
- **Respiro de 11,6–13,3 s**: o mar entra em 11,9 s (antes da imagem, abaixando quando a voz volta) e um sopro novo em 12,55 s acompanha a câmera abrindo para o Atlântico.
- No render, cada fala toca a 0.8 (−2 dB): o player não baixa 3 dB na conversão mono→estéreo, como o ffmpeg faz.
- Resultado medido no render final (`renders/video_2026-11-18_09-34-57.mp4`): −15,3 LUFS, pico −2,8 dBTP; nenhum silêncio acima de 0,4 s, exceto 0,9 s no fim.
- Tomadas "Raquel" em `assets/voz/raquel/` estão incompletas (11 de 16 falas, sem 07, 07b, 08, 09 e 10) e não entram no vídeo.

## Trilha musical (18/11/2026)
- **"A Good Dream", de Jesse Keller**, licença CC BY 3.0, achada no Openverse (Jamendo). O catálogo do HeyGen exige o programa `heygen`, que ainda não tem versão para Windows. **O crédito é obrigatório onde o vídeo for publicado**: o texto está em `assets/trilha/CREDITS.md`.
- Edição de 42 s (`assets/trilha/a-good-dream-editada.wav`): filme 0–30,4 s = introdução suave da música; emenda de 0,3 s em 30,25 s, escondida sob o chicote e a voz; o clímax da música cai em 37,15 s, no ouro subindo e logo antes do "Ganésh"; fade-out de 40,2 a 42 s.
- Ducking no `index.html` (`data-automation` da `#trilha-bgm`): volume cheio nos respiros (5,3–7,2 s, 11,7–13,3 s, 34,8–37,4 s e o final), 0.28 sob a voz e 0.21 sob o clímax. Medido: a música fica 13 dB abaixo da voz durante a fala e 4,5 dB abaixo do nível da fala nos respiros. O carve automático não foi usado, porque a curva de volume dele somaria com esse ducking.
- Render final: `renders/video_2026-11-18_10-53-13.mp4` — −15,2 LUFS, pico −2,6 dBTP, nenhum silêncio no filme (só os 0,2 s iniciais). Renderizar com `--no-best-effort`: um render com aviso `media_readiness_timeout` saiu com 1 a cada 4 quadros sem desfoque de movimento na gôndola (24,9–25,4 s).
