# gerekli kütüphaneler
import cv2
import numpy as np

# haarcascade dosyasını python dosyasının bulunduğu dizine kaydedin
cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('image.jpg') # resmi okuduk
img = cv2.resize(img, (500,750)) # resmi 500x700 olarak boyutlandırdık
copy = img.copy() # resmi kopyaladık
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
eyes = cascade.detectMultiScale (gray,1.3,5) # gözleri tespit ettik
for (ex,ey,ew,eh) in eyes: # çizeceğimiz karelerin boyutları
    cv2.rectangle(copy,(ex,ey),(ex+ew, ey+eh), (0,255,0),2)
    
stack = np.hstack([img,copy])
cv2.imshow('Output', stack)
cv2.waitKey(0)





