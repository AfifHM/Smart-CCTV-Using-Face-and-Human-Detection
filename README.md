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

## Durasi dan Alarm
