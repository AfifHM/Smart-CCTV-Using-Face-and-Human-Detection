import cv2
import os
import numpy as np

#Modul yang mengandung segala fungsi yang akan digunakan untuk mendeteksi dan mengenali wajah di gambar atau video


#Fungsi untuk mendeteksi wajah pada gambar skala abu-abu dan memberi kotak pada pixel yang teridentifikasi sebagai wajah
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#Konversi gambar berwarna ke gray-scale
    face_haar_cascade=cv2.CascadeClassifier(r'D:\Data Pribadi\Akademik\Kuliah\Semester 7\Kerja Praktek\FaceRecognition-master\HaarCascade\haarcascade_frontalface_default.xml')#Load haar classifier
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.35,minNeighbors=5)#Deteksi wajah pada gambar dan memberi kotak pada pixel yang teridentifikasi

    return faces,gray_img

#Fungsi untuk membaca file training dalam folder untuk melatih sistem memberi sebuah ID
def labels_for_training_data(directory):
    faces=[]
    faceID=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")#Skip file yang dimulai dengan . (Sekaligus tanda pergantian folder ID)
                continue

            id=os.path.basename(path)#Mengambil nama directory/folder
            img_path=os.path.join(path,filename)#Mengambil alamat gambar
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path)#load gambar satu per satu
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)#Memanggil fungsi face Detection agar dapat hasil hanya dibagian wajah yang masuk ke data
            if len(faces_rect)!=1:
               continue #Diasumsikan bahwa tiap gambar training hanya ada 1 orang, jadi tidak perlu ada fungsi tambahan dan bisa dilanjutkan ke tahap berikutnya
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]#Crop bagian gambar yang menunjukkan gambar untuk masuk ke data
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID


#Fungsi untuk melatih classifier haar dan mengambil wajah
def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

#Fungsi untuk menggambar kotak penunjuk wajah
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,0,255),thickness=4)

#Fungsi untuk menuliskan ID
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
