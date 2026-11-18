# Fase 1: entender e pesquisar a empresa

Uma identidade de luxo nasce de fatos. Os sites premiados parecem inevitáveis porque cada escolha vem de algo real: o lugar de origem, o processo, uma pessoa, um número. Sem pesquisa, sobram clichês ("tradição", "excelência", "paixão") e o resultado tem cara de template.

Faça a pesquisa **antes** de perguntar: as perguntas ficam poucas e certeiras, e a pessoa percebe que você entendeu o negócio dela.

## 1. Ler o que a pessoa mandou

| Material | Como ler | O que tirar |
|---|---|---|
| Site atual | Navegador interno (`get_page_text`) ou WebFetch | Nome jurídico, endereço, telefones, e-mail, história, textos, cores e fontes em uso |
| Catálogo em PDF | `pypdf` para texto; extraia as imagens (as páginas costumam ser imagens inteiras) | Produtos, origens, prêmios e notas, preços (não publicar sem pedir), fotos de produto |
| Logo | Imagem ou arquivo vetorial | Cores exatas (medidas em pixels), formas que podem virar moldura |
| Fotos | Abra cada uma | O que é usável; quem aparece (pessoas exigem autorização) |
| Conversas, áudios transcritos, e-mails | Leia tudo | Como a empresa fala de si, o que o dono valoriza, pedidos e restrições |
| Apresentação antiga | Leia | Números que a empresa já usa, argumentos de venda |

Guarde o material em `fontes/` e não altere os originais.

## 2. Pesquisar fora

Faça buscas em paralelo; use `deep-research` quando o setor for desconhecido ou a empresa tiver pouca presença on-line.

1. **A empresa**: CNPJ e razão social, tempo de mercado, notícias, Instagram e LinkedIn, avaliações, prêmios. Separe outros negócios do mesmo grupo (na Ganesh, o comércio exterior em ganlog.com.br era outro negócio).
2. **Os produtos e parceiros**: a origem de cada produto, os produtores ou fornecedores, as notas e prêmios que eles próprios divulgam.
3. **O setor e os concorrentes diretos**: 3 a 5 sites. Anote o que todos repetem, porque é exatamente isso que deve ser evitado.
4. **As referências premiadas do setor**: Awwwards, FWA, CSSDA, Behance. Comece pela tabela de `padrao-de-qualidade.md` e acrescente o que achar do setor.
5. **Os canais reais**: onde o produto é vendido, pontos físicos, ações de degustação, feiras.

Regras:
- Cada fato no dossiê tem fonte (link, página do catálogo ou "dito pela cliente em <data>").
- Fato sem fonte confiável vai para "A confirmar". Nunca vira número grande no site.
- Não copie textos nem imagens protegidas de outros sites. Fotos de produto saem do material da própria empresa.
- Não envie dados pessoais da pessoa ou do cliente para serviços externos.

## 3. Escrever o `dossie.md`

Use este modelo (também em `assets/modelos/dossie.md`; exemplo real em `assets/exemplo-ganesh/dossie.md`):

```markdown
# Dossiê: <Empresa>  (<data>)

## Em uma frase
<o que a empresa faz, para quem, e o que ela faz que ninguém mais faz>

## Fatos (com fonte)
| Fato | Fonte |
|---|---|

## Produtos e origem
<linhas, países/regiões, destaques com notas e prêmios citados pelo próprio fornecedor>

## Público e decisão de compra
<quem precisa ser convencido; o que essa pessoa teme e o que ela quer ver>

## Ativos disponíveis
- Logo: <formato, qualidade>
- Fotos: <usáveis / com pessoas (autorização?)>
- Catálogo: <data, nº de itens>
- Contatos oficiais: <telefone, WhatsApp, e-mail, endereço>

## Histórias verdadeiras (matéria-prima do conceito)
1. <processo, lugar, pessoa, número, caso real>

## O que os concorrentes repetem (evitar)

## Referências premiadas do setor

## A confirmar com a cliente
- <números, autorizações, e-mail oficial>
```

## 4. Do dossiê para o conceito

As **histórias verdadeiras** são a matéria-prima do momento principal. Procure a que tem movimento, ou seja, um começo e um fim no espaço ou no tempo: origem → destino, matéria-prima → produto, ontem → hoje. Na Ganesh, o dossiê mostrou que a empresa nasceu no comércio exterior e faz ela mesma o desembaraço nos portos; isso virou "A viagem do seu vinho", que nenhuma outra importadora pode contar do mesmo jeito.
