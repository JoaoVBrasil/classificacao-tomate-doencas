# Classificação de Doenças em Folhas de Tomate a partir de Cor e Textura

**Projeto Aplicado Longitudinal — Processamento Digital de Imagens**
**Etapa M1 — Definição, Investigação de Viabilidade e Planejamento Técnico**

> ⚠️ **Este repositório está na etapa M1.** É um projeto em fase de definição e planejamento — ainda sem código, dataset baixado ou experimentos executados. Ver "6. Estágio atual" abaixo antes de avaliar o que existe aqui.

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

Base: subconjunto de tomate do dataset **PlantVillage** (Hughes & Salathé, 2015), gratuito e amplamente usado na literatura de PDI/visão computacional para este problema. Origem, licença, contagens e instruções de acesso em [`images/README.md`](images/README.md) — 

## 6. Estágio atual do projeto

📍 **Fase de definição e planejamento (M1).** Ainda não há código. O que existe hoje é: definição do problema, pipeline preliminar (hipótese técnica), levantamento sobre o dataset e um plano de investigação de viabilidade — ver checklist em [`docs/proposta.md`](docs/proposta.md#12-próximos-passos-antes-da-entrega).

As pastas `src/`, `notebooks/`, `tests/` e `results/` **ainda não existem** e serão criadas a partir do momento em que houver conteúdo real para colocar nelas (a partir da M2), seguindo a orientação do enunciado de não criar pastas vazias apenas para reproduzir uma estrutura de referência.

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

Python 3, com **OpenCV** e/ou **scikit-image** para processamento de imagens, **NumPy/SciPy** para manipulação numérica, **scikit-learn** para classificadores clássicos (k-NN, SVM, Random Forest) e **Matplotlib/Pandas** para análise e visualização. Justificativa por etapa em [`docs/proposta.md`](docs/proposta.md#6-pipeline-preliminar). Ver `requirements.txt` — nenhuma dependência foi instalada ou testada até o momento.

## 9. Reprodutibilidade

Ainda não há experimentos implementados para reproduzir nesta etapa. Instruções de setup de ambiente e execução serão adicionadas junto com o primeiro código, a partir da M2.

## 10. Vídeo da M1

📹 **[TODO: link do vídeo, não listado, no YouTube]**

## 11. Documentação adicional

- [`docs/proposta.md`](docs/proposta.md) — proposta técnica completa (problema, objetivos, pipeline, arquitetura, viabilidade, referências, próximos passos)
- [`images/README.md`](images/README.md) — dataset: origem, licença, acesso
- [`AI_USAGE.md`](AI_USAGE.md) — uso de ferramentas de IA generativa neste projeto
# classificacao-tomate-doencas
