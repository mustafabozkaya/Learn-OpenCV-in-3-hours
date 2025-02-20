import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgBlur2 = cv2.GaussianBlur(imgGray,(41,41),0)
imgCanny = cv2.Canny(img,100,200)
imgCanny2 = cv2.Canny(img,300,400)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
imgDialation2 = cv2.dilate(imgCanny,kernel,iterations=3)
imgEroded2 = cv2.erode(imgDialation,kernel,iterations=3)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("rgb Image",imgrgb)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Blur2 Image",imgBlur2)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Canny2 Image",imgCanny2)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.imshow("Dialation2 Image",imgDialation2)
cv2.imshow("Eroded2 Image",imgEroded2)
cv2.waitKey(0)