# Dependências: skills e ferramentas

## As skills já vêm junto

As 19 skills externas abaixo estão guardadas dentro desta skill, em `dependencias/skills.zip` (lista em `dependencias/manifesto.json`, cópia de 18/11/2026). Ficam compactadas de propósito: pastas soltas com `SKILL.md` aqui dentro poderiam aparecer duplicadas para o Claude.

```bash
python ~/.claude/skills/marca-de-luxo/scripts/instalar_dependencias.py --verificar   # o que falta
python ~/.claude/skills/marca-de-luxo/scripts/instalar_dependencias.py               # instala só o que falta
```

Depois de instalar, reinicie a sessão. `--forcar` reinstala todas a partir do pacote (útil se uma foi editada por engano); para versões mais novas, baixe do GitHub pelas fontes da tabela e gere o zip de novo.

## Skills externas (instaladas em `~/.claude/skills`)

| Skill | Fonte (GitHub) | Fase | Para quê |
|---|---|---|---|
| `frontend-design` | anthropics/claude-plugins-official, `plugins/frontend-design/skills/frontend-design` | 3 a 5 | Direção de arte, tipografia, anti-"cara de IA". Leia antes de desenhar. |
| `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-performance`, `gsap-plugins`, `gsap-utils` | greensock/gsap-skills, `skills/` | 5 e 7 | Animação, rolagem fixa, desempenho. `gsap-scrolltrigger` e `gsap-performance` são leitura obrigatória. |
| `gsap-react`, `gsap-frameworks` | idem | 5 | Só se o site for em React, Vue ou Svelte. |
| `threejs-webgl` | freshtechbro/claudedesignskills, `plugins/individual/threejs-webgl/skills/threejs-webgl` | 5 e 7 | Objeto herói em 3D. |
| `lightweight-3d-effects` | idem | 5 | Profundidade em fotos sem modelo 3D (Vanilla-Tilt, Zdog). |
| `barba-js` | idem | 5 | Transição entre páginas, só em sites com várias páginas. |
| `locomotive-scroll` | idem | 5 | Alternativa de rolagem suave; o padrão desta skill é Lenis. |
| `hyperframes` | heygen-com/hyperframes, `skills/` | 7 | Contrato de render HTML → MP4. **Leia primeiro no vídeo.** |
| `hyperframes-cli` | idem | 7 | `init`, `check`, `snapshot`, `preview`, `render`. |
| `hyperframes-registry` | idem | 7 | Efeitos, transições e cartões prontos; procure aqui antes de escrever um efeito. |
| `media-use` | idem | 7 | Música, som, voz; diz o que é grátis e o que exige login na HeyGen. |
| `reverse-any-video`, `style-sampling` | idem | 7 | Quando a pessoa mandar um vídeo de referência ou pedir uma série no mesmo estilo. |

## Skills do próprio ambiente (já disponíveis)

| Skill | Fase | Para quê |
|---|---|---|
| `anthropic-skills:deep-research` | 1 | Pesquisa ampla do setor e dos concorrentes quando a empresa é pouco conhecida ou o setor é novo para você. |
| `anthropic-skills:pdf` | 1 | Catálogos e apresentações antigas em PDF (extrair textos e imagens). |
| `anthropic-skills:built-in-browser` | 1, 5, 7 | Ler sites, testar a prévia local, conferir o site publicado. |
| `artifact-design` | 5, 6 | Regras do artefato quando o site ou o deck forem publicados como artefato. |
| `anthropic-skills:skill-creator` | 8 | Atualizar esta skill e rodar os testes de `evals/`. |

## Ferramentas

| Ferramenta | Fase | Observação |
|---|---|---|
| Python 3 + Pillow, pypdf, numpy | 1, 4 | Scripts em `scripts/`. `pip install pillow pypdf numpy`. |
| Prévia local | 5 | `.claude/launch.json` com `python -m http.server 8765 --directory site`. |
| Git | 5 | Repositório próprio na pasta `site/`. Commit e push só quando a pessoa pedir; cada publicação precisa de uma autorização nova. |
| Vercel | 8 | `vercel.json` de site estático (exemplo em `assets/exemplo-ganesh/site/`). |
| Node.js 22+ e FFmpeg/FFprobe | 7 | Windows: `winget install OpenJS.NodeJS.LTS` e `winget install Gyan.FFmpeg`, **sempre com autorização**. Depois `npx hyperframes doctor --json`. |
| Conta HeyGen (opcional) | 7 | Catálogo de música grátis e voz. Exige o programa `heygen`, que não tem versão para Windows (só WSL). No Windows, use o Openverse (CC0 ou CC BY, com crédito) para a trilha. |
| Conta ElevenLabs (opcional) | 7 | Locução. Modelo Multilingual v2; confirme que a voz escolhida continua na conta. |

## Pilha do site (versões fixas e testadas)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
```

No vídeo, use Three.js r147 em script comum (a r160 não tem build UMD); detalhes em `video.md`.
