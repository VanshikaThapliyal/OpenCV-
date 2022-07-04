import cv2 as cv
img=cv.imread('pictures/dog.jpg') #BGR image
cv.imshow('Dog',img)
# 1. to convert image to grayscale
#in grayscale, you see the intensity of the color rather than the color itself
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#2. HOW TO BLUR AN IMAGE
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT) #(3,3) is the kernel size, as to be odd, its actually the intensity of blurr
cv.imshow('BLUR',blur)
#3. edge cascade
canny=cv.Canny(img, 125, 175) #125 and 175 are threshhold values
cv.imshow('CANNY',canny) #to reduce the edges, you may pass the blur 
#4.dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilate',dilated)
#5.Eroding
eroded=cv.erode(dilated,(7,7),iterations=1)
cv.imshow('eroded',eroded)
#6.Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#INTER_AREA used when resizing the image to dimensions smaller than the dimensions of the original pic
#INTER_LINEAR/INTER_CUBIC when doing the opposite
#INTER_CUBIC gives image of much higher quality
cv.imshow('Resize',resized)
#7.cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)