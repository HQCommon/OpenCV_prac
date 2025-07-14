import cv2 as cv  

def rescaleFrame(frame, scale=0.75):\
    # Images, Video, Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# img = cv.imread('Photos/FELV-cat.jpg')
# cv.imshow('Cat', img)

# cv.imshow('Cat_Resized', rescaleFrame(img, scale=2))

# cv.waitKey(0)

def changeRes(width, height): #Research more about this?
    #Live Video
    capture.set(3,width)
    capture.set(5,height)

# Reading Videos
capture = cv.VideoCapture('Photos/1.mp4')

while True:
    isTrue, frame = capture.read() #While there is a frame, it's true to show

    #frame_resized = rescaleFrame(frame, scale=2)
    cv.imshow('Arma Video', frame)
    #cv.imshow('Video Resized', frame_resized)

    #0xFF==ord('key') < whatever key is, closes the window... break is hit
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()