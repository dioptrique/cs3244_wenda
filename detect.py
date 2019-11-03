#!/usr/bin/env python

import numpy as np
import cv2
import sys

cascade = cv2.CascadeClassifier("wenda_data/cascade.xml")

image = sys.argv[1]
scale = float(sys.argv[2])
img = cv2.imread("datasets/JPEGImages/" + image + ".jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

people = cascade.detectMultiScale(gray, 1.03)
img = cv2.resize(img,None, fx = scale, fy = scale)
for (x, y, w, h) in people:
    print("Wenda")
    print(str((x, y, w, h)))
    (x, y, w, h) = (int(x*scale), int(y*scale), int(w*scale), int(h*scale))
    print(str((x, y, w, h)))
    print(str((x, y)))
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
cv2.imshow(image,img)
cv2.waitKey()

cv2.destroyAllWindows()
