######################### READ IMAGE ############################
#import cv2
## LOAD AN IMAGE USING 'IMREAD'
#img = cv2.imread("Resources/lena.png")
#print('Original Dimensions : ',img.shape)
## DISPLAY
#cv2.imshow("Lena Soderberg",img)
#cv2.waitKey(0)

######################### READ VIDEO #############################
#import cv2
#frameWidth = 640
#frameHeight = 480
#cap = cv2.VideoCapture("Resources/test_video.mp4")
#print(f"cap---={0}",cap)
#
#while True:
#    success, img = cap.read()
#    print(success,"##########")
#    print(img.shape)
#    img = cv2.resize(img, (frameWidth, frameHeight))
#    cv2.imshow("Result", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
######################### READ WEBCAM  ############################
import cv2
framewidth = 1040
frameheight = 980
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10,250)
while True:
    success, img = cap.read()
    print(success,"##########")
    print(img.shape)
    img = cv2.resize(img, (framewidth, frameheight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

if __name__ == '__main__':
    True