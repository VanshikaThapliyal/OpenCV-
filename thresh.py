#thresholding is basically binarizing an image
#if pixel vale is less than the threshold value then we set that pixel intensity value to zero
#and if it is above than the threshold value then we set it to 255/white

import cv2 as cv
from cv2 import threshold
from cv2 import ADAPTIVE_THRESH_MEAN_C
from cv2 import ADAPTIVE_THRESH_GAUSSIAN_C
img=cv.imread('pictures/balloon.jpg')
cv.imshow('Balloon',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Thresholding
threshold,thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY) #threshold value is 155 and if the pixel value>threshold value then set it to 255
cv.imshow('Simple Threshold',thresh)

#threshold inverse
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) #we are doing the inverse here
cv.imshow('Simple Thresholded Inverse',thresh_inv)

# Adaptive Thresholding - computer will find the optimal threshold value
adaptive_thresh=cv.adaptiveThreshold(gray,255,ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,9) #11-kernel size
cv.imshow('Adaptive Thresholding',adaptive_thresh)
cv.waitKey(0)