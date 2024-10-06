
import os
import cv2 as cv
import numpy as np

# 定義人物名單和訓練圖像的路徑
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'/Users/wangxiaowen/Desktop/opencv-course-master/Resources/Faces/train'

# 加載 Haar 紋理檔
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# 初始化 features 和 labels 列表
features = []
labels = []

# 創建訓練數據
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)  # 取得人物的標籤

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # 讀取圖像並轉換為灰階
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # 檢測臉部
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # 將檢測到的臉部區域添加到 features 列表
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# 執行創建訓練數據的函數
create_train()
print('Training Done----------')

# 將 features 和 labels 轉換為 NumPy 陣列
features = np.array(features, dtype='object')
labels = np.array(labels)

# 創建人臉識別器
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# 訓練人臉識別器
face_recognizer.train(features, labels)

# 保存訓練好的模型和數據
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
