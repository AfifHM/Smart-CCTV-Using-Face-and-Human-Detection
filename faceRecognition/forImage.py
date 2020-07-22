import cv2
import os
import numpy as np
import faceRecognition as fr


#Modul untuk input gambar
test_img=cv2.imread(r'D:\Data Pribadi\Akademik\Kuliah\Semester 7\Kerja Praktek\FaceRecognition-master\TestImages\Tes13.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)


#Bagian untuk mentraining data dari folder yang telah disediakan
#faces,faceID=fr.labels_for_training_data('trainingImages')
#face_recognizer=fr.train_classifier(faces,faceID)
#face_recognizer.write('trainingData.yml')


#Load data training yang telah ditrain sebelumnya
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Read data training untuk diload

name={0:"Taylor",1:"Ronaldo",2:"Faruq",3:"Fadhil",4:"Unknown"}#Membuat id untuk tiap identitas

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#prediksi label untuk gambar dan wajah yang terdeteksi
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence<50):#Jika confidence lebih dari 50 maka tidak akan diprint id wajah
        fr.put_text(test_img,predicted_name,x,y)
    else:
        predicted_name=name[4]
        fr.put_text(test_img,predicted_name,x,y)
        

resized_img=cv2.resize(test_img,(1280,720))
cv2.imshow("face detecetion tutorial",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows
