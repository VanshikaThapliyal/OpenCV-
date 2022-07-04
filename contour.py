#contours are the boundaries of objects,line that joins the points or curves around the boundaries
import cv2 as cv
import numpy as np
img=cv.imread('pictures/balloon.jpg')
cv.imshow('Balloon',img)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
#blurring the image
#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)
canny=cv.Canny(blur,125,175) #findingg edges
cv.imshow('canny',canny)
#threshhold method-binarize that image
ret ,thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY) #125=threshhold value, 255=maximum value 
#if pixel<125 then it is set to 0 and black, if pixel>125 then it is set to 255 and white
cv.imshow('Thresh',thresh)
contours ,hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 
#cv.CHAIN_APPROX_NONE is approximation method
#cv.RETR_TREE for all hierarichal contours,RETR_EXT if only external contours,RETR_LIST if all contours
print(f'{len(contours)} contour(s) found!' )
#drawing contours
cv.drawContours(blank,contours,-1,(0,0,255),1)#-1 for all contours,red color contours
cv.imshow('Contours Drawn',blank)
cv.waitKey(0)