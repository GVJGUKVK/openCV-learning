import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),thickness=-1)
circle=cv.circle(blank.copy(),(200,200),200,(255,255,255),thickness=-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('circle',circle)

#bitewise_and
bitewise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bitewise_and',bitewise_and)

#bitewise_or
bitewise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitewise_or',bitewise_or)

#bitewise_XOR
bitewise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitewise_XOR',bitewise_xor)

#bitewise_NOT
bitewise_not=cv.bitwise_not(rectangle,circle)
cv.imshow('bitewise_not',bitewise_not)

cv.waitKey(0)