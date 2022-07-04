import cv2 as cv
img=cv.imread('pictures/balloon.jpg')
cv.imshow('Balloon',img) #kernel size basically no. of rows and columns
#AVERAGE BLUR, we take the middle pixel intensity which is the average of the pixel intensities around it
average=cv.blur(img,(7,7))#(3,3) is the kernel size
cv.imshow('Average Blur',average)
#GAUSSIAN BLUR, similar to average blurring but we use a weighted mean where neighbourhood pixels closer to
#to the central pixel contribute more weight to the average
gauss=cv.GaussianBlur(img,(7,7),0) #0 is standard deviation towards x
cv.imshow('GAUSSIAN blur',gauss)
#MEDIAN BLUR,similar to average but instead we find the median of the surrounding pixels-better blurring than guass and average
median=cv.medianBlur(img,7) #we take only 3 because it is automatically assumed to be a tuple of 3,3 size
cv.imshow('Median',median)
#BILATERAL BLUR,blurring will take place but the edges will be retained
bilateral=cv.bilateralFilter(img,10,35,25) #5 ->Diameter of each pixel neighborhood,15->SigmaColor,colors farther to each other will get mixed
#15-> sigmaSpace,more further pixels will get mixed
cv.imshow('BILATERAL',bilateral)
cv.waitKey(0)