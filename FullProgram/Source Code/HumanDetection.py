import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
import time

def initiate():
    #Fungsi menginisiasi persiapan descriptor dan detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    return hog

def detect(hog,frame,stride,pad,scale) :
    #Fungsi mengembalikan koordinat lokasi manusia, detectmultiscale memiliki parameter
    #sesuai masukan stride,pad,scale

    # resizing for faster detection
    #frame = cv2.resize(frame, (640, 480))
    (regions, _) = hog.detectMultiScale(frame, winStride= stride, padding= pad, scale= scale)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
    pick = non_max_suppression(regions, probs=None, overlapThresh=0.65)

    return pick

def boxes(frame,area) :
    #fungsi menggambar kotak di koordinat yang ada pada area
    for (xA, yA, xB, yB) in area:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)


#def isEmpty(frame,timestamp) :
