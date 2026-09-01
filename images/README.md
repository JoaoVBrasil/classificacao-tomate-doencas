# Imagens e dados — PlantVillage (subconjunto de tomate)

## Origem

O dataset utilizado é o **PlantVillage**, publicado originalmente por Hughes & Salathé (2015) [1] e posteriormente usado por Mohanty, Hughes & Salathé (2016) [2] em um trabalho de classificação de doenças de plantas com redes neurais convolucionais. É um dos datasets mais citados na literatura de PDI/visão computacional aplicada à agricultura — o que é, em si, um indício indireto de viabilidade (ver `../docs/proposta.md`, Seção 8.1).

O dataset original não está mais disponível diretamente em plantvillage.org; hoje é obtido por meio de espelhos ("mirrors") republicados por terceiros, principalmente:

- Kaggle: <https://data.mendeley.com/datasets/tywbtsjrjv/1>


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

- **Licença:** CC0 1.0. A licença foi verificada na página específica do Mendeley Data utilizada pelo grupo para realizar o download, em 31/08/2026.
- **O dataset foi baixado pelo grupo a partir da página do Mendeley Data utilizada como fonte:** https://data.mendeley.com/datasets/tywbtsjrjv/1. Foi utilizada a versão `without_augmentation` para a inspeção inicial das imagens. A licença informada na página é **CC0 1.0**.

## Referências

[1] HUGHES, D. P.; SALATHÉ, M. *An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing.* arXiv:1511.08060, 2015.

[2] MOHANTY, S. P.; HUGHES, D. P.; SALATHÉ, M. *Using Deep Learning for Image-Based Plant Disease Detection.* Frontiers in Plant Science, v. 7, art. 1419, 2016.
