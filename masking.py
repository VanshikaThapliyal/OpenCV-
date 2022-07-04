#MASKING is basically when you need some certain part of the picture to be focused and the not the whole complete picture
import cv2 as cv
import numpy as np
img=cv.imread('pictures/football.jpg')
cv.imshow('Football',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank) 
#drawing circle over the blank image
mask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2 ),(img.shape[1]//2+100,img.shape[0]//2+100 ),255,-1) #width/2,height/2=centre coordinates
cv.imshow('Mask',mask) 

#creating a masked image
masked=cv.bitwise_and(img,img,mask=mask) #intersecting the image and mask
cv.imshow('Masked Image',masked)
cv.waitKey(0)