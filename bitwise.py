import cv2 as cv
#four basic bitwise operators=and or XOR not
#bitwise operators operate in binary
#a pixel is turned off it has a value of zero and turned on if it has a value 1
import numpy as np
blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1) #-1 to fill this image,255->all 255 i.e white
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)
#bitwise AND -->intersecting regions
bitwise_and=cv.bitwise_and(circle,rectangle)
cv.imshow('BITWISE_AND',bitwise_and) #showing intersection of both the images
#bitwise OR -->non intersecting and intersecting regions
bitwise_or=cv.bitwise_or(circle,rectangle)
cv.imshow('BITWISE_OR',bitwise_or) #dosen't scrape out the rest area,basically superimpose
#bitwise XOR --> non intersecting regions
bitwise_xor=cv.bitwise_xor(circle,rectangle)
cv.imshow('BITWISE_XOR',bitwise_xor)
#bitwise NOT -->inverses the color,takes only one argument
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('BITWISE_NOT',bitwise_not)
cv.waitKey(0)