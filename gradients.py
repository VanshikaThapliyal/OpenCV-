import cv2 as cv
import numpy as np
img=cv.imread('pictures/football.jpg')
cv.imshow('Football',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#laplacian
lap =cv.Laplacian(gray,cv.CV_64F) #CV_64F ddepth
lap =np.uint8(np.absolute(lap)) #absolute(lap)-pixels converting into absolute value
cv.imshow('Laplacian',lap)
 
#Sobel-computes gradient in 2 directions- x & y
sobelx=cv.Sobel(gray,cv.CV_64F,1,0) #dx=1,dy=0
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('SobelX',sobelx)
cv.imshow('Sobely',sobely)
cv.imshow('Combined_Sobel',combined_sobel)

canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)