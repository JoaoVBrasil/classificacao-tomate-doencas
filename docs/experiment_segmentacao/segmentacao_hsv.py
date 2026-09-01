import cv2
import numpy as np
import os


def segmentar_folha(caminho):
    imagem = cv2.imread(caminho)

    if imagem is None:
        raise FileNotFoundError(caminho)

    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)

    mascara = ((H >= 20) & (H <= 100) & (S >= 35) & (V >= 25)).astype(np.uint8) * 255

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)

    n, labels, stats, _ = cv2.connectedComponentsWithStats(mascara, 8)

    if n > 1:
        maior = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        mascara = np.where(labels == maior, 255, 0).astype(np.uint8)

    segmentada = cv2.bitwise_and(imagem, imagem, mask=mascara)

    return mascara, segmentada


if __name__ == "__main__":

    classes = [
        "Tomato___healthy",
        "Tomato___Late_blight",
        "Tomato___Septoria_leaf_spot",
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus"
    ]

    for classe in classes:

        pasta = f"images/tomato_subset/{classe}"
        arquivos = os.listdir(pasta)

        imagem = None

        for arquivo in arquivos:
            if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
                imagem = arquivo
                break

        caminho = os.path.join(pasta, imagem)

        mascara, segmentada = segmentar_folha(caminho)

        cv2.imwrite(f"mascara_{classe}.png", mascara)
        cv2.imwrite(f"folha_segmentada_{classe}.png", segmentada)

        print(f"Processada: {classe}")