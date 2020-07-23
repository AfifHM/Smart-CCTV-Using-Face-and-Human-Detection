"""Program ini bertujuan mendeteksi manusia
sekaligus menghitung durasi deteksi dan
apabila durasi deteksi melebihi nilai yang ditentukan
alarm akan menyala"""

import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
import time

# Variabel timestamp
tsd=[0,0,0,False]  # untuk mendeteksi

# Inisialisasi deteksi manusia dengan HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Video input (anda dapat menggunakan stream video online
# dengan menggunakan rtsp dan sejenisnya
filename = 'coba5'
cap = cv2.VideoCapture(filename + '.mp4')

# Mengecek fps video input dan insialisasi output video
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
out = cv2.VideoWriter(
    'output ' + filename + '.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    fps,
    (640, 480))


# Memulai mengolah video
while (cap.isOpened()): #selama video masih ada, akan selalu true
    timer = cv2.getTickCount()
    # Membaca stream
    ret, frame = cap.read()
    if ret:
        # Resizing untuk meningkatkan kecepatan pemrosesan
        frame = cv2.resize(frame, (640, 480))

        # Mendeteksi daerah yang terindikasi ada manusianya
        # dan mengembalikan dalam bentuk koordinat
        (regions, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.2)

        # Menggunakan non_max_suppression untuk menghindari
        # kotak yang overlap padahal masih 1 objek yang sama
        regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
        pick = non_max_suppression(regions, probs=None, overlapThresh=0.65)

        # menggambar kotak untuk koordinat yang diberikan
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

        # Pengambilan data timestamp dan durasi
        if len(regions) == 0:
            print('Human Not Detected')


        else:
            print('Human Detected')
            if tsd[3] == False:
                # Pertama kali deteksi, waktu awal diambil
                tsd[0] = time.time()
                tsd[3] = True
            elif tsd[3] == True:
                # Sudah pernah deteksi, waktu akhir diambil
                tsd[1] = time.time()
            tsd[2] = tsd[1] - tsd[0]
            print("Waktu terdeteksi : ")
            print(tsd, '\n')


        # Menyalakan Alarm bila durasi deteksi melebihi threshold
        if (tsd[2] >= 10):
            print("Alarm Triggerred!!!")
            playsound("Industrial Alarm.wav")
            break

        # Output Video

        out.write(frame.astype('uint8'))
        cv2.imshow("After NMS", frame)
        # Keluar dari program dengan menekan tombol 'q' di keybpard
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Apabila video habis, keluar program
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print('Waktu awal terdeteksi : ', tsd[0], '\n')
print('Waktu akhir terdeteksi : ', tsd[1], '\n')
print('Durasi terdeteksi : ', (tsd[1] - tsd[0]), ' detik', '\n')
