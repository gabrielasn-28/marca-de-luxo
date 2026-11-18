# SPEC: "A viagem do seu vinho" (Ganesh Vinhos)

GOAL:    the producer ends the film feeling that Ganesh carries his wine personally from his vineyard to a Brazilian glass, and wants that partner.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps.
TIME:    42 s x 30 = 1260 frames (v2). Music bed to be added (HeyGen catalog after sign-in): calm, elegant, ~84 BPM, strings and soft piano; payoff on the mark at 40.5 s.

LOOK:    the brand's own world, same as the site.
         ground: cellar #120F0C with a warm radial pool of light (#3A3020 at the centre, 0 at 60% radius); no other gradient.
         ink: ivory #F1EBE0. Accent: champagne gold #D6C190, used on the travelling routes, the active place name and the one gold mark. Brand gold #8F7749 for the symbol and the wine-free fills.
         display: Bodoni Moda 400, 104 px (9.6% of height), tracking -1%; italic for the second half of a phrase in gold. Body: Jost 300, 34 px (3.1%), tracking 0.
         medium: dark glass and gold leaf. The bottle is dark green-black glass (roughness 0.05, env intensity 2.6) with a gold capsule (metalness 1, roughness 0.28) and the Ganesh elephant in gold leaf. The map is an engraved nautical chart: hairline gold coastlines (0.9 px), countries of origin filled at 16% gold.
         light: key from upper right (warm #FFE2B0), cool-gold rim from behind left; contact shadow under the bottle 0.6 opacity, 40 px blur. No vignette beyond the light pool, no grain.

OBJECTS: the bottle (symbolic "your wine": no third-party label, elephant in gold); the nautical chart with real coastlines (Natural Earth); vineyard points at their real places (Champagne, Borgonha, Bordeaux, Douro, Rioja, Toscana, Piemonte, Dalmácia, Mendoza, Vale do Maule); the ports of Santos, Itajaí, São Francisco do Sul and Vitória; the real Ganesh stand at Covabra (photo, no customers' faces); a wine glass drawn as a single gold line that fills with wine #5E1A26; the Ganesh symbol (the brand's SVG).

MOTION:  arrivals expo.out / power4.out on long tails; camera moves power2.inOut; zoom-throughs power3.in.
         title entrance per word: blur 6 px -> 0 and opacity 0 -> 1 in 0.13 s, words 0.08 s apart, no translate. Titles dead still once landed. Exits 40% shorter (blur-out 0.18 s).
         routes draw with stroke-dashoffset, 1.6 s each, 0.07 s stagger.
         bottle: slow sway +-0.42 rad over 7 s while on screen (the one continuous motion), pour tilt 1.15 rad over 1.1 s.

SHOTS (v2, 42 s, faster and continuous; every seam is a hidden cut on an identical frame):
  1. 0.0-6.2   Abertura. Macro on the shoulder and gold capsule while the bottle spins (giro -2.6 -> 0, power3.out 3.3 s) and the key light sweeps (x -7 -> 4); dolly out to the whole bottle (1.3-3.0); title per word; gold-leaf sheen across "à mesa brasileira." (3.3-4.4); push into the elephant (4.75) and the symbol grows to a gold frame (5.45-6.07).  -> gold = gold.
  2. 6.2-24.2  A viagem. Gold falls onto the chart; vineyard points pop (back.out); montage of four punch-ins at 0.6 s each with the region name large in italic (Champagne, Bordeaux, Douro, Toscana); Europe overview + "Começa com quem faz o vinho."; pull back to the Atlantic, ten routes draw; the camera FOLLOWS the ship (a bright point with its own trail) from Champagne to Santos over 4 s; decelerates onto the coast, ports pop one by one, "Chega ao porto sem intermediários."; a ring opens once over Covabra; zoom through the point while a gold elephant grows from it to scale 7.  -> same giant elephant.
  3. 24.2-30.4 Na gôndola. The giant gold elephant's gold dissolves into the real Covabra photo while the silhouette shrinks to its frame on the right (power3.inOut 1.3 s); "Ganha a gôndola."; slow push on the photo; whip left (x -1150, blur 18 px, power3.in 0.85 s).  -> velocity-matched whip.
  4. 30.4-36.4 Na taça. Everything whips in from the right (power3.out); the bottle arrives spinning, tilts and pours; the wine surface in the glass waves as it fills; the wine overflows into a full-frame wave rising to cover the screen (4.4-5.7).  -> wine = wine.
  5. 36.4-42.0 Assinatura. The wine drains top to bottom revealing the cellar while gold rises inside the elephant; GANESH letters converge to their spacing (x offsets, expo.out); gold-leaf sheen across symbol and wordmark; "O seu vinho já tem uma casa no Brasil." held 3.3 s.
BANNED:  floating particles, lens flares, glass cards, three cards in a row, numbered 01/02 labels, text that drifts after landing, every element fading and sliding up, the logo docked in a corner, any invented label on the bottle, faces of customers.

QA:      frames 2.5 (bottle + full title), 6.8 (emblem filling), 8.0 (chart on Europe, points), 16.5 (routes mid-draw), 23.5 (ports legible >= 28 px), 29.5 (Covabra in the elephant), 37.0 (pour, glass half full), 43.5 (lockup + final line, centred, nothing clipped).
