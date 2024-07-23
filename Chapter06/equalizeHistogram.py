import cv2
import matplotlib.pyplot as plt

"""
GRAY SCALE EQ
"""

image = cv2.imread('resources/image.png', cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

hist_orig = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')

plt.subplot(2, 2, 3)
plt.title('Histogram of Original Image')
plt.plot(hist_orig)
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.title('Histogram of Equalized Image')
plt.plot(hist_eq)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()


"""
COLOR IMAGE EQ
"""

image = cv2.imread('resources/image.png')

ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

equalized_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))

plt.show()
