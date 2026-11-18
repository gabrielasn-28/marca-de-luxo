# Fase 5: checklist de teste do site

## Prévia local
`.claude/launch.json` na raiz do projeto:
```json
{"version":"0.0.1","configurations":[{"name":"site","runtimeExecutable":"python","runtimeArgs":["-m","http.server","8765","--directory","site"],"port":8765}]}
```
Abra com `preview_start` e o nome da configuração. O artefato publicado pode pedir login no navegador interno; teste sempre pela prévia local.

## Painel oculto = animação em câmera lenta
Se `tabs_context` disser que o painel está oculto, o requestAnimationFrame fica limitado. Antes de cada captura de tela:
```js
gsap.globalTimeline.getChildren(false,true,true).forEach(t=>{if(!t.scrollTrigger&&t.repeat()!==-1)t.progress(1)}); GARRAFA.sujo=true;
```
Para chegar a uma etapa da rolagem: `scrollTo(0, pinSpacer.offsetTop + innerHeight * N)` e espere uns 2 segundos.

Com o painel oculto também ficam parados os eventos `scroll`, o ResizeObserver e o IntersectionObserver. Para testar cliques e rolagem suave, gire o relógio do GSAP à mão:
```js
const pump = async ms => { const t = performance.now(); while (performance.now() - t < ms) { gsap.ticker.tick(); await new Promise(r => setTimeout(r, 16)); } };
scrollTo(0, y); dispatchEvent(new Event("scroll")); await pump(1500);
```
Não force `progress(1)` em todos os scrub tweens de uma vez: o da abertura reescreve o objeto 3D compartilhado e o teste mostra um estado que o usuário nunca vê. Recarregue com uma URL nova (`?v=N`) entre testes, porque o estado da Lenis fica sujo. Se `preview_start` cair numa porta trocada (o `http.server` ignora a porta atribuída), use a prévia que já responde em 8765.

## Passe por tudo
- [ ] Computador (1440×860) e celular (`resize_window` com preset mobile): `scrollWidth === innerWidth`.
- [ ] Abertura: título inteiro, sem acento cortado; objeto 3D entre os títulos, sem encostar no texto.
- [ ] Cada etapa do momento principal: texto legível e nada saindo da tela (rótulos, objeto).
- [ ] Portfólio: o produto cabe inteiro na altura da tela; percurso horizontal ≤ 3,5 telas; contador chega a "10 / 10" com o último cartão inteiro na tela; setas, teclado e gesto lateral andam um cartão.
- [ ] Modo sem animação: o portfólio rola de lado sozinho (simule com `ScrollTrigger.getAll().forEach(s => s.kill(true))` e remova `.fixa`).
- [ ] Celular: em cada etapa, o objeto 3D não cobre rótulo nem foto (compare retângulos).
- [ ] Celular: todo efeito de hover tem versão de toque (toque no item e confira que algo aparece).
- [ ] Tema dia e tema noite em todas as seções.
- [ ] Console sem erros (`read_console_messages` com `onlyErrors`).
- [ ] Nenhuma foto de pessoa sem autorização, nenhum dado inventado.
- [ ] Ao terminar o teste, volte o viewport para `desktop`.
