import cv2 as cv  #cv is now a subclass in cv2
#img = cv.imread('pictures/dog.jpg')#imread loads the image
#cv.imshow('Dog',img)  #displaying as a window
#cv.waitKey(0)  #keybinding function, waits for infinite time until a key is pressed

#now reading videos
capture=cv.VideoCapture('videos/dog.mp4') #0 means the web cam has access to the videos
while True:
    isTrue, frame= capture.read()#capture.read will read the video frame by frame and will store it in variable frame
    cv.imshow('Video',frame)

    #now to stop the video form being played infinetly
    if cv.waitKey(3) & 0xFF==ord('d'): #if key "d" is pressed then break out of the loop
        break
capture.release() #releasing the capture window
cv.destroyAllWindows #destroying the window