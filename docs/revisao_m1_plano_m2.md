# Revisão da M1 e plano de ação para a M2

## 4. Parte A — Identificação da equipe e dos materiais conferidos

| Item | Informação |
|---|---|
| Identificação do grupo | Grupo 14 |
| Integrantes | João Vitor Schwambach Brasil e Luiz Gustavo Machado Muller |
| Repositório avaliado | https://github.com/JoaoVBrasil/classificacao-tomate-doencas |
| Commit, versão ou estado da entrega M1 | `15548c0381172fd567c91be3e2ff6f74a307b588` |
| Documento de feedback consultado | Devolutiva da M1 — Grupo 14 |
| Data desta revisão do documento | 27/10/2026 |
| Nota informada na devolutiva | Conferência adiada |
| Nota registrada no diário | Pendente de consulta pelos integrantes |

O grupo conferiu o commit `15548c0381172fd567c91be3e2ff6f74a307b588`, que corresponde ao estado do repositório considerado na avaliação.

## 5. Parte B — Resposta ao feedback

Leiam toda a devolutiva antes de responder aos itens separadamente. Depois, classifiquem cada observação recebida.

| Nº | Síntese da observação recebida | Classificação do grupo | Evidência ou justificativa | Ação decorrente |
|---:|---|---|---|---|
| 1 | O subconjunto do dataset foi removido do repositório, dificultando a reprodução dos experimentos. | Concordamos | Um clone limpo precisa obter os dados separadamente; instruções de fonte e preparação local constam em [`images/README.md`](../images/README.md). A M2 também orienta não versionar dataset de terceiros. | Os arquivos foram removidos do índice Git para o próximo commit, permanecem ignorados pelo `.gitignore` e continuam disponíveis apenas no checkout local. Commits públicos antigos não foram reescritos. |
| 2 | Os scripts apresentavam inconsistência nos caminhos dos arquivos e diretórios de saída. | Concordamos | O pipeline M2 aceita diretórios por argumentos e grava resultados em `results/m2/`; comando registrado no README. | Unificar entrada e saída no comando reproduzível da M2. |
| 3 | A segmentação deve ser avaliada em uma amostra maior e deve existir uma forma de medir sua qualidade. | Concordamos | Foram processadas 48 imagens (12 por classe), com comparação de Dice/IoU contra um proxy automático de fundo. | A avaliação foi ampliada e documentada como preliminar; a referência automática não substitui máscaras anotadas. |
| 4 | É necessário extrair características de textura e verificar sua capacidade de separar requeima e septoriose. | Concordamos parcialmente | Foram extraídos contraste, homogeneidade e energia GLCM em `results/m2/descritores.csv`; não houve treinamento de classificador nem teste da separação entre as classes. | A extração foi implementada na M2; a avaliação de poder discriminativo e classificação fica para a M3. |
| 5 | A divisão dos dados deve evitar que imagens originais e suas variantes aumentadas fiquem simultaneamente nos conjuntos de treino e teste. | Concordamos | A M2 não realiza treinamento nem cria divisão treino/teste. A origem/duplicidade das imagens locais ainda deve ser auditada. | Planejar auditoria por imagem de origem e divisão sem vazamento antes do classificador M3. |
| 6 | Os resultados obtidos com o PlantVillage não representam diretamente fotografias de campo. | Concordamos | A limitação foi mantida na proposta e no relatório; a amostra inspecionada também apresenta variação de fundo e folhas sobrepostas. | Não generalizar resultados a campo; registrar essa restrição nas conclusões. |

### 5.1 Síntese da posição do grupo

O grupo manteve o escopo de quatro classes e avançou para uma implementação parcial. O código processa 48 imagens, compara duas configurações de morfologia e exporta descritores de cor, geometria e GLCM. As métricas usam proxy automático e, portanto, são preliminares. O conjunto foi retirado do índice Git (remoção staged), sem reescrever o histórico anterior; cada integrante deverá obter os dados da fonte indicada e confirmar a licença. Os nomes, a data desta revisão e a divisão de contribuições informada pela equipe estão registrados neste documento. A nota no diário e os cálculos oficiais continuam pendentes de consulta pela equipe.

## 6. Parte C — Conferência das pontuações

| Critério | Peso ou valor máximo | Nível atribuído | Pontuação registrada | Pontuação recalculada pelo grupo | Diferença |
|---|---:|---|---:|---:|---:|
| 1. Problema | 15,00 | Excelente | 15,00 | Adiada | Adiada |
| 2. Imagens e dados | 10,00 | Excelente | 10,00 | Adiada | Adiada |
| 3. Objetivos e sucesso | 10,00 | Excelente | 10,00 | Adiada | Adiada |
| 4. Pipeline | 15,00 | Excelente | 15,00 | Adiada | Adiada |
| 5. Viabilidade | 15,00 | Excelente | 15,00 | Adiada | Adiada |
| 6. Repositório | 10,00 | Adequado | 7,50 | Adiada | Adiada |
| 7. Markdown | 10,00 | Excelente | 10,00 | Adiada | Adiada |
| 8. Vídeo | 10,00 | Pendente | 10,00 | Adiada | Adiada |
| 9. Histórico | 5,00 | Adequado | 5,00 | Adiada | Adiada |
| **Total** | **100,00** | | **Conferência adiada** | **Conferência adiada** | **Conferência adiada** |

> A transcrição e a conferência aritmética das pontuações foram adiadas a pedido da equipe. Retomar este item após consultar a ficha original e o diário.

### 6.1 Resultado da conferência aritmética

**Conferência adiada para depois, conforme decisão da equipe.** A soma da ficha e
qualquer possível divergência não foram analisadas nesta revisão.

## 7. Parte D — Conferência da nota registrada no diário

| Verificação | Valor |
|---|---:|
| Nota recalculada a partir da ficha | Conferência adiada |
| Nota apresentada na devolutiva | Conferência adiada |
| Nota registrada no diário | Conferência adiada |
| Diferença identificada | Será verificada posteriormente pela equipe. |

**Conferência da nota adiada a pedido da equipe.** Consultar a ficha original e o
diário em outro momento; nenhum cálculo ou conclusão sobre divergência foi
registrado nesta revisão.

## 8. Parte E — Diagnóstico da situação atual

| Componente | Situação atual | Evidência existente | Lacuna identificada |
|---|---|---|---|
| Definição e delimitação do problema | Adequado | Cultura, quatro classes e cenário de aplicação registrados na proposta. | Confirmar que os integrantes mantêm o escopo; a inspeção M2 encontrou variação de fundo e folhas sobrepostas. |
| Objetivo e saída esperada | Adequado | Entrada, saída e critérios previstos registrados na proposta revisada. | Classificador final planejado para M3. |
| Conjunto inicial de imagens | Adequado | PlantVillage caracterizado, licença verificada e subconjunto escolhido (critério 2, Excelente). | Resultados no PlantVillage não representam diretamente fotografias de campo. |
| Pipeline proposto | Adequado | Etapas e alternativas justificadas; na M2 há código para segmentação, morfologia e descritores de cor/textura. | Ainda não há classificador nem avaliação do poder discriminativo dos descritores. |
| Evidência de viabilidade | Parcial | Experimento em 48 imagens, com Dice/IoU contra proxy, CSVs e figuras. | Proxy automático não é referência anotada; validação continua preliminar. |
| Fundamentação e referências | Adequado | Proposta e referências listadas; uso de IA atualizado em `AI_USAGE.md`. | Equipe deve verificar fontes e licença do conjunto realmente utilizado. |
| Organização do repositório | Atualizada para M2 | README, dependências e instruções de obtenção; o dataset está fora do índice Git e ignorado. | Remoção staged ainda precisa entrar no commit de entrega; commits públicos anteriores não foram reescritos. |
| Relatório técnico | Parcial da M2 | [`docs/relatorio_m2.md`](relatorio_m2.md) documenta amostra, protocolo, comparação, limitações e plano M3. | Classificador e validação por máscaras manuais não foram implementados nesta etapa. |
| Página parcial do projeto | Atualizada | README apresenta objetivo, execução, saídas, estado, links e pendência do vídeo. | Inserir link do vídeo e identificador do commit/tag de entrega. |
| Registro de decisões e limitações | Adequado | Limitação do PlantVillage frente a fotografias de campo e proxy automático estão explicitados. | Confirmar fonte/licença do arquivo local e concluir auditoria de duplicatas para M3. |

### 8.1 Interpretação do escopo de implementação da M2

O enunciado permite explicitamente que a inferência final ou um classificador
completo permaneçam para a M3, se houver fluxo parcial executável e plano
concreto. Também não determina que toda avaliação de segmentação use máscaras
manuais: admite referência manual, rótulos, contagens ou outro procedimento
adequado. Nesta entrega, Dice/IoU são calculados contra um proxy automático e a
avaliação é declarada preliminar; essa limitação e a validação planejada estão em
[`docs/relatorio_m2.md`](relatorio_m2.md). Assim, classificador e máscaras manuais
não são requisitos obrigatórios já cumpridos na M2, embora a qualidade da saída
precise de evidência quantitativa e a limitação seja transparente.

## 9. Parte F — Plano de ação para a M2

### 9.1 Ajustes herdados da M1

| Prioridade | Problema identificado na M1 | Ação de correção | Responsável | Prazo | Evidência de conclusão |
|---|---|---|---|---|---|
| Essencial | Subconjunto do dataset removido do repositório, impedindo reprodução dos experimentos. | Não versionar o dataset; documentar fonte e preparação local. | Equipe | Atualizado em 27/10/2026 | Imagens fora do índice Git; instruções em `images/README.md`; histórico antigo não reescrito. |
| Essencial | Script de segmentação salvava resultados em diretório diferente do apresentado. | Unificar caminhos via argumentos de entrada e saída. | João Vitor Schwambach Brasil (pipeline); Luiz Gustavo Machado Muller (documentação/revisão) | Concluído na M2 | Execução reproduzível gera artefatos em `results/m2/`. |
| Importante | Segmentação avaliada em amostra pequena, sem forma de medir qualidade. | Avaliar 48 imagens e calcular Dice/IoU contra proxy, declarando a avaliação preliminar. | João Vitor Schwambach Brasil (pipeline/experimento); Luiz Gustavo Machado Muller (documentação/revisão) | Concluído parcialmente na M2 | CSV por imagem, resumo, figuras e ressalvas em `docs/relatorio_m2.md`; anotação manual ainda pendente para M3. |
| Recomendável | Divisão de dados não considerava a origem das imagens (original x variante aumentada). | Auditar duplicatas/origem e só então definir partições para classificação. | Equipe | M3 | Inventário de imagens e divisão sem vazamento, a produzir. |

### 9.2 Novos desenvolvimentos da M2

| Entrega ou resultado da M2 | Tarefa concreta | Responsável principal | Colaboradores | Prazo | Evidência esperada | Dependências ou riscos |
|---|---|---|---|---|---|---|
| Implementação inicial executável | Pipeline de leitura, segmentação, morfologia e descritores | João Vitor Schwambach Brasil | Luiz Gustavo Machado Muller (revisão) | M2 | Código em `src/tomato_pdi/`, testes e execução reproduzível | Depende da obtenção local do conjunto, não incluído no Git. |
| Segmentação | Avaliar 12 imagens por classe com indicador preliminar | João Vitor Schwambach Brasil | Luiz Gustavo Machado Muller | M2, parcialmente concluído | CSV, máscaras de exemplo e parâmetros documentados | Proxy automático não é referência manual; validar na M3. |
| Morfologia matemática | Comparar limiar HSV antes/depois de abertura 3×3 + fechamento 5×5 | João Vitor Schwambach Brasil | Luiz Gustavo Machado Muller | M2 | Dice/IoU e figura comparativa | Resultado é relativo ao proxy; melhora não comprova qualidade real. |
| Extração de características | Extrair cor, geometria e GLCM; testar separação das classes na M3 | João Vitor Schwambach Brasil (extração) | Luiz Gustavo Machado Muller (revisão/documentação) | Extração M2; discriminação M3 | `results/m2/descritores.csv`; classificador ainda não executado | Variância de segmentação e amostra pequena podem afetar descritores. |
| Experimentos com parâmetros | Comparar duas configurações morfológicas nas mesmas 48 imagens | João Vitor Schwambach Brasil | Luiz Gustavo Machado Muller | M2 | CSV, JSON, figura e análise no relatório | Métricas provisórias contra proxy. |
| Testes e casos difíceis | Testar utilitários e registrar menor/maior concordância | João Vitor Schwambach Brasil (testes/pipeline) | Luiz Gustavo Machado Muller (revisão) | M2 | Quatro testes unitários; exemplos no relatório | Caso mínimo evidencia inadequação do proxy em fundo heterogêneo. |
| Relatório técnico parcial | Consolidar método, resultados, limitações e plano M3 | Luiz Gustavo Machado Muller | João Vitor Schwambach Brasil (revisão técnica) | M2 | `docs/relatorio_m2.md` | Revisão final e confirmação das fontes pela equipe. |
| Página parcial | Atualizar estado, instruções, resultados e pendências | Luiz Gustavo Machado Muller | João Vitor Schwambach Brasil (revisão técnica) | M2 | README atualizado | Link de vídeo e commit/tag ainda serão incluídos. |
| Organização e reprodutibilidade | Documentar ambiente, comandos e obtenção de dados sem versionar o dataset | Luiz Gustavo Machado Muller | João Vitor Schwambach Brasil | M2 | README, `pyproject.toml`, `images/README.md`; dataset ignorado | Cada pessoa precisa obter versão compatível localmente. |

### 9.3 Protocolo experimental mínimo

| Elemento | Definição do grupo |
|---|---|
| Pergunta do experimento | Abertura 3×3 e fechamento 5×5 melhoram a concordância da máscara HSV com o proxy de fundo? |
| Imagens ou amostra utilizadas | 12 imagens por classe, 48 no total, escolhidas por ordenação numérica dos nomes. |
| Método principal | Limiar HSV (H 20–100, S ≥ 35, V ≥ 25), maior componente conectado e proxy Lab estimado pelos quatro cantos. |
| Configurações ou parâmetros comparados | Mesmo limiar e mesmas imagens; sem morfologia versus abertura elíptica 3×3 + fechamento elíptico 5×5. |
| Resultado esperado | Verificar se morfologia altera a concordância; não pressupor melhora. |
| Métrica ou critério de comparação | Dice e IoU por imagem e média, explicitamente contra proxy automático (avaliação preliminar). |
| Forma de registrar os resultados | `results/m2/segmentacao_metricas.csv`, `resumo.json`, duas figuras e análise em `docs/relatorio_m2.md`. |
| Limitações já previstas | Desempenho no PlantVillage não representa diretamente fotografias de campo. |

### 9.4 Distribuição das responsabilidades

| Integrante | Responsabilidades principais | Artefatos ou partes sob sua responsabilidade | Como o trabalho será validado pelo grupo |
|---|---|---|---|
| João Vitor Schwambach Brasil | Proposta e feedback M1; implementação e execução do pipeline M2 | `src/tomato_pdi/`, experimento e evidências técnicas | Revisão conjunta do código, reprodução do comando e explicação das decisões |
| Luiz Gustavo Machado Muller | Proposta e feedback M1; relatório/README, organização e revisão/validação | `README.md`, `docs/relatorio_m2.md`, `images/README.md` e documentação M2 | Conferência dos resultados gerados, comandos, fontes e consistência documental |
| Trabalho conjunto | Revisão do escopo, validação do material e preparação da apresentação | Revisão M1/M2; vídeo M2 (a gravar) | Participação identificável e validação final por ambos |

### 9.5 Evidências da implementação parcial executada

| Entrega M2 | Evidência verificada neste checkout | Situação / ação necessária |
|---|---|---|
| Código executável | `src/tomato_pdi/`; comando `python -m tomato_pdi --samples-per-class 12` | Executado em 48 imagens. |
| Comparação controlada | `results/m2/segmentacao_metricas.csv`; sem morfologia versus abertura 3×3 + fechamento 5×5 | Dice médio 0,8723 → 0,8786; IoU médio 0,7930 → 0,8030, comparados ao proxy automático. |
| Descritores | `results/m2/descritores.csv` | Área, perímetro, circularidade, médias HSV/Lab e GLCM; separação por classificador não avaliada. |
| Relatório e organização | [`docs/relatorio_m2.md`](relatorio_m2.md), README e dependências em `pyproject.toml` | Equipe deve validar o conteúdo e instalar o extra de desenvolvimento para rodar os testes. |
| Referência e dados | [`images/README.md`](../images/README.md) | Dataset removido do índice Git (remoção staged), cópia local mantida e instruções de obtenção documentadas; histórico antigo não reescrito. Equipe ainda confirma fonte/licença. |
| Contribuições, vídeo e versão de entrega | Contribuições e responsáveis preenchidos conforme divisão informada pela equipe | Gravar vídeo não listado e registrar commit/tag após revisão final. |

## 10. Parte G — Compromisso da equipe

> Texto para confirmação dos integrantes: revisamos a devolutiva da M1, identificamos as correções necessárias e registramos um plano de ação e as evidências disponíveis para a M2. A consulta da nota no diário e a divergência do subtotal ainda precisam ser conferidas; confirmaremos também que todos compreendem as tarefas e os resultados esperados.

Integrantes: João Vitor Schwambach Brasil e Luiz Gustavo Machado Muller.

Data desta revisão: 27/10/2026. A conferência da nota foi adiada; o compromisso final ainda depende da validação de ambos.

## 11. Checklist antes da entrega

- [x] identificou a equipe e a entrega avaliada;
- [x] respondeu às observações relevantes do feedback com evidências disponíveis;
- [x] diferenciou concordância e concordância parcial;
- [ ] conferiu a nota e os cálculos — conferência adiada para depois;
- [x] separou correções da M1 e novos desenvolvimentos da M2;
- [x] definiu tarefas, responsáveis e evidências de conclusão; prazos acadêmicos exatos não foram informados;
- [x] incluiu segmentação, morfologia, características e experimento no plano M2;
- [x] definiu protocolo experimental mínimo e registrou suas limitações;
- [x] registrou dependências, riscos e limitações;
- [ ] confirmou que ambos os integrantes leram, compreendem e aprovam o plano.