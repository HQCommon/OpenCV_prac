import cv2 as cv

img = cv.imread('Photos/FELV-cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
                                      #Pixel intensity greater than 150 is shown and less than 255
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh= cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)

# There's Gaussian thresholding which takes the weight of the pixels and applies to the frame right then down to right

cv.waitKey(0)