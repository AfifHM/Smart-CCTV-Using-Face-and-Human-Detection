import os
import cv2
import numpy as np
import faceRecognition as fr
import HumanDetection as hd
import time
from playsound import playsound

#variabel status ruangan. 0 = empty, 1 = uknown, 2 = known
status = 0
#variabel timestamp
tsk = [0,0,0,False] #untuk durasi status known, mendeteksi ruang kosong (isempty)
tsu = [0,0,0,False] #untuk durasi status unkown

#Merupakan bagian untuk load data training dan capture video dari sumber
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Load data training yang sudah tersimpan sebelumnya

name = {0 : "TestImages", 1 : "Ronalod", 2 : "Faruq", 3 : "Fadhil", 4 : "Unknown"}
#Nama Video untuk presentasi final
# known1 -> known, isempty
# coba14 -> unknown alarm
# coba 16 -> unknown alarm
# CekFadhilFaruqNaila1 -> deteksi beberapa orang sekaligus
filename = '\coba16'
hog = hd.initiate()
cap=cv2.VideoCapture('D:\Bahan Kuliah\PyCharm Projects\FaceRecog\Video'+ filename +'.mp4')
fps_read = cap.get(cv2.CAP_PROP_FPS)
print("Input Video FPS :",fps_read)
height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Input Video Frame Size : ",width," x ",height)
out = cv2.VideoWriter(
    'output '+ 'coba16' +'.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    fps_read,
    (640,480))

while (cap.isOpened()):

    ret,test_img=cap.read()#capture frame dari video dan mengembalikan 2 nilai yaitu gambar dan nilai boolean dari gambar
    if ret :
        # Resizing Image for faster detection
        resized_img = cv2.resize(test_img, (640, 480))
        #resized_img = test_img
        timer = cv2.getTickCount()
        if status == 0 or status == 1: #apabila status sebelumnya empty atau unknown

            faces_detected,gray_img=fr.faceDetection(resized_img)
            #print("faces_detected:",faces_detected)





            for (x,y,w,h) in faces_detected:
                cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,0,255),thickness=2) #menggambar kotak untuk wajah


                #cv2.imshow('face detection Tutorial ',resized_img)



            for face in faces_detected:
                (x,y,w,h)=face
                roi_gray=gray_img[y:y+w, x:x+h]
                label,confidence=face_recognizer.predict(roi_gray)#Memprediksi identitas wajah
                print("confidence:",confidence)
                print("label:",label)
                fr.draw_rect(resized_img,face)
                predicted_name=name[label]
                if confidence < 80: #Jika confidence kecil dari 80 maka print identitas wajah
                    fr.put_text(resized_img,predicted_name,x,y)
                    status = 2 #ubah status jadi known
                else:
                    predicted_name=name[4]
                    fr.put_text(resized_img,predicted_name,x,y)
                    status = 1 #ubah status jadi uknown


        if status == 0 or status == 1 :
            regions = hd.detect(hog, resized_img, (4,4), (4, 4), 1.2)
            hd.boxes(resized_img, regions)
            if len(regions) !=0 : #terdeteksi manusia
                if status == 0 :
                    status = 1
                print('Human Detected')
                #update durasi
                if tsu[3] == False:
                    tsu[0] = time.time()
                    tsu[3] = True
                elif tsu[3] == True:
                    tsu[1] = time.time()
                    tsu[2] = tsu[1] - tsu[0]

                tsk = [0, 0, 0, False]




        if status == 2 :
            tsu =[0,0,0,False] #reset
            regions = hd.detect(hog, resized_img, (4,4), (4, 4), 1.2)
            hd.boxes(resized_img, regions)
            if len(regions) == 0:
                print('Human Not Detected')
                if tsk[3] == False:
                    tsk[0] = time.time()
                    tsk[3] = True
                elif tsk[3] == True:
                    tsk[1] = time.time()
                    tsk[2] = tsk[1] - tsk[0]



            else :
                tsk = [0,0,0,False] #reset bila terdeteksi manusia

        # showing fps
        cv2.putText(resized_img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);            cv2.putText(resized_img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2);

        # ubah durasi

        tsu[2] = tsu[2]*(fps/fps_read)
        tsk[2] = tsk[2]*(fps/fps_read)

        if status == 1:  # status unknown
            print("Waktu terdeteksi : ")
            print(tsu, '\n')
            if tsu[2] >= 10:  # durasi terdeteksi melebihi 10 detik
                print("alarm triggered!")
                playsound("Industrial Alarm.wav")
                break  # keluar program
        if status == 2:
            print("Waktu tidak terdeteksi : ")
            print(tsk, '\n')
            if tsk[2] >= 2:  # misal tidak terdeteksi (kosong) selama 5 detik
                print("Reset Status menjadi 0")
                status = 0  # ubah status jadi empty




        cv2.imshow('face recognition tutorial ',resized_img)
        print("Status : ",status)
        out.write(resized_img.astype('uint8'))
        if cv2.waitKey(1) & 0xFF == ord('q'):
        # Tekan q untuk menghentikan atau tunggu hingga akhir video
            break
    else :
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print('Waktu awal terdeteksi : ', tsu[0], '\n')
print('Waktu akhir terdeteksi : ', tsu[1], '\n')
print('Durasi terdeteksi : ', tsu[2],' detik','\n')

print('Waktu awal tidak terdeteksi : ', tsk[0], '\n')
print('Waktu akhir tidak terdeteksi : ', tsk[1], '\n')
print('Durasi tidak terdeteksi : ', tsk[2],' detik','\n')

if tsu[2] >=10:
    print ("Alarm Triggered!")
    playsound("Industrial Alarm.wav")
    print("Alarm Triggered!")
    playsound("Industrial Alarm.wav")