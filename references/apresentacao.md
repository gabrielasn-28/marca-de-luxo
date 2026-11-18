# Módulo: apresentação no mesmo estilo do site

Exemplo testado: `assets/exemplo-ganesh/apresentacao/` (12 slides, Ganesh Vinhos para produtores).

## Formato
Use o tipo de artefato **Slides**: `Artifact` com `action: "quickstart"`, `intent: "slides"`, depois publique com o `type_url`. Ele permite apresentar em tela cheia e exportar em PowerPoint e PDF, que é o que o cliente envia por e-mail. Siga as instruções do tipo, que chegam na criação:
- `project/deck.json`, `project/deck.css` e um arquivo por slide;
- 1920×1080 com margem de 128px;
- texto com no mínimo 24px;
- até 200 elementos por slide.

Envie as imagens primeiro como assets (`file_paths` com `asset: true`) e use as URLs `/_blob/...`.

## Roteiro que funcionou (para fornecedores e produtores)
1. Capa: o nome da marca, a promessa ("O seu vinho em boas mãos no Brasil") e os produtos num palco de luz.
2. Origem: uma frase de impacto num slide da cor da marca (o dourado).
3. A empresa em números: 4 números grandes que sejam reais (confirme com o cliente).
4. O conceito do site: a viagem, com o mapa e as rotas em SVG animadas por `stroke-dashoffset`.
5. A prova técnica: tabela de portos e capacidade.
6. Portfólio: um produto por país, numa fila.
7. Prestígio: tela dividida em texto claro e painel dourado com os produtos, citando o catálogo.
8. Processo: 6 passos numerados, porque é uma sequência real.
9. Caso real: foto em arco (border-radius grande no topo) e fatos com fonte citada.
10. O que o parceiro recebe: 4 colunas no slide dourado.
11. Proposta: 3 ideias, em forma de convite e não de pedido.
12. Contato e assinatura, com o símbolo grande e apagado ao fundo.

## Ritmo visual
Alterne noite (adega), dia (papel) e dourado. A ousadia fica no slide da viagem.

## O que o formato Slides não aceita (aprendido)
- `mask` e `clip-path`: a silhueta da logo não pode ser moldura. Use arco com `border-radius` ou um SVG.
- `<text>` dentro de SVG: os rótulos precisam ser `<p>` posicionados sobre o desenho.
- `border-radius` acima de 256px.
- `z-index`: a ordem do código manda.
- Animação: `@keyframes` com o estado final no estilo normal e o início em `from`; para entrar em sequência, use `animation-delay: calc(var(--i) * 130ms)`.

## Conferir
O link do artefato pede login no navegador interno. Para conferir:
1. Gere uma prévia local juntando `deck.css` com as `<section>` e trocando `/_blob/<id>` pelas imagens locais.
2. Abra a prévia num viewport de 1920×1080.
3. Meça por JavaScript se algum elemento passa de x 1792 ou y 952. A fila do portfólio estourou 28px, e esse foi o único ajuste necessário.
4. Apague a prévia ao terminar.

## Pendências típicas para o cliente confirmar
- Números do slide 3.
- E-mail oficial.
- Autorização de uso de fotos com pessoas.
- Versões em outros idiomas (ES e IT para produtores estrangeiros).

## Traduções (feito: ES e IT)
- Cada idioma é **uma apresentação separada**, com o mesmo `deck.css` copiado. As imagens precisam ser enviadas de novo para cada apresentação, porque os ids `/_blob/` mudam e é preciso trocar todos.
- Use tratamento formal: em espanhol "usted/su", em italiano "voi/vostro". Termos de vinho: "lineal" (ES) e "scaffale" (IT) para gôndola; "despacho aduanero" (ES) e "sdoganamento" (IT) para desembaraço; "bodega" (ES) e "cantina" (IT) para vinícola; "cosecha" (ES) e "vendemmia" (IT) para safra.
- **Tire as notas do apresentador** das versões enviadas ao produtor, porque quem abre a apresentação consegue lê-las. As notas internas ficam só na versão do cliente.
- Endereço: em espanhol "7.º piso, …, São Paulo, Brasil"; em italiano "7º piano, …, San Paolo, Brasile".
- Conferência automática: procure palavras em português no texto sem as tags ("você", "seu", "vinho", "garrafa", "-ção", "não", "rótulo"), ids de imagem da versão original e `<aside>`.
