import cv2
import numpy as np
from matplotlib import pyplot as plt

# lê a imagem e armazena e duas variáveis seu tamanho
img = cv2.imread('lena.jpg')
qt_linhas, qt_colunas = img.shape

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

# calcula o padrão lbp de uma imagem
def lbp(img, qt_linhas, qt_colunas):
    img2 = np.zeros((qt_linhas, qt_colunas), dtype = int)

    for i in range(1, qt_linhas - 1):
        for j in range(1, qt_colunas - 1):

            Centro = img[i, j]

            A = img[i - 1, j]
            B = img[i - 1, j + 1]
            C = img[i, j + 1]
            D = img[i + 1, j + 1]
            E = img[i + 1, j]
            F = img[i + 1, j - 1]
            G = img[i, j - 1]
            H = img[i - 1, j - 1]

            soma = 0
            if(A > Centro):
                soma = soma + (2**0)
            if(B > Centro):
                soma = soma + (2**1)
            if(C > Centro):
                soma = soma + (2**2)
            if(D > Centro):
                soma = soma + (2**3)
            if(E > Centro):
                soma = soma + (2**4)
            if(F > Centro):
                soma = soma + (2**5)
            if(G > Centro):
                soma = soma + (2**6)
            if(H > Centro):
                soma = soma + (2**7)

            img2[i , j] = soma
    return img2

# plot: plota algo a um gráfico, no caso, o histograma.
plt.plot(histograma_B, color = 'b')
plt.plot(histograma_G, color = 'g')
plt.plot(histograma_R, color = 'r')
# show: mostra o gráfico
plt.show()