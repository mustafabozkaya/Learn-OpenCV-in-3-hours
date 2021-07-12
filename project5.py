import cv2
import  numpy as np
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# print(pytesseract.image_to_string(Image.open(r"Resources/1.jpg"),lang="eng"))
# print(pytesseract.get_languages(config=''))
framewidth = 640
frameheight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, framewidth)
# cap.set(4, frameheight)
# cap.set(10,250)


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)

    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
while True:
    # success, img = cap.read()
    img = cv2.imread("Resources/book.jpg")
    #print(success, "##########")
    print(img.shape)
    img = cv2.resize(img, (framewidth, frameheight))
    cv2.imshow("Result", img)
    # Adding custom options
    gray = get_grayscale(img)
    thresh = thresholding(gray)
    openn = opening(gray)
    cannyy = canny(gray)
    custom_config = r'-l tur --psm 6'
    txt = pytesseract.image_to_string(img,lang='tur')

    with open("result.txt", mode='a') as file:
        file.write(txt)
        file.write("\n")

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



