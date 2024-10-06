import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)


blank = np.zeros(img.shape[:2],dtype='uint8')
#------->
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,thickness=-1)


# masked=cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('masked',masked)

# gray_hist=cv.calcHist([gray],[0],circle,[256],[0,256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#--------------->
#color histogram
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,thickness=-1)
masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked',masked)

plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)