# Deteksi Kejadian Tak Diinginkan Menggunakan CCTV

## Overview
CCTV sering digunakan untuk mengawasi ruangan baik terbuka atau tertutup dari kejadian yang tidak diinginkan seperti pencurian atau barang tertinggal. Namun, kerap kali kejadian yang tak diinginkan tersebut hanya terekam oleh CCTV dan sulit untuk ditindak lanjut. Kami menggunakan algortima pendeteksi identitas manusia untuk memperingatkan penjaga keamanan apabila terjadi kejadian tak diinginkan yang terekam oleh CCTV.

Algoritma dibuat menggunakan python. Jadi, segala penjelasan terkait modul yang diperlukan, kode yang diupload dan hal-hal lain terkait penggunaan algoritma yang kami buat disajikan dalam format yang digunakan python.

## Dependencies
untuk dapat menjalankan seluruh algoritma yang kami buat, terdapat beberapa modul yang harus anda install terlebih dahulu, yaitu :
* OpenCV
* numpy
* imutils

## General Idea
Untuk memahami bagaimana algoritma bekerja, mari kita definisikan kejadian tak diinginkan terlebih dahulu. Kami mendefinisikan kejadian tak diinginkan sebagai adanya orang tak dikenal saja pada CCTV yang terekam selama waktu tertentu. Ada 3 poin utama, yaitu :

1. Hanya terdapat orang tak dikenal
2. Orang tak dikenal terlihat oleh CCTV
3. Orang tak dikenal terekam selama waktu tertentu

dari ketiga poin tersebut, maka kami membuat sebuah algotirma yang mampu :

1. Mengetahui identitas orang melalui wajah yang terekam
2. Mendeteksi orang tersebut
3. Menentukan apakah orang tersebut terekam selama waktu tertentu

## Detekesi Wajah Menggunakan HaarCascade

## Deteksi Manusia Menggunakan HOG-SVM
Untuk mendeteksi keberadaan manusia yang terekam kamera, kami menggunakan algoritma HOG-SVM. HOG(Histogram Oriented Gradients) merupakan fitur yang kami ekstraksi untuk membedakan mana manusia dan mana yang bukan. Jika anda tertarik lebih dalam mengenai HOG, anda dapat membacanya [di sini](https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/). Kami menggunakan fungsi bawaan dari openCV untuk mengekstraksi fitur HOG, yang kemudian diklasifikasi oleh SVM.

SVM (Support Vector Machine) merupakan salah satu metode supervised machine learning. Metode ini sering dipakai untuk klasifikasi dua jenis benda. Sehingga cocok untuk tujuan kami yaitu mendeteksi manusia yang ada di rekaman CCTV. Apabila anda tertarik lebih jauh, anda dapar mempelajarinya [di sini](https://scikit-learn.org/stable/modules/svm.html). Sama seperti HOG, kami mneggunakan fungsi yang ada dalam openCV untuk melakukan klasifikasi menggunakan SVM.

Berikut ini contoh deteksi manusia yang kami lakukan

(Insert picture here)

Anda dapat melakukan deteksi manusia saja menggunakan Human_Recog.py. Parameter-parameter yang kami gunakan bertujuan untuk mendeteksi manusia dalam ruangan. Bila anda menginginkan deteksi di tempat lain atau merasa hasilnya kurang akurat, kami sarankan anda mengubah parameter fungsi ***hog.DetectMultiscale()***. Penjelasan setiap parameter yang ada dalam fungsi tersebut dapat anda baca [di sini](https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)

Selebihnya, anda hanya tinggal me-run saja kodenya. Jangan lupa untuk mengganti nama dan directory video dengan nama dan directory video yang anda ingin gunakan.

## Durasi dan Alarm
