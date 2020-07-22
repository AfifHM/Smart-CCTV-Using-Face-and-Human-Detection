# Deteksi Kejadian Tak Diinginkan Menggunakan CCTV

## Overview
CCTV sering digunakan untuk mengawasi ruangan baik terbuka atau tertutup dari kejadian yang tidak diinginkan seperti pencurian atau barang tertinggal. Namun, kerap kali kejadian yang tak diinginkan tersebut hanya terekam oleh CCTV dan sulit untuk ditindak lanjut. Kami menggunakan algortima pendeteksi identitas manusia untuk memperingatkan penjaga keamanan apabila terjadi kejadian tak diinginkan yang terekam oleh CCTV.

Algoritma dibuat menggunakan python. Jadi, segala penjelasan terkait modul yang diperlukan, kode yang diupload dan hal-hal lain terkait penggunaan algoritma yang kami buat disajikan dalam format yang digunakan python.

## Dependencies
untuk dapat menjalankan seluruh algoritma yang kami buat, terdapat beberapa modul yang harus diinstall di python anda terlebih dahulu, yaitu :
* OpenCV
(note : Harap menginstall modul opencv-contrib-python dikarenakan modul ini memuat modul utama sekaligus modul contrib yang bakal diperlukan selama proses pengerjaan)
* numpy
* imutils
* playsound
* time

Selain itu, dalam pengerjaan dan pengetesan kami menggunakan ***PyCharm Community Version*** sebagai IDE-nya. Anda dapat mendownload PyCharm secara gratis [di sini](https://www.jetbrains.com/pycharm/). Apabila anda menggunakan IDE lain, harap diperhatikan bagaimana IDE tersebut bekerja. Karena bisa saja ada sedikit perbedaan dengan penjelasan yang kami berikan nantinya terkait menjalankan program

## General Idea
Untuk memahami bagaimana algoritma bekerja, mari kita definisikan kejadian tak diinginkan terlebih dahulu. Kami mendefinisikan kejadian tak diinginkan sebagai adanya orang tak dikenal saja pada CCTV yang terekam selama waktu tertentu. Ada 3 poin utama, yaitu :

1. Hanya terdapat orang tak dikenal
2. Orang tak dikenal terlihat oleh CCTV
3. Orang tak dikenal terekam selama waktu tertentu

dari ketiga poin tersebut, maka kami membuat sebuah algoritma yang mampu :

1. Mengetahui identitas orang melalui wajah yang terekam
2. Mendeteksi orang tersebut
3. Menentukan apakah orang tersebut terekam selama durasi waktu tertentu

## Deteksi dan pengenalan Wajah Menggunakan HaarCascade
Untuk mendeteksi wajah menggunaakan kamera, kami menggunakan algoritma Viola Jones. Prosedur deteksi wajah Viola-Jones mengklasifikasikan gambar berdasarkan pada nilai fitur sederhana. Sehingga metode algoritma Viola Jones merupakan salah satu metode deteksi wajah dengan tingkat akurasi yang tinggi dan komputasi yang cepat. Algoritma Viola Jones menggunakan fitur Haar sebagai deskriptor kemudian menggabungkan Integral Image dan AdaBoost Classifier untuk mencari dan melakukan seleksi nilai fitur dan membentuk Cascade Classifier. Classifier tersebut yang akan digunakan untuk mendeteksi wajah pada gambar. Jika tertarik untuk membaca lebih mendalam mengenai Algoritma Viola Jones dapat mengakses [di sini](https://www.superdatascience.com/blogs/opencv-face-recognition) atau untuk yang berbasis project bisa diakses [disini](https://towardsdatascience.com/the-intuition-behind-facial-detection-the-viola-jones-algorithm-29d9106b6999#:~:text=The%20Viola%2DJones%20algorithm%20first,which%20will%20be%20explained%20later.)

Untuk mendeteksi wajah, digunakan fungsi ***haarscascade.detectMultiscale*** dengan beberapa parameter yang dapat diubah apabila menginginkan hasil yang berbeda dari hasil yang kami dapatkan. Untuk memahami lebih lanjut mengenai fungsi ini bisa diakses [disini](https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html#cascadeclassifier-detectmultiscale).

Berikut ini contoh deteksi wajah manusia yang kami lakukan

<img src="Images_Hasil/FaceDetection1.png" width=500>

Untuk mengenali wajah, kami menggunakan sistem training terhadap classifier dengan menggunakan data training. Lalu hasil training akan dijadikan untuk penentu identitas wajah yang dideteksi dengan menggunakan fungsi ***faceRecognizer.predict*** yang merupakan fungsi bawaan dari openCV untuk mendeteksi kemiripan gambar dengan array input. Untuk memahami lebih dalam terkait fungsi ini bisa diakses [disini](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_api.html#facerecognizer-predict).

Berikut ini contoh pengenalan id wajah manusia yang kami lakukan

<img src="Images_Hasil/FaceRecognition2.png" width=500>

Untuk uji coba bisa dilakukan dengan melakukan run pada code yang disediakan. Harap disesuaikan beberapa nama folder, directory dan parameter sesuai yang digunakan.

## Deteksi Manusia Menggunakan HOG-SVM
Untuk mendeteksi keberadaan manusia yang terekam kamera, kami menggunakan algoritma HOG-SVM. HOG(Histogram Oriented Gradients) merupakan fitur yang kami ekstraksi untuk membedakan mana manusia dan mana yang bukan. Jika anda tertarik lebih dalam mengenai HOG, anda dapat membacanya [di sini](https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/). Kami menggunakan fungsi bawaan dari openCV untuk mengekstraksi fitur HOG, yang kemudian diklasifikasi oleh SVM.

SVM (Support Vector Machine) merupakan salah satu metode supervised machine learning. Metode ini sering dipakai untuk klasifikasi dua jenis benda. Sehingga cocok untuk tujuan kami yaitu mendeteksi manusia yang ada di rekaman CCTV. Apabila anda tertarik lebih jauh, anda dapar mempelajarinya [di sini](https://scikit-learn.org/stable/modules/svm.html). Sama seperti HOG, kami mneggunakan fungsi yang ada dalam openCV untuk melakukan klasifikasi menggunakan SVM.

Berikut ini contoh deteksi manusia yang kami lakukan

<img src="Images_Hasil/FrameOut68.jpg" width=500>
<img src="Images_Hasil/FrameOut98.jpg" width=500>

Anda dapat melakukan deteksi manusia saja menggunakan Human_Recog.py. Parameter-parameter yang kami gunakan bertujuan untuk mendeteksi manusia dalam ruangan. Bila anda menginginkan deteksi di tempat lain atau merasa hasilnya kurang akurat, kami sarankan anda mengubah parameter fungsi ***hog.DetectMultiscale()***. Penjelasan setiap parameter yang ada dalam fungsi tersebut dapat anda baca [di sini](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)

Selebihnya, anda hanya tinggal me-run saja kodenya. Jangan lupa untuk mengganti nama dan directory video dengan nama dan directory video yang anda ingin gunakan.

## Durasi dan Alarm
Untuk menentukan durasi deteksi, kami memanfaatkan fungsi ***hog.DetectMultiScale()***. Fungsi tersebut mengembalikan lokasi manusia berbentuk koordinat. Sehingga dapat dijadikan acuan apakah dalam video terdeteksi manusia atau tidak. Durasi dapat dihitung dengan menggunakan array timestamp berisi tiga nilai, waktu pertama terdeteksi, waktu terakhir terdeteksi dan status. Kira-kira array akan terlihat seperti berikut.

```
timestamp [waktu awal,waktu akhir, durasi, status]
```
varaiabel status digunakan untuk menentukan apakah deteksi awal sudah dilakukan. Pada kode yang kami buat, nilai diset False ketika deteksi pertama belum dilakukan. Sehingga timestamp waktu awal akan diupdate. Kemudian status berubah menjadi True apabila deteksi pertama sudah dilakukan. Sehingga waktu akhir bisa diambil dan durasi bisa dihitung. Apabila durasi melebihi threshold, maka alarm akan menyala menggunakan fungsi ***playsound()***. Anda bisa menggunakan suara alarm yang anda suka. Anda dapat melakukan pengetesan deteksi manusia sekaligus durasi dan alarm menggunakan HumanRecAndAlarm.py.

## Penggunaan kode program

### Face Recognition
Beberapa hal yang perlu diperhatikan sebelum menggunakan program Face Recognition adalah sebagai berikut :

#### File program
Face Recognition menggunakan 3 program Python, yaitu 
1. faceRecognition.py yang berisi kumpulan fungsi untuk pengenalan wajah diantaranya fungsi untuk training, fungsi untuk memberi kotak pada wajah dan menulis id
2. forImage.py untuk mencoba program mengenali wajah pada foto atau gambar
3. forVideo.py untuk mencoba program mengenali wajah pada video

#### Video Input
Dalam program terdapat fungsi untuk input gambar ataupun video pada line berikut
```
test_img = cv2.imread('FileName.jpg') #untuk input berupa gambar
```
dan
```
cap = cv2.VideoCapture('FileName.mp4') #untuk input berupa video
```
Anda dapat menggunakan nama file dan directory yang anda inginkan, misalnya
```
test_img=cv2.VideoCapture('D:\Test\FileName.mp4')
```
atau, anda juga dapat menggunakan stream online melalui rtsp atau sejenisnya, misalnya
```
cap = cv2.VideoCapture('rtsp://root:pass@192.168.0.91:554/axis-media/media.amp')
```
dan
```
cap = cv2.VideoCapture('https://www.dropbox.com/s/39f9fo9ch4gqoig/sample_video.mp4')
```
Namun, untuk penggunaan stream online perlu diperhatikan beberapa hal yaitu versi openCV haruslah pada versi 3.4.1. Sehingga anda perlu melalukan beberapa update terhadap openCV yang anda gunakan.

#### Fungsi .detectMultiscale dan .predict

#### Training Data untuk ID wajah

#### Cara menggunakan program

### Human Detection
Beberapa hal yang perlu diperhatikan sebelum menggunakan program human detection (Human_Recognition.py dan HumanRecAndAlarm.py) adalah sebagai berikut :

#### Video Input dan Output
dalam program yang dibuat, inisiallisasi video input terdapat pada line berikut
```
cap = cv2.VideoCapture('FileName.mp4')
```
anda dapat menggunakan nama file dan direktori yang anda inginkan, misalnya
```
cap = cv2.VideoCapture('D:\Video\FileName.mp4')
```
atau, anda juga dapat menggunakan stream online melalui rtsp atau sejenisnya, misalnya
```
cap = cv2.VideoCapture('rtsp://root:pass@192.168.0.91:554/axis-media/media.amp')
```
Namun, perlu diperhatikan bahwa penggunaan url rtsp pada openCV dapat dilakukan pada versi 3.4.1. Apabila anda tidak memilikinya, anda perlu menginstall versi terbarunya atau menggunakan cara lain yang tersebar di internet.

Untuk video output, terdapat pada line berikut
```
out = cv2.VideoWriter('outputfilename.avi',cv2.VideoWriter_fourcc(*'MJPG'),fps,(640,480))
```
Kami tidak menyarankan anda mengubah parameter tersebut, kecuali nama outputfilename. apabila anda ingin mengubahnya, tolong dicari terlebih dahulu format videowriternya. Sama seperti video input, anda dapat mengganti nama video output dengan nama dan direktori yang diinginkan serta menggunakan video stream seperti rtsp.

#### Fungsi hog.DetectMultiScale dan Bounding Box
Fungsi ***hog.DetectMultiScale*** mengembalikan lokasi manusia yang terdeteksi dalam bentuk koordinat. Dalam program, penggunaannya adalah sebagai berikut
```
(regions, _) = hog.detectMultiScale(frame, winStride=(4,4),padding=(4,4),scale=1.2)
```
Harap diingat, parameter yang digunakan dioptimalkan untuk penggunaan dalam ruangan. Apabila anda ingin menggunakannya di tempat yang berbeda, atau kurang puas dengan hasil akhir yang kami buat, anda dapat mengubah parameter sesuai yang diinginkan. Namun, jangan lupa untuk membaca arti dari parameter dalam fungsi tersebut [di sini](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)

Sebelum membuat kotak pembatas, kami menggunakan non-maximum suppression untuk menghindari overlap kotak yang memiliki objek deteksi yang sama.

<img src="https://pyimagesearch.com/wp-content/uploads/2014/10/nms_slow_01.jpg" width=500>

Gambar di atas merupakan salah satu contoh penggunaan non-maximum suppression. Implementasi dalam program adalah sebagai berikut
```
regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
pick = non_max_suppression(regions, probs=None, overlapThresh=0.65)
```
Anda dapat membaca non-maximum suppression lebih jauh [di sini](https://www.pyimagesearch.com/2014/11/17/non-maximum-suppression-object-detection-python/)
Setelah melakukan non-maximum suppression, barulah kami menggambar kotak pembatasnya. Implementasinya adalah sebagai berikut
```
 for (xA, yA, xB, yB) in pick:
      cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
```
Dua parameter terakhir merupakan warna kotak dan ketebalan garis kotak. Anda dapat menggantinya sesuka hati.
#### Durasi

#### Alarm
