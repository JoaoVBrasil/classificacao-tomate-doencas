### Experimento: segmentação folha/fundo em imagens reais do PlantVillage

Testamos o código de segmentação em uma imagem de cada uma das quatro classes 
trabalhadas (`healthy`, `Late_blight`, `Septoria_leaf_spot` e 
`Tomato_Yellow_Leaf_Curl_Virus`), usando limiarização em HSV seguida de 
limpeza morfológica, para ver se conseguíamos separar bem a folha do fundo.

**O que fizemos:** convertemos a imagem pra HSV e usamos uma faixa de matiz, 
saturação e valor pra marcar o que é folha. Depois limpamos ruído com abertura 
e fechamento morfológico, e ficamos só com o maior "pedaço" conectado (pra 
descartar qualquer resíduo isolado).

**Resultado:**

| Classe | Segmentação funcionou? |
|---|---|
| `healthy` | Sim, contorno ficou bem fiel à folha |
| `Late_blight` | Sim, até as partes necrosadas na borda ficaram certas |
| `Septoria_leaf_spot` | Sim, as manchas escuras não atrapalharam |
| `Tomato_Yellow_Leaf_Curl_Virus` | Só parcialmente — a máscara ficou meio "quadrada" e cortou pedaço da folha |

**O que achamos disso:** pra 3 das 4 classes o método funcionou bem de 
primeira. O problema apareceu só no Yellow Leaf Curl Virus, que deixa a folha 
bem amarelada — nossa hipótese é que esse amarelo tá saindo da faixa de matiz 
que configuramos pra detectar "folha", então parte da folha real acaba sendo 
tratada como fundo.

Isso é um ponto de atenção real pra próxima etapa: talvez precisemos ajustar 
a faixa de cor pra essa classe especificamente, ou pensar numa segmentação 
que não dependa tanto de limiares fixos.

**Próximo passo:** esse teste foi feito com só 1 imagem por classe, então 
ainda não dá pra saber se esse problema do Yellow Leaf Curl Virus se repete 
sempre ou foi só naquela imagem. Isso fica pra ser testado com mais calma 
mais pra frente.