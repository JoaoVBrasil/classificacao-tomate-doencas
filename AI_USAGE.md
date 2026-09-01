# Uso de Inteligência Artificial Generativa

Em conformidade com a Seção 16 do enunciado da M1, declaramos de forma transparente o uso de ferramentas de IA generativa neste projeto.

## Registro de uso

| Item | Descrição |
|---|---|
| **Ferramenta utilizada** | Claude (Anthropic), via interface de chat |
| **Data** | **[31 de Agosto de 2026]** |
| **Finalidade** | A partir de uma ideia inicial já definida pelo nosso grupo (classificação de doenças em folhas de tomate usando o PlantVillage, com pipeline de segmentação + características de cor/textura + classificação clássica), pedimos ajuda para: (1) organizar a estrutura de pastas do repositório conforme o enunciado da M1; (2) redigir um rascunho inicial do `README.md` e da proposta técnica (`docs/proposta.md`), incluindo descrição do problema, objetivos, pipeline preliminar (com diagramas), arquitetura preliminar e levantamento de fatos sobre o dataset PlantVillage (origem, licença aproximada, número aproximado de imagens, classes de doenças do tomate); (3) sugerir referências bibliográficas iniciais sobre o dataset. |
| **Material produzido ou modificado com apoio da ferramenta** | `README.md`, `docs/proposta.md`, `images/README.md`, `requirements.txt`, `pyproject.toml`, `.gitignore`, este arquivo (`AI_USAGE.md`) |

Nosso grupo leu integralmente o README e a proposta técnica gerados e 
discutiu cada seção, garantindo que todos entendessem e 
concordassem com as decisões apresentadas. Especificamente:

- Conferimos o número de imagens e a lista de classes de doenças do 
  tomate diretamente na página do dataset em [fonte escolhida], 
  confirmando os valores citados na proposta.
- Verificamos a licença do dataset na fonte específica que baixamos 
  ([https://data.mendeley.com/datasets/tywbtsjrjv/1]).
- Testamos a instalação das dependências listadas em requirements.txt 
  em ambiente local, confirmando que o notebook roda sem erros.

Todos os integrantes são capazes de explicar e justificar oralmente 
as decisões técnicas apresentadas neste documento.


## O que a ferramenta **não** fez

A IA não teve acesso a nenhuma imagem real do dataset, não executou nenhum experimento, não escolheu o tema do projeto (já definido pelo grupo antes desta conversa) e não pode atestar, em nome do grupo, que a investigação de viabilidade foi de fato realizada. As Seções 8 ("Estudo inicial de viabilidade") e 12 ("Próximos passos") de `docs/proposta.md` deixam essa distinção explícita e continuam válidas até que o grupo as reescreva com resultados reais.

## Responsabilidade

O grupo permanece integralmente responsável pelo conteúdo entregue e deve ser capaz de explicar e justificar, sem apoio de texto, qualquer decisão técnica registrada neste repositório — inclusive no vídeo da M1.
