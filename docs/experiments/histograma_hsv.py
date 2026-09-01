import cv2
import os
import matplotlib.pyplot as plt

dataset_path = "images/tomato_subset"

classes = [
    "Tomato___healthy",
    "Tomato___Late_blight",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus"
]

quantidade_imagens = 20

for classe in classes:
    pasta = os.path.join(dataset_path, classe)
    arquivos = os.listdir(pasta)

    imagens = []
    for arquivo in arquivos:
        if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
            imagens.append(arquivo)

    imagens = imagens[:quantidade_imagens]

    histograma_medio = None

    for arquivo in imagens:
        caminho = os.path.join(pasta, arquivo)

        imagem = cv2.imread(caminho)
        hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

        # Calcula o histograma do canal H (matiz)
        histograma = cv2.calcHist(
            [hsv],
            [0],
            None,
            [180],
            [0, 180]
        )

        histograma = cv2.normalize(
            histograma,
            None,
            0,
            1,
            cv2.NORM_MINMAX
        )

        if histograma_medio is None:
            histograma_medio = histograma
        else:
            histograma_medio += histograma

    histograma_medio /= len(imagens)

    plt.plot(histograma_medio, label=classe)

plt.title("Distribuição de matiz (H) das classes")
plt.xlabel("Matiz (H)")
plt.ylabel("Frequência normalizada")
plt.legend()
plt.grid()
plt.show()