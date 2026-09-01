# Imagens e dados — PlantVillage (subconjunto de tomate)

## Origem

O dataset utilizado é o **PlantVillage**, publicado originalmente por Hughes & Salathé (2015) [1] e posteriormente usado por Mohanty, Hughes & Salathé (2016) [2] em um trabalho de classificação de doenças de plantas com redes neurais convolucionais. É um dos datasets mais citados na literatura de PDI/visão computacional aplicada à agricultura — o que é, em si, um indício indireto de viabilidade (ver `../docs/proposta.md`, Seção 8.1).

O dataset original não está mais disponível diretamente em plantvillage.org; hoje é obtido por meio de espelhos ("mirrors") republicados por terceiros, principalmente:

- Kaggle: <https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset>
- GitHub (republicação usada em diversos trabalhos): <https://github.com/spMohanty/PlantVillage-Dataset>

**Atenção:** como o dataset é redistribuído em várias plataformas, com pequenas variações entre versões, o grupo deve conferir a licença e a contagem exata de imagens diretamente na página escolhida para download, em vez de assumir automaticamente os números abaixo.

## Quantidade e características

- Dataset completo: aproximadamente **54 mil imagens**, **38 classes**, cobrindo **14 espécies** de plantas (maçã, uva, milho, tomate, batata, entre outras) [1, 2].
- Subconjunto de tomate: **10 classes** (9 doenças + 1 classe saudável); a contagem de imagens varia entre aproximadamente 14 mil e 18 mil dependendo do espelho/versão específica consultada.
- Imagens capturadas em condições controladas (fundo homogêneo, folha isolada e centralizada) — uma simplificação em relação a fotos de campo, discutida como limitação em `../docs/proposta.md`, Seção 9.

### Classes escolhidas para este projeto (4 de 10 disponíveis para tomate)

1. `Tomato___healthy`
2. `Tomato___Late_blight`
3. `Tomato___Tomato_Yellow_Leaf_Curl_Virus`
4. `Tomato___Septoria_leaf_spot`

(Nomes de pasta/classe podem variar ligeiramente conforme o espelho escolhido — conferir ao baixar.)

## Licença e condições de uso

A versão original do PlantVillage é licenciada como **CC0 1.0** (domínio público). Alguns espelhos/republicações podem apresentar termos ligeiramente diferentes. **O grupo deve verificar e registrar aqui a licença exata da página específica utilizada para download antes da entrega final**, citando a fonte e a data de verificação.

## Como obter

O dataset **não está incluído neste repositório** (tamanho incompatível com um repositório Git). Para obtê-lo:

1. Baixar o subconjunto de tomate a partir de um dos links acima.
2. Salvar localmente em `images/raw/` (pasta já listada no `.gitignore` — não commitar o dataset completo).
3. Selecionar manualmente 5–10 imagens representativas de cada uma das 4 classes escolhidas e copiá-las para `images/exemplos/` (criar esta pasta ao fazê-lo), para que o repositório tenha uma amostra visual mesmo sem o dataset completo.

**Status atual: nenhuma imagem foi baixada ainda.** Esta seção descreve como obter o dataset, não confirma que isso já foi feito — ver checklist de próximos passos em `../docs/proposta.md`, Seção 12.

## Referências

[1] HUGHES, D. P.; SALATHÉ, M. *An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing.* arXiv:1511.08060, 2015.

[2] MOHANTY, S. P.; HUGHES, D. P.; SALATHÉ, M. *Using Deep Learning for Image-Based Plant Disease Detection.* Frontiers in Plant Science, v. 7, art. 1419, 2016.
