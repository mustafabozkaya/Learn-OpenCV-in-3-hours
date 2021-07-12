import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
print(img[0])
print(img[0].shape)
print(img.shape)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

imgCropped = img[0:119,350:img.shape[1],0:3]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)