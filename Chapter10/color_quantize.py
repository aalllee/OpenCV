import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('resources/image.png')


def color_quantize(image, k):
    data = np.float32(image).reshape((-1,3))
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)

    ret, label, center = cv2.kmeans(data, k , None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


img_quant = color_quantize(img,5)

cv2.imshow("window",img_quant)
cv2.waitKey(0)