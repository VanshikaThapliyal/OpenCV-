import cv2 as cv
img = cv.imread('pictures/large_cat.jpg')
cv.imshow('CAT',img)

#now declaring a function that can reset the frames
def rescaleFrame(frame, scale=0.25):
    width=int(frame.shape[1]*scale)   #frame.shape[1] is the width of the image
    height=int(frame.shape[0]*scale) #frame.shape[1] is the height of the image
    dimensions =(width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #INTER_AREA is one of the interpolation methods
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)
#changing the resolution
def changeRes(width,height):
    #this method only works for live videos
    capture.set(3,width)
    capture.set(4,width)
capture=cv.VideoCapture('videos/dog.mp4') #0 means the web cam has access to the videos
while True:
    isTrue, frame= capture.read()#capture.read will read the video frame by frame and will store it in variable frame
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    #now to stop the video form being played infinetly
    if cv.waitKey(20) & 0xFF==ord('d'): #if key "d" is pressed then break out of the loop
        break
capture.release() #releasing the capture window
cv.destroyAllWindows

cv.waitKey(0)