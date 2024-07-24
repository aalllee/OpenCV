import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resources/image.png",cv2.IMREAD_GRAYSCALE)

ret, thresh1  = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)

cv2.imshow("window",thresh1)
cv2.waitKey(0)

"""
THRESHOLD TYPES
        cv2.THRESH_BINARY
        cv2.THRESH_BINARY_INV
        cv2.THRESH_TRUNC
        cv2.THRESH_TOZERO
        cv2.THRESH_TOZERO_INV
        cv2.THRESH_OTSU
        cv2.THRESH_TRIANGLE
"""

img = cv2.bilateralFilter(img, 15, 25, 25)

adaptive_thresh_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                             cv2.THRESH_BINARY, 11, 2)

adaptive_thresh_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                 cv2.THRESH_BINARY, 11, 2)


plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Adaptive Mean Thresholding')
plt.imshow(adaptive_thresh_mean, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Adaptive Gaussian Thresholding')
plt.imshow(adaptive_thresh_gaussian, cmap='gray')
plt.axis('off')

plt.show()