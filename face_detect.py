import cv2 as cv

img = cv.imread('Photos/face.jpg')
cv.imshow('Faces', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Group', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=23)
print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 4)

cv.imshow('Detected Faces', img)

cv.waitKey(0)