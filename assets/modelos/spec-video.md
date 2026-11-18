# SPEC: "<título>" (<Empresa>)

GOAL:    <o que o espectador sente e quer fazer ao fim>
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps.
TIME:    <N> s x 30 = <quadros>. Música: <estilo, BPM, ponto de clímax em X s> ou "sem trilha (avisar)".

LOOK:    fundo: <token noite com hex>, palco de luz <hex no centro, raio>.
         texto: <hex>. Destaque: <hex> (só no que está ativo). Marca: <hex>.
         display: <fonte> <peso>, <px> (<% da altura>), tracking <x>. Corpo: <fonte> <peso>, <px>.
         material: <do objeto herói: cor, rugosidade, metal>.
         luz: principal <direção, cor>; contraluz <direção, cor>; sombra de contato <opacidade, desfoque>.

OBJECTS: <objeto herói>; <cenário>; <foto real>; <símbolo da marca>.

MOTION:  chegadas <curva>; câmera <curva>; mergulhos <curva>.
         título: por palavra, desfoque 6px→0, 0,13 s, 0,08 s entre palavras, sem subir. Parado depois de pousar.
         <o único movimento contínuo>

SHOTS:   (cada costura é um quadro idêntico dos dois lados)
  1. 0.0-<t>   Abertura. <plano>  -> <costura>
  2. <t>-<t>   Momento principal. <plano>  -> <costura>
  3. <t>-<t>   Prova real. <plano>  -> <costura>
  4. <t>-<t>   Produto em uso. <plano>  -> <costura>
  5. <t>-<N>   Assinatura. <símbolo + frase final parados ≥ 3 s>

BANNED:  partículas, brilho de lente, cartões de vidro, três cards em fila, rótulos 01/02, texto que flutua depois de pousar, tudo surgindo e subindo, logo num canto, rótulo inventado no produto, rosto sem autorização.

QA:      quadros <t1> (abertura completa), <t2> (cenário), <t3> (meio do momento principal), <t4> (texto pequeno legível ≥ 28 px), <t5> (prova real), <t6> (assinatura centrada, nada cortado).
