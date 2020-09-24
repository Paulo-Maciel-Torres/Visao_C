import cv2
import numpy as np
from matplotlib import pyplot as plt

# lê a imagem
img = cv2.imread('lena.jpg')

# calcHist: Calcula o histograma da imagem
histograma_B = cv2.calcHist([img], [0], None, [256], [0,255])
histograma_G = cv2.calcHist([img], [1], None, [256], [0, 255])
histograma_R = cv2.calcHist([img], [2], None, [256], [0, 255])

# normalizando os histogramas
histograma_B = (histograma_B - np.amin(histograma_B)) / (np.amax(histograma_B) - np.amin(histograma_B))
histograma_G = (histograma_G - np.amin(histograma_G)) / (np.amax(histograma_G) - np.amin(histograma_G))
histograma_R = (histograma_R - np.amin(histograma_R)) / (np.amax(histograma_R) - np.amin(histograma_R))

# calcula a distância euclidiana
def distancia(histograma1, histograma2):
    ''' RECEBE DOIS HISTOGRAMAS E DEVOLVE A DISTÂNCIA EUCLIDIANA
    ENTRE ELES '''
    soma = 0
    for i in range(len(histograma1)):
        soma = soma + (histograma1[i] - histograma2[i]) ** 2
    return np.sqrt(soma)

# plot: plota algo a um gráfico, no caso, o histograma.
plt.plot(histograma_B, color = 'b')
plt.plot(histograma_G, color = 'g')
plt.plot(histograma_R, color = 'r')
# show: mostra o gráfico
plt.show()