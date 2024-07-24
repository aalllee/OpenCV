import cv2
import numpy as np
def build_sample_image_2():
    """Builds a sample image with basic shapes"""
    # Create a 500x500 gray image (70 intensity) with a rectangle and a
    #circle inside (with internal contours):
    img = np.ones((500, 500, 3), dtype="uint8") * 70
    cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 255), -1)
    cv2.rectangle(img, (150, 150), (250, 250), (70, 70, 70), -1)
    cv2.circle(img, (400, 400), 100, (255, 255, 0), -1)
    cv2.circle(img, (400, 400), 50, (70, 70, 70), -1)
    return img

img = build_sample_image_2()

cv2.imshow("window",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY )

cv2.imshow("window",binary_image)
cv2.waitKey(0)

contours, hierarchy= cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)


image_with_contours = img.copy()
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
cv2.imshow("window",image_with_contours)
cv2.waitKey(0)


"""
MOMENTS
"""
M = cv2.moments(contours[0])
print("Contour area: '{}'".format(cv2.contourArea(contours[0])))
print("Contour area: '{}'".format(M['m00']))

print("center X : '{}'".format(round(M['m10'] / M['m00'])))
print("center Y : '{}'".format(round(M['m01'] / M['m00'])))

def roundness(contour, moments):
       """Calculates the roundness of a contour"""
       length = cv2.arcLength(contour, True)
       k = (length * length) / (moments['m00'] * 4 * np.pi)
       return k

def eccentricity_from_ellipse(contour):
       """Calculates the eccentricity fitting an ellipse from a contour"""
       (x, y), (MA, ma), angle = cv2.fitEllipse(contour)
       a = ma / 2
       b = MA / 2
       ecc = np.sqrt(a ** 2 - b ** 2) / a
       return ecc



