import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_read_and_resize(imageFromDB):
    img = cv2.imread(imageFromDB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h,w,c = img.shape

    if w > 1000:
        new_w = 1000
        ar = w/h
        new_h = int(new_w/ar)

        img = cv2.resize(img, (new_w,new_h), interpolation= cv2.INTER_AREA)
    con = image_dialation(img)
    segmentation(con,img)

def thresholding(image):
  img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  ret, threshold = cv2.threshold(img_grey,80,255,cv2.THRESH_BINARY_INV)
  return threshold

def image_dialation(img):
    thresh_img = thresholding(img)

    kernal = np.ones((3,85),np.uint8)
    dialation = cv2.dilate(thresh_img,kernal,iterations=1)

    (contours, heirarchy) = cv2.findContours(dialation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def segmentation(contours,img):
    boxes = []
    boxes_img = img.copy()
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        cv2.rectangle(boxes_img, (x,y), (x+w, y+h), (40,100,250), 2)
        boxes.append((x,y,w,h))

    for j in range(len(boxes)):
        (x,y,w,h) = boxes[j]
        crop = img[y-10:y+h+10, x-10:x+w+10]
        cv2.imwrite(f'S_{j}.jpg', crop)