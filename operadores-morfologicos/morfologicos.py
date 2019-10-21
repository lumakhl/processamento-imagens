import matplotlib.pyplot as plt
import cv2 as cv2
import numpy as np


img = cv2.imread("mama6.png")
kernel = np.ones((3,3),np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

soma = cv2.add(img,tophat)
b = cv2.subtract(soma, blackhat)

c = cv2.subtract(b,img)
s, d = cv2.threshold(c,18,255,cv2.THRESH_BINARY)
cv2.imshow('img',d)
cv2.waitKey(0)

