import cv2 as cv
import numpy as np #importing the numpy package we downloaded
#now we create a blank image 
blank=np.zeros((500,500,3) ,dtype='uint8') #dtype is the data type of the image, 3=no. of color channels
cv.imshow('Blank',blank)
#1. paint the image a certain color
#blank[200:300,300:400]=0,255,0 #referncing all the pixels with [:]
#2. Draw a rectangle
# cv.rectangle(blank,(0,0),(500,250),(0,255,0),thickness=cv.FILLED) #cv.FILLED fills the rectangle with color
# #3.Draw a circle 
# cv.circle(blank,(250,250),40,(0,0,250),thickness=-1)#thickness=-1 fills the shape with color
# cv.imshow('Circle',blank)
# #4.Draw a line
# cv.line(blank,(0,250),(250,250),(255,255,255),thickness=3)
# cv.imshow('Line',blank)
# #5.Write text
cv.putText(blank,'Hello, My name is Vanshika',(0,250),cv.FONT_HERSHEY_TRIPLEX,0.75,(0,255,0),thickness=0)
cv.imshow('TEXT',blank)
#cv.imshow('Rectangle',blank)
#cv.imshow('Green',blank)
cv.waitKey(0)