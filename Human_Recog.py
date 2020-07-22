import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
import time



# Inisialisasi deteksi manusia dengan HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Video input (anda dapat menggunakan stream video online
# dengan menggunakan rtsp dan sejenisnya
filename = 'coba5'
cap = cv2.VideoCapture(filename+'.mp4')

#Mengecek fps video input dan insialisasi output video
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
out = cv2.VideoWriter(
    'output '+ filename +'.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    fps,
    (640,480))

#Memulai mengolah video
while(cap.isOpened()) :
    timer = cv2.getTickCount()
    # Membaca stream
    ret, frame = cap.read()
    if ret :
        # Resizing untuk meningkatkan kecepatan pemrosesan
        frame = cv2.resize(frame, (640, 480))


        # Mendeteksi daerah yang terindikasi ada manusianya
        # dan mengembalikan dalam bentuk koordinat
        (regions, _) = hog.detectMultiScale(frame, winStride=(4,4),padding=(4,4),scale=1.2)


        # Menggunakan non_max_suppression untuk menghindari
        # kotak yang overlap padahal masih 1 objek yang sama
        regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
        pick = non_max_suppression(regions, probs=None, overlapThresh=0.65)

        # menggambar kotak untuk koordinat yang diberikan
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)


        # Output Video

        out.write(frame.astype('uint8'))
        cv2.imshow("After NMS",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else :
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print('Waktu awal terdeteksi : ', tsd[0], '\n')
print('Waktu akhir terdeteksi : ', tsd[1], '\n')
print('Durasi terdeteksi : ', (tsd[1] - tsd[0]),' detik','\n')