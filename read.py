import cv2 as cv   

img = cv.imread('Photos/FELV-cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)

# Reading Videos
# capture = cv.VideoCapture('Photos/1.mp4')

# while True:
#     isTrue, frame = capture.read() #While there is a frame, it's true to show
#     cv.imshow('Arma Video', frame)

#     #0xFF==ord('key') < whatever key is, closes the window... break is hit
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

