import cv2

imagem = cv2.imread('Imagens_teste_canecas/teste01.png')

#classificador = cv2.CascadeClassifier('cascade_caneca1.xml')
classificador = cv2.CascadeClassifier('cascade_caneca2.xml')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza,
                                           scaleFactor=1.25,
                                           minNeighbors=4)

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0,255, 0), 2)

cv2.imshow('Detector de Canecas', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()