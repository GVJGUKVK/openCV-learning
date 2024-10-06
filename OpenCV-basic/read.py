import cv2 as cv
#img = cv.imread("Photos/cat_large.jpg") #讀取圖片
#cv.imshow('Cat', img) #顯示圖片(視窗名稱,檔案)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


#cv.waitKey(0) #等待按下按鍵時間,0無限長