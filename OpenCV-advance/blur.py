import cv2 as cv


img = cv.imread("Photos/Park.jpg") 
cv.imshow('Park', img)

#Averaging blur
average=cv.blur(img,(3,3))
cv.imshow('average blur',average)

#Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Gaussian blur',gauss)

#median blur
median=cv.medianBlur(img,3)
cv.imshow('Median blur',median)

#bilateral blur
bilateral=cv.bilateralFilter(img,5,35,35)
cv.imshow('bilateral blur',bilateral)

cv.waitKey(0)