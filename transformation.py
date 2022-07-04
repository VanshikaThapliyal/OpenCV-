#translation,rotation,resizing,clipping,cropping
import cv2 as cv
import numpy as np
img=cv.imread('pictures/football.jpg')
cv.imshow('Football',img)
#1.Translation-shifting the image along x and y axis
def translate(img,x,y):
    transMAT=np.float32([[1,0,x],[0,1,y]]) #affine transformation matrix
    dimensions=(img.shape[1],img.shape[0]) #width and height
    return cv.warpAffine(img,transMAT,dimensions) #performing the image translation
#-x --> left
#-y --> up
#x-->right
#y-->down
translated=translate(img,100,100) #100 towards right and 100 down
cv.imshow('Translated',translated)
#rotation
def rotate(img, angle,rotPoint=None):
    (height,width)=img.shape[:2]#grabbing the height and width of the image
    if rotPoint is None:
        rotPoint =(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) #we are not bothered by the scale so set it to 1.0
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45) #positive means anticlockwise and negative means clockwise
rotateAgain=rotate(rotated,45)
cv.imshow('Rotated',rotated)
cv.imshow('rotateAgain',rotateAgain)
#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)
#flipping
flip=cv.flip(img,-1) #0 --> flipping along x axis, 1 --> flipping along y axis , -1 --> both
cv.imshow('Flipped',flip)
cropped=img[200:400,300:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)