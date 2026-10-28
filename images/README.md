# Imagens e dados — PlantVillage (subconjunto de tomate)

> A fonte e licença desta seção são as informadas anteriormente pela equipe. Antes
> da publicação da M2, reconfirmem se a versão baixada corresponde de fato ao
> registro citado e se a licença se aplica aos arquivos locais. A amostra M2
> contém fundos visivelmente variados e algumas imagens com folhas sobrepostas;
> não se deve presumir que toda imagem tenha fundo homogêneo e uma folha isolada.

## Origem

O dataset utilizado é o **PlantVillage**, publicado originalmente por Hughes & Salathé (2015) [1] e posteriormente usado por Mohanty, Hughes & Salathé (2016) [2] em um trabalho de classificação de doenças de plantas com redes neurais convolucionais. É um dos datasets mais citados na literatura de PDI/visão computacional aplicada à agricultura — o que é, em si, um indício indireto de viabilidade (ver `../docs/proposta.md`, Seção 8.1).

O dataset original não está mais disponível diretamente em plantvillage.org; hoje é obtido por meio de espelhos ("mirrors") republicados por terceiros, principalmente:

- Kaggle: <https://data.mendeley.com/datasets/tywbtsjrjv/1>

## Como obter e preparar a cópia local

1. Acesse a página de dados indicada acima e confira a versão, os termos e a licença
   aplicáveis ao arquivo que for baixar.
2. A equipe informa que a cópia usada no projeto veio da versão
   `without_augmentation`. Baixe essa versão somente se ela ainda corresponder à
   fonte/licença que a equipe verificou.
3. Extraia os arquivos localmente para `images/tomato_subset/`, preservando um
   diretório por classe (por exemplo,
   `images/tomato_subset/Tomato___healthy/`).
4. Execute o pipeline a partir da raiz do projeto:

   ```bash
   python -m tomato_pdi --dataset-dir images/tomato_subset --output-dir results/m2
   ```

Os arquivos do dataset estão excluídos do Git por `.gitignore` e não devem ser
adicionados ao repositório. A remoção dos arquivos previamente rastreados está
preparada no índice para o próximo commit; o diretório local foi mantido e não
será incluído em um clone novo. Commits públicos anteriores não foram reescritos
e ainda podem conter os dados no histórico. Cada integrante deve obter os dados
diretamente da fonte e respeitar os termos aplicáveis. A estrutura e os nomes das
classes podem variar conforme a versão: confira-os antes de executar.


## Quantidade e características

- Dataset completo: aproximadamente **54 mil imagens**, **38 classes**, cobrindo **14 espécies** de plantas (maçã, uva, milho, tomate, batata, entre outras) [1, 2].
- Subconjunto de tomate: **10 classes** (9 doenças + 1 classe saudável); a contagem de imagens varia entre aproximadamente 14 mil e 18 mil dependendo do espelho/versão específica consultada.
- O conjunto é descrito nas referências como imagens de condições controladas; porém, na cópia local inspecionada para M2 há fundos variados e algumas imagens com folhas sobrepostas. A adequação da versão local e a diferença para fotografias de campo são limitações documentadas em `../docs/relatorio_m2.md`.

### Classes escolhidas para este projeto (4 de 10 disponíveis para tomate)

1. `Tomato___healthy`
2. `Tomato___Late_blight`
3. `Tomato___Tomato_Yellow_Leaf_Curl_Virus`
4. `Tomato___Septoria_leaf_spot`

(Nomes de pasta/classe podem variar ligeiramente conforme o espelho escolhido — conferir ao baixar.)

### Contagem observada no checkout local

| Pasta | Imagens |
|---|---:|
| `Tomato___healthy` | 1.591 |
| `Tomato___Late_blight` | 1.909 |
| `Tomato___Septoria_leaf_spot` | 1.771 |
| `Tomato___Tomato_Yellow_Leaf_Curl_Virus` | 5.357 |
| **Total nas quatro classes** | **10.628** |

As contagens foram obtidas por extensão JPG/JPEG/PNG nas quatro pastas locais.
As imagens selecionadas para inspeção M2 têm 256×256 pixels. O experimento utiliza
12 imagens por classe (48 no total), em ordem numérica de nome de arquivo; não é
uma amostra aleatória nem uma partição de treino/teste. A declaração
`without_augmentation` precisa ser reconfirmada pela equipe e por auditoria de
duplicatas/origem antes de definir partições para a M3.

## Licença e condições de uso

- **Licença:** CC0 1.0. A licença foi verificada na página específica do Mendeley Data utilizada pelo grupo para realizar o download, em 31/08/2026.
- **O dataset foi baixado pelo grupo a partir da página do Mendeley Data utilizada como fonte:** https://data.mendeley.com/datasets/tywbtsjrjv/1. Foi utilizada a versão `without_augmentation` para a inspeção inicial das imagens. A licença informada na página é **CC0 1.0**.

O `.gitignore` exclui `images/tomato_subset/` para evitar adicionar arquivos de
dados em novos commits. Os arquivos anteriormente rastreados foram removidos do
índice Git para o próximo commit; a cópia local foi mantida. O histórico público
anterior não foi reescrito, então commits antigos ainda podem conter os dados.
Essa remoção não comprova nem substitui a verificação de licença para a versão
local.

## Referências

[1] HUGHES, D. P.; SALATHÉ, M. *An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing.* arXiv:1511.08060, 2015.

[2] MOHANTY, S. P.; HUGHES, D. P.; SALATHÉ, M. *Using Deep Learning for Image-Based Plant Disease Detection.* Frontiers in Plant Science, v. 7, art. 1419, 2016.
