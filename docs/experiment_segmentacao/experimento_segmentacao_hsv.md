# Experimento M1 — Segmentação folha/fundo por HSV

## Objetivo

Testar preliminarmente se a limiarização no espaço de cor HSV consegue separar a folha do fundo nas imagens selecionadas para o projeto.

## Lote

Foram avaliadas **20 imagens**, sendo um pequeno lote das imagens fornecidas para o experimento. A análise foi feita visualmente; os rótulos das classes não são necessários para avaliar a etapa de segmentação.

## Método

1. Conversão da imagem RGB/BGR para HSV.
2. Seleção de pixels com:
   - H entre 20 e 100;
   - S >= 35;
   - V >= 25.
3. Abertura e fechamento morfológicos com elemento elíptico 5×5.
4. Seleção do maior componente conectado, assumindo uma folha principal por imagem.
5. Aplicação da máscara sobre a imagem original.

## Resultado observado

O método conseguiu, de forma geral, **isolar a folha do fundo nas 20 imagens**, apesar de algumas limitações:

- sombras intensas podem ser removidas ou parcialmente excluídas da máscara;
- regiões muito escuras da folha podem apresentar falhas;
- folhas muito claras/amareladas exigem uma faixa de HSV suficientemente ampla;
- o método depende das condições relativamente controladas das imagens;
- não foi calculada uma métrica de acurácia de segmentação, pois não existe neste experimento uma máscara-verdade (ground truth) manual para comparação.

Portanto, o experimento fornece **evidência preliminar de viabilidade**, mas não demonstra que os parâmetros são definitivos ou que o método será o melhor entre HSV, Otsu e GrabCut.

## Área segmentada

A fração da imagem classificada como folha variou de **17.1% a 52.8%** entre as 20 imagens. Essa informação deve ser interpretada apenas como indicador auxiliar, não como uma métrica de qualidade, pois a área verdadeira da folha não foi anotada manualmente.

## Conclusão para a M1

A limiarização em HSV mostrou-se **promissora como primeiro método de segmentação folha/fundo** para o conjunto avaliado. O resultado justifica continuar a investigação na M2, comparando os resultados com pelo menos outro método e ajustando os parâmetros conforme a inspeção das imagens.

## Próximo passo

Comparar HSV com Otsu e/ou GrabCut em um lote semelhante e registrar visualmente as diferenças, especialmente em imagens com sombra, folhas amareladas e regiões escuras.
