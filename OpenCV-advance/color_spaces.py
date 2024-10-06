import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/cats.jpg')
cv.imshow('cats',img)
#BGR(openCV) RGB(matplotlib)
# plt.imshow(img)
# plt.show()

# BGR 2 Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR 2 HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR 2 L*a*b
lab= cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('l*a*b',lab)

#BGR 2 RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)



#HSv 2 BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV 2 BGR',hsv_bgr)
cv.waitKey(0)