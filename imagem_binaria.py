import cv2
import numpy as np
import matplotlib.pyplot as plt

# ler a imagem e coloca-la em Escala-de-Cinza
img = cv2.imread('osso.png')
imgBinaria = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fundo = 255 # cor branca
objeto = 0 # cor preta

qtLinhas, qtColunas = imgBinaria.shape
##############################################################################################

# calcula a coordenada do centróide do objeto
centroideX = 0
centroideY = 0 
totalPontos = 0

for i in range(1, qtLinhas - 1):
    for j in range(1, qtColunas - 1):
        if imgBinaria[i, j] == objeto:
            centroideX = centroideX + i
            centroideY = centroideY + j
            totalPontos += 1

centroideX = int(centroideX/totalPontos)
centroideY = int(centroideY/totalPontos)

centroide = (centroideX, centroideY)

# adiciona um círculo verde no centróide da imagem
cv2.circle(img, centroide, 1, (0,255,0), 10)

##############################################################################################

# cria uma imagem toda preta com as mesmas medidas da imagem original
imgContorno = np.zeros((qtLinhas, qtColunas), dtype = int)

# percorre toda a imagem original
for i in range(1, qtLinhas - 1):
    for j in range(1, qtColunas - 1):

        # se a posiçaõ [i, j] da imagem original for preta, vai comparar seus vizinhos para
        # mudar a cor da posição [i, j] na imagem do contorno (no caso de ser um ponto de
        # contorno)
        if(imgBinaria[i, j] == objeto):

            A = imgBinaria[i - 1, j]
            B = imgBinaria[i + 1, j]
            C = imgBinaria[i, j + 1]
            D = imgBinaria[i, j - 1]

            if (A == fundo or B == fundo or C == fundo or D == fundo):
                imgContorno[i, j] = 255

##############################################################################################

# calcula a Relaçao de Aspecto da imagem
x, y, w, h = cv2.boundingRect(imgBinaria)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

if (h > w):
    relação_aspecto = float(w)/h
else:
    relação_aspecto = float(h)/w

##############################################################################################

# demarcar os espaços não-convexos

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, imgBinariaC = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(imgBinariaC,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints = False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    cv2.line(img, start, end, [0,255,0], 2)

##############################################################################################

# código para definir a solidez

img3 = cv2.imread('osso1.png')
gray3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img3B = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(img3B, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnt = contours[0]

hull = cv2.convexHull(contours[0])
hull_area = cv2.contourArea(hull)
area_objeto = cv2.contourArea(contours[0])
solidez = area_objeto / hull_area

print('área não convexa: ', hull_area)
print('área do objeto: ', area_objeto)
print('solidez: ', solidez)