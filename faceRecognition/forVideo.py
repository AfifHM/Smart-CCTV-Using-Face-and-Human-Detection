import os
import cv2
import numpy as np
import faceRecognition as fr


#Merupakan bagian untuk load data training dan capture video dari sumber
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Load data training yang sudah tersimpan sebelumnya

name = {0 : "TestImages", 1 : "Ronalod", 2 : "Faruq", 3 : "Fadhil", 4 : "Unknown"}


cap=cv2.VideoCapture(r'D:\Data Pribadi\Akademik\Kuliah\Semester 7\Kerja Praktek\FaceRecognition-master\Data\Fadhil Naila 1.mp4')

while True:
    ret,test_img=cap.read()#capture frame dari video dan mengembalikan 2 nilai yaitu gambar dan nilai boolean dari gambar
    faces_detected,gray_img=fr.faceDetection(test_img)
    print("faces_detected:",faces_detected)


    for (x,y,w,h) in faces_detected:
      cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,0,255),thickness=4) #menggambar kotak untuk wajah

    resized_img = cv2.resize(test_img, (1280, 720)) #mengatur ulang ukuran gambar menjadi yang diinginkan
    cv2.imshow('face detection Tutorial ',resized_img)
    cv2.waitKey(10)


    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#Memprediksi identitas wajah
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if confidence < 50: #Jika confidence kecil dari 50 maka print identitas wajah
           fr.put_text(test_img,predicted_name,x,y)
        else:
            predicted_name=name[4]
            fr.put_text(test_img,predicted_name,x,y)


    resized_img = cv2.resize(test_img, (1280, 720))
    cv2.imshow('face recognition tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'): #Tekan q untuk menghentikan atau tunggu hingga akhir video
        break

cap.release()
cv2.destroyAllWindows()