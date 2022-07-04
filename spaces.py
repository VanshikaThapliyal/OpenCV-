#OPENCV USES THE BGR FORMAT,outside we use RGB format
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('pictures/mouse.jpg')
cv.imshow('Mouse',img)
 
plt.imshow(img)
plt.show()
#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)
#BGR TO HSV-hue saturation value(basically how humans concieve)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
#BGR TO Lab
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB',lab)
#BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
#grayscale cannot be converted to HSV directly

#hsv to bgr
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV2BGR',hsv_bgr)
#lab to bgr
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB2BGR',lab_bgr)
cv.waitKey(0)