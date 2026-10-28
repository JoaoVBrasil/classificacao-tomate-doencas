# Classificação de doenças em folhas de tomate

**Projeto Aplicado Longitudinal — Processamento Digital de Imagens — M2**
**Grupo 14**

## Equipe

| Integrante | GitHub |
|---|---|
| João Vitor Schwambach Brasil | [@JoaoVBrasil](https://github.com/JoaoVBrasil) |
| Luiz Gustavo Machado Muller | [@LuizGMMuller](https://github.com/LuizGMMuller) |

## Problema e objetivo

O projeto investiga a análise de imagens de folhas de tomate para distinguir quatro
classes: saudável, requeima, septoriose e Tomato Yellow Leaf Curl Virus. O objetivo
final é combinar cor e textura em um classificador clássico. Nesta M2, o fluxo
executável cobre leitura, segmentação HSV, morfologia, análise de componentes,
extração de atributos e avaliação preliminar da máscara. A classificação e uma
referência manual de segmentação permanecem para a M3.

O resultado não substitui diagnóstico agronômico. As condições de captura e a
representatividade das imagens limitam qualquer generalização para lavouras.

## Estado da implementação

| Etapa | Estado |
|---|---|
| Leitura das imagens e seleção determinística por classe | Implementado |
| Máscara inicial por limiar HSV e maior componente conectado | Implementado |
| Abertura 3×3 e fechamento 5×5 | Implementado e comparado com a máscara sem morfologia |
| Área, perímetro, circularidade, médias HSV/Lab e GLCM | Implementado; CSV reproduzível |
| Métricas Dice/IoU | Calculadas contra proxy automático, não contra anotação manual |
| Classificador e avaliação em treino/validação/teste | Planejado para M3 |
| Máscaras anotadas manualmente e validação independente | Planejado para M3 |

## Dados

Na cópia local usada para gerar os resultados, havia imagens organizadas em dez
diretórios de classes de tomate. As quatro classes do escopo somavam 10.628
imagens: 1.591 saudáveis, 1.909 requeima, 1.771 septoriose e 5.357 Yellow Leaf
Curl Virus. O experimento M2 usa as primeiras 12 imagens em ordenação numérica de
cada classe (48 imagens), sem treinamento de modelo. Os arquivos não são incluídos
no índice Git atual; cada integrante deve obtê-los conforme
[`images/README.md`](images/README.md).

A origem e licença informadas pelo grupo estão em [`images/README.md`](images/README.md).
O relatório registra também o que foi possível observar na amostra local e as
limitações de representatividade. **Não adicione nem publique novos arquivos do
dataset**; siga as instruções de obtenção e licenciamento descritas naquele
documento. A remoção dos arquivos do índice Git está preparada para o próximo
commit; commits públicos anteriores não foram reescritos e podem continuar contendo
os dados no histórico.

## Instalação e execução

Requer Python 3.10 ou superior. A partir da raiz:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install ".[dev]"
python -m tomato_pdi --samples-per-class 12
```

O dataset deve estar em `images/tomato_subset/<nome-da-classe>/`. Reinstale o
pacote com `python -m pip install ".[dev]"` depois de alterar o código. Para
escolher outro diretório ou gerar uma amostra maior:

```bash
python -m tomato_pdi \
  --dataset-dir images/tomato_subset \
  --output-dir results/m2 \
  --samples-per-class 12
```

Saídas produzidas em `results/m2/`:

- `segmentacao_metricas.csv`: Dice e IoU por imagem, com/sem morfologia;
- `descritores.csv`: região e atributos de cor/textura por imagem;
- `resumo.json`: médias e protocolo da execução;
- `comparacao_morfologia.png`: comparação das métricas;
- `mascaras_exemplo.png`: maior e menor concordância observadas.

O menor Dice/IoU reflete concordância com uma referência automática provisória,
estimada pela diferença de cor em relação aos quatro cantos da imagem. Ela **não é
uma anotação de verdade-terreno**; os números são evidência preliminar e precisam
ser confirmados com máscaras revisadas manualmente.

Para executar os testes unitários:

```bash
python -m pytest
```

## Experimento M2 reproduzido

Pergunta: a abertura e o fechamento morfológicos alteram a concordância da máscara
HSV com o proxy de fundo? A única variável entre as duas configurações é a
morfologia. As 48 imagens (12 por classe) e o cálculo da referência são iguais.

Na execução registrada em [`results/m2/resumo.json`](results/m2/resumo.json), a
média de Dice passou de **0,8723** sem morfologia para **0,8786** com abertura
3×3 + fechamento 5×5; o IoU médio passou de **0,7930** para **0,8030**. A melhora
é pequena e não demonstra qualidade real de segmentação porque a referência é
automática. A figura compara as configurações; `mascaras_exemplo.png` mostra um
caso de maior concordância e um de menor concordância, incluindo a falha do proxy
em imagens com fundo heterogêneo ou múltiplas folhas.

![Comparação de métricas da morfologia](results/m2/comparacao_morfologia.png)

![Exemplos de máscaras e limitações](results/m2/mascaras_exemplo.png)

## Organização

```text
src/tomato_pdi/          Pipeline e experimento reproduzível
tests/                   Testes unitários
docs/                    Proposta, relatório M2 e experimentos anteriores
images/                  Instruções e dados locais do projeto
results/m2/              CSVs, resumo e figuras gerados
AI_USAGE.md              Declaração de uso de IA generativa
```

## Evolução, relatório e referências

- [`docs/proposta.md`](docs/proposta.md): proposta e estado atualizados.
- [`docs/revisao_m1_plano_m2.md`](docs/revisao_m1_plano_m2.md): feedback da M1 e
  revisão/plano da equipe; responsáveis e contribuições foram preenchidos conforme
  divisão informada pelo grupo. A nota registrada no diário ainda requer consulta.
- [`docs/relatorio_m2.md`](docs/relatorio_m2.md): protocolo, resultados, análise,
  limitações e plano M3.
- [`images/README.md`](images/README.md): origem declarada e condições dos dados.
- [`AI_USAGE.md`](AI_USAGE.md): registro das ferramentas e materiais apoiados por IA.

As referências bibliográficas e condições de uso do conjunto estão em
[`docs/proposta.md`](docs/proposta.md#11-referências) e
[`images/README.md`](images/README.md).

## Vídeo M2

**O vídeo não foi possível de realizar dentro do prazo e será gravado posteriormente.**
Depois da gravação, incluir aqui o link não listado. O vídeo deverá contar com
participação identificável dos dois integrantes e apresentar a evolução, os dados,
a execução, as máscaras, a comparação, as limitações e o plano M3.

## Identificação da versão de entrega

- Commit/tag M2: **preencher após revisão final e criação da versão de entrega**.
- Data da entrega: **confirmar com a disciplina**.
