import cv2 as cv

img = cv.imread('Photos/FELV-cat.jpg')

cv.imshow('Cat', img)

# Converting image to Greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)