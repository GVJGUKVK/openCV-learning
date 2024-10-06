import cv2 as cv
img = cv.imread("Photos/cat.jpg") #讀取圖片


def rescaleFrame(frame, scale=0.75):
    #image,video,live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image= rescaleFrame(img)
cv.imshow('Cat', resized_image) #顯示圖片(視窗名稱,檔案)
capture = cv.VideoCapture('Videos/dog.mp4')

def chageRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) 