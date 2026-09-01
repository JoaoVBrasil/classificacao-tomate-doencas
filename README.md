# Classificação de Doenças em Folhas de Tomate a partir de Cor e Textura

**Projeto Aplicado Longitudinal — Processamento Digital de Imagens**
**Etapa M1 — Definição, Investigação de Viabilidade e Planejamento Técnico**

> 📍 **O projeto está atualmente na etapa M1.** O dataset foi baixado e foram realizados experimentos preliminares de histograma de cor em HSV e segmentação folha/fundo por HSV. Os resultados desses experimentos ainda estão em análise.

---

## Integrantes

| Nome completo | Usuário GitHub | Contato |
|---|---|---|
| **[João Vitor Schwambach Brasil]** | **[JoaoVBrasil]** | [joaovitorsbrasil11@gmail.com] |
| **[Luiz Gustavo Machado Muller]** | **[LuizGMMuller]** | [luizgustavomm19@gmail.com] |

---

## 1. Problema investigado

O projeto investiga a **classificação de doenças foliares em plantas de tomate (*Solanum lycopersicum*)** a partir de fotografias de folhas individuais, usando técnicas clássicas de PDI (segmentação, características de cor e textura), sem depender de aprendizado profundo.

Delimitamos o escopo a **uma única cultura (tomate)** e a **quatro classes**, em vez de um classificador genérico "doente vs. saudável" ou de todas as 10 classes de tomate disponíveis no dataset, para manter o problema tecnicamente tratável dentro do prazo da disciplina.

### Classes escolhidas

| Classe | Sintoma visual predominante |
|---|---|
| Saudável | Ausência de lesões; folha verde e uniforme |
| Requeima (*Late blight*) | Lesões grandes, irregulares, verde-acinzentadas a marrom-escuras, aspecto "encharcado" |
| Vira-cabeça-amarelo (*Tomato Yellow Leaf Curl Virus*) | Amarelecimento (clorose) e enrolamento das bordas — sem lesões pontuais, sintoma qualitativamente diferente das demais |
| Septoriose (*Septoria leaf spot*) | Muitas manchas pequenas e circulares, com centro claro/acinzentado e borda escura |

A escolha buscou classes com assinaturas visuais suficientemente diferentes entre si (ver justificativa completa em [`docs/proposta.md`](docs/proposta.md#1-problema)).

## 2. Contexto de aplicação

O diagnóstico de doenças foliares em tomate hoje depende majoritariamente de inspeção visual por agrônomos ou pelo próprio produtor. Um classificador automático operável a partir de fotos simples poderia servir como ferramenta de **triagem inicial** — sem substituir diagnóstico profissional. Não pretendemos construir um produto pronto para uso em campo; o contexto orienta decisões técnicas e limitações (detalhado em `docs/proposta.md`).

## 3. Objetivo geral

Desenvolver um pipeline de PDI capaz de classificar uma imagem de folha de tomate em uma das quatro classes definidas, a partir de características de cor e textura extraídas da região foliar segmentada. Objetivos específicos e critérios de sucesso verificáveis em [`docs/proposta.md`](docs/proposta.md#3-objetivo).

## 4. Visão resumida da solução proposta

Pipeline preliminar: **pré-processamento → segmentação folha/fundo → extração de características de cor e textura → classificação**. Alternativas consideradas em cada etapa (ex.: limiar em HSV vs. GrabCut para segmentação; k-NN vs. SVM para classificação) e justificativa técnica completa em [`docs/proposta.md`](docs/proposta.md#6-pipeline-preliminar).

## 5. Conjunto de imagens

Base: subconjunto de tomate do dataset **PlantVillage** (Hughes & Salathé, 2015), gratuito e amplamente usado na literatura de PDI/visão computacional para este problema. Origem, licença, contagens e instruções de acesso em [`images/README.md`](images/README.md) 

## 6. Estágio atual do projeto

📍 **Fase de investigação e viabilidade (M1).** O dataset já foi obtido e foram realizados dois experimentos preliminares:

- análise de histograma de cor em HSV;
- segmentação folha/fundo por limiarização em HSV.

Os códigos e resultados dos experimentos estão organizados em `docs/experiment_histograma/` e `docs/experiment_segmentacao/`.

A análise inicial dos resultados da segmentação e histograma ja foi realizada e se encontra dentro das suas pastas citadas anteriormente.

As pastas `src/`, `notebooks/` e `tests/` ainda não foram criadas, pois serão utilizadas nas etapas posteriores, quando houver implementação do pipeline definitivo.

## 7. Organização do repositório

.
├── README.md                       # documentação principal do projeto
├── AI_USAGE.md                     # declaração de uso de IA generativa
├── requirements.txt                # dependências Python do projeto
├── pyproject.toml                  # metadados e configuração do projeto
├── .gitignore                      # arquivos ignorados pelo Git
│
├── docs/
│   ├── proposta.md                 # proposta técnica do projeto
│   ├── experiment_histograma/      # experimentos relacionados a histogramas
│   └── experiment_segmentacao/     # experimentos relacionados à segmentação
│
└── images/
    ├── README.md                   # origem e informações sobre o dataset
    └── tomato_subset/              # subconjunto de imagens utilizado
    

## 8. Tecnologias previstas

Python 3, com **OpenCV** e/ou **scikit-image** para processamento de imagens, **NumPy/SciPy** para manipulação numérica, **scikit-learn** para classificadores clássicos (k-NN, SVM, Random Forest) e **Matplotlib/Pandas** para análise e visualização.

Durante a M1, OpenCV, NumPy e Matplotlib já foram utilizados nos experimentos preliminares de histograma e segmentação. As demais bibliotecas serão utilizadas conforme as próximas etapas do pipeline forem implementadas.

## 9. Reprodutibilidade

O ambiente Python utilizado nos experimentos é gerenciado por meio de um ambiente virtual (`.venv`), que não é versionado no Git.

As dependências utilizadas estão registradas em `requirements.txt`.

Os experimentos da M1 podem ser executados a partir da raiz do projeto utilizando os scripts presentes em:

- `docs/experiment_histograma/histograma_hsv.py`
- `docs/experiment_segmentacao/segmentacao_hsv.py`

As instruções específicas de execução e os resultados de cada experimento estão documentados em suas respectivas pastas.

## 10. Vídeo da M1

📹 **[TODO: link do vídeo, não listado, no YouTube]**

## 11. Documentação adicional

- [`docs/proposta.md`](docs/proposta.md) — proposta técnica completa (problema, objetivos, pipeline, arquitetura, viabilidade, referências, próximos passos)
- [`images/README.md`](images/README.md) — dataset: origem, licença, acesso
- [`AI_USAGE.md`](AI_USAGE.md) — uso de ferramentas de IA generativa neste projeto
# classificacao-tomate-doencas
