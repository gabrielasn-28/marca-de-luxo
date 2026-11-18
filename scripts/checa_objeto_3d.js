// Verificador: o objeto 3D fixo encosta em algum texto, rótulo ou foto?
// Cole no console da prévia (ou rode com javascript_tool) em cada tamanho de celular:
// 390x664 (iPhone com as barras do Safari), 375x667 (iPhone SE), 375x812, 430x740, e 1440x860.
// Requer: window.GARRAFA {x,y,s} e window.ALTURA3D() (altura do canvas em lvh), câmera fov 30 a z 16.
// Ajuste ALVOS e o seletor da seção fixa (.viagem) ao projeto.
const ALVOS = '.abertura h1 .l>span,.abertura .sub,.etapa .n,.etapa h2,.etapa p,.camera text,.janela,.taca,.trilha li,.topo .marca';
const CAIXAS = '.janela,.taca,.trilha li,.topo .marca'; // elementos medidos pela caixa inteira; o resto, pelo texto
const pump = async ms => { const t = performance.now(); while (performance.now() - t < ms) { gsap.ticker.tick(); await new Promise(r => setTimeout(r, 16)); } };
await pump(2500);
const caixa = () => {
  const W = innerWidth, H = ALTURA3D(), visH = 2 * 16 * Math.tan(15 * Math.PI / 180), visW = visH * W / H, B = GARRAFA;
  const cx = (.5 + B.x / visW) * W, cy = (.5 - B.y / visH) * H, hw = B.s * (W / visW), hh = 2.72 * B.s * (H / visH);
  return [cx - hw, cy - hh, cx + hw, cy + hh];
};
const visivel = e => { for (let n = e; n && n.nodeType === 1; n = n.parentElement) { const s = getComputedStyle(n); if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity < .25) return false; } return true; };
const rects = e => { if (e.matches(CAIXAS)) return [e.getBoundingClientRect()]; const rg = document.createRange(); rg.selectNodeContents(e); return [...rg.getClientRects()]; };
const toca = (g, e) => rects(e).some(r => r.width > 2 && !(g[2] < r.left || g[0] > r.right || g[3] < r.top || g[1] > r.bottom));
const checa = nome => { const g = caixa(); const hits = [...document.querySelectorAll(ALVOS)].filter(e => visivel(e) && toca(g, e)).map(e => e.textContent.trim().slice(0, 22) || e.className); return nome + ': ' + (hits.join(', ') || 'livre'); };
const out = [checa('abertura')];
const st = ScrollTrigger.getAll().find(s => s.pin && s.trigger.classList.contains('viagem'));
for (const f of [0.05, 0.3, 0.45, 0.66, 0.97]) {
  scrollTo(0, st.start + (st.end - st.start) * f); dispatchEvent(new Event('scroll')); ScrollTrigger.update(); await pump(1500);
  out.push(checa(document.querySelector('.trilha li.ativa').textContent));
}
innerWidth + 'x' + innerHeight + ' | ' + out.join(' | ');
// "livre" em todas as etapas = aprovado. Encostar na taça na etapa final é esperado (a garrafa serve o vinho).
