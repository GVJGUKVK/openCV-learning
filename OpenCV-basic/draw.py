import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# point the image a certain color
#blank[200:300,300:400] = 0,255,0
#cv.imshow('green',blank)

#draw the rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)


#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)
cv.imshow('circle',blank)

#draw a line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('line',blank)


#write a text
cv.putText(blank,'Hello i an good guy',(100,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)
cv.imshow('text',blank)
cv.waitKey(0)



