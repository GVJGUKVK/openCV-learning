import cv2 as cv
import numpy as np
img = cv.imread('Photos/Park.jpg') 

cv.imshow('Park',img)

#translate
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#x-right,y-down

translated=translate(img,-100,100)
cv.imshow('Translate',translated)

#rotate
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions= (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated= rotate(img,45) #角度正=>逆時針旋轉
cv.imshow('Rotated',rotated)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
  

#flip
flip=cv.flip(img,1)      #0-->up and down  1-->right and left -1-->both
cv.imshow('flip',flip)

#Cropping
cropped= img[200:400,300:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)