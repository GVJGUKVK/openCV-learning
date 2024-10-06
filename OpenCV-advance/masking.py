import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)


blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank image',blank)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,thickness=-1)
cv.imshow('Circle',circle)

masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',masked)
cv.waitKey(0)