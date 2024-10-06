import cv2 as cv

img = cv.imread('Photos/Park.jpg')
cv.imshow('park',img)

#convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Coscode
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#dilated
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#eroded
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('eroded',eroded)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropped
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)