import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/FELV-cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV < Hue Saturation Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# LAB to BGR
hsv_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)