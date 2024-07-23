import cv2


gray_image = cv2.imread('resources/image.png', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=2.0)
gray_image_clahe = clahe.apply(gray_image)

cv2.imshow("window",gray_image)
cv2.waitKey(0)

cv2.imshow("window",gray_image_clahe)
cv2.waitKey(0)

def equalize_clahe_color_hsv(img):
    clahe = cv2.createCLAHE(clipLimit=4.0)
    H,S,V = cv2.split(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    eq_V = clahe.apply(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    return eq_image


image = cv2.imread('resources/image.png')
cv2.imshow("clahe hsv", equalize_clahe_color_hsv(image))
cv2.waitKey(0)