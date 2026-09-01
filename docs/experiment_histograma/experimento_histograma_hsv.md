# Experimento — Histograma de cor em HSV

## Objetivo

Verificar se existem diferenças nas cores das folhas entre as quatro classes escolhidas para o projeto.

O histograma foi utilizado como uma primeira análise das imagens antes da implementação da classificação.

## Classes analisadas

Foram utilizadas as quatro classes escolhidas para o projeto:

- `Tomato___healthy`
- `Tomato___Late_blight`
- `Tomato___Septoria_leaf_spot`
- `Tomato___Tomato_Yellow_Leaf_Curl_Virus`

## Método

As imagens foram convertidas do espaço de cor RGB para HSV.

O histograma foi utilizado para observar a distribuição dos valores de cor presentes nas imagens. A análise foi feita sobre uma amostra das imagens das quatro classes.

O objetivo não foi classificar as imagens neste momento, mas verificar visualmente se existem diferenças de cor que possam ser utilizadas posteriormente como características para o classificador.

## Código

O código utilizado está em:

`docs/experiment_histograma/histograma_hsv.py`

Para executar o experimento a partir da raiz do projeto:

```bash
python3 docs/experiment_histograma/histograma_hsv.py 
```

## Resultado

O resultado gerado pelo experimento está em:

`docs/experiment_histograma/results/Figure_1.png`

## Análise

O histograma será analisado para verificar se as distribuições de cor apresentam diferenças entre as quatro classes.

A observação será focada principalmente em identificar se alguma classe apresenta uma distribuição de cores diferente das demais e se essas diferenças podem ser úteis para a classificação.

## Conclusão

O experimento representa uma primeira verificação sobre a utilização de características de cor no pipeline.

A conclusão final será definida a partir da análise do histograma e da comparação entre as classes.


#### Histograma de cor HSV

Foi realizado um primeiro teste utilizando a distribuição do canal H (matiz) do espaço HSV nas quatro classes. O histograma apresentou diferenças na distribuição de matiz entre as classes. A classe `Tomato___Tomato_Yellow_Leaf_Curl_Virus` apresentou uma concentração diferente das demais, principalmente em uma faixa de matizes associada a tons mais amarelados. Por outro lado, `Tomato___healthy` e `Tomato___Septoria_leaf_spot` apresentaram maior sobreposição.

Esse resultado indica que o canal H pode ser útil como uma característica de cor, mas provavelmente não será suficiente sozinho para separar todas as quatro classes. Por isso, a investigação continuará considerando outras características de cor e, posteriormente, características de textura.