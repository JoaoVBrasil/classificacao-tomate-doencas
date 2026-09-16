# 5. Parte B — Resposta ao feedback

| Nº | Síntese da observação recebida | Classificação do grupo | Evidência ou justificativa | Ação decorrente |
|----|---------------------------------|--------------------------|------------------------------|-------------------|
| 1 | O subconjunto do dataset foi removido do repositório, dificultando a reprodução dos experimentos. | Concordamos | O feedback apontou que os scripts dependiam do subconjunto do dataset, que não estava disponível no repositório avaliado. | Adicionamos o dataset utilizado ao repositório. |
| 2 | Os scripts apresentavam inconsistência nos caminhos dos arquivos e diretórios de saída. | Concordamos | A devolutiva identificou que o script de segmentação salvava os resultados em um local diferente dos resultados apresentados. | Corrigimos os caminhos de entrada e saída dos arquivos. |
| 3 | A segmentação deve ser avaliada em uma amostra maior e deve existir uma forma de medir sua qualidade. | Concordamos | A devolutiva recomenda ampliar a avaliação da segmentação e utilizar uma forma de medir sua qualidade. | Avaliar a segmentação em mais imagens na M2. |
| 4 | É necessário extrair características de textura e verificar sua capacidade de separar requeima e septoriose. | Concordamos | O feedback recomenda o uso de características de textura para analisar a separação entre essas classes. | Adicionar características de textura e realizar testes na M2. |
| 5 | A divisão dos dados deve evitar que imagens originais e suas variantes aumentadas fiquem simultaneamente nos conjuntos de treino e teste. | Concordamos | A devolutiva recomenda considerar a origem das imagens na divisão dos conjuntos. | Organizar a divisão dos dados entre treino e teste. |
| 6 | Os resultados obtidos com o PlantVillage não representam diretamente fotografias de campo. | Concordamos | A devolutiva destaca essa limitação do conjunto de dados utilizado. | Manter essa limitação registrada na análise do projeto. |

## 5.1 Síntese da posição do grupo

O grupo compreendeu e concorda com os principais pontos apresentados na avaliação da M1. As correções relacionadas ao dataset e aos caminhos dos arquivos já foram realizadas. Os demais pontos serão considerados no desenvolvimento da M2, principalmente a avaliação da segmentação, as características de textura e a organização dos dados para os testes. A principal questão técnica para a continuidade do projeto é tornar os experimentos mais reproduzíveis e avançar na análise das características das imagens.