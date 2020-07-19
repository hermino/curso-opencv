import cv2

imagem = cv2.imread('pessoas.jpg')
classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza,
                                           scaleFactor=1.09,
                                           minNeighbors=7,
                                           minSize=(30,30),
                                           maxSize=(100,100))

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0,255, 0), 2)

cv2.imshow('Detector de Faces', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()