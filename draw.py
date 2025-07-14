import cv2 as cv
import numpy as np

#.shape = [height, width, color channels]

blank = np.zeros((500,500, 3), dtype = 'uint8')  #(500,500,3), height, width, color channels (red, gree, blue)
cv.imshow('Blank', blank)
#print("Height =", blank.shape[0], " Width =", blank.shape[1], " Color channels:", blank.shape[2])

# ____________________________________________1. Paint the image a certain color
#blank[:] = 255,0,0 #the [:] means use all pixels
blank[200:300, 300:400] = 255,0,0 # sing certain pixels 200 - 300 and 300 - 400 pixel dimensions are used
cv.imshow('Green', blank)

# ____________________________________________2. Draw a Rectangle
# could use thickness=cv.FILLED to fill box or -1
cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=-1) #makes a rectangle from 0,0 (origin) to (250,250) point, with a thickens of lines of 2
cv.imshow('Rectangle', blank)

# ____________________________________________3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# ____________________________________________4. Draw a line
cv.line(blank, (100,250), (300,400), (0,0,255), thickness=2)
cv.imshow('Line', blank)

# ____________________________________________5. Write Text
cv.putText(blank, "Sup this is text", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)