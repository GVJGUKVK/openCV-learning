import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#lapacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lapacian',lap)

#sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobel X',sobelx)
cv.imshow('sobel Y',sobely)
cv.imshow('combined sobel',combined_sobel)



cv.waitKey(0)