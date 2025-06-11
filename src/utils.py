# src/ia_uv_semafaro/utils.py

import cv2
import numpy as np
from ia_uv_semafaro.algoritmos.MapaSemafaro import cor_para_forma

def detectar_cores_e_formas(imagem_path: str):
    imagem = cv2.imread(imagem_path)
    if imagem is None:
        print("Erro: imagem não encontrada.")
        return []

    imagem = cv2.resize(imagem, (600, 800))
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    resultados = []

    faixas = {
        "VERMELHO": [
            ((0, 100, 100), (10, 255, 255)),
            ((160, 100, 100), (180, 255, 255))
        ],
        "AMARELO": [((20, 100, 100), (35, 255, 255))],
        "VERDE": [((40, 100, 100), (90, 255, 255))]
    }

    for cor, ranges in faixas.items():
        mascara_total = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for faixa in ranges:
            mascara = cv2.inRange(hsv, faixa[0], faixa[1])
            mascara_total = cv2.bitwise_or(mascara_total, mascara)

        pixels_detectados = cv2.countNonZero(mascara_total)

        if pixels_detectados > 500:
            forma = cor_para_forma(cor)
            resultados.append((cor, forma))

    return resultados
