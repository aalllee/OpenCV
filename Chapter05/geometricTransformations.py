import cv2
import numpy as np
image = cv2.imread("resources/logo.png")


"""
SCALE
"""
w = 300
h = 300

resized_image = cv2.resize(image,(w,h),interpolation=cv2.INTER_LINEAR)

cv2.imshow('Image mouse', image)
cv2.waitKey(0)

cv2.imshow('Image mouse', resized_image)
cv2.waitKey(0)


"""
TRANSLATE
"""
tx = 50
ty = 100
M = np.float32([[1, 0, tx], [0, 1, ty]])

height, width = image.shape[:2]
dst_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow('Image mouse', dst_image)
cv2.waitKey(0)



height, width = image.shape[:2]
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 1)
dst_image = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image mouse', dst_image)
cv2.waitKey(0)


"""
Affine Transform
"""
pts_1 = np.float32([[0, 0], [50, 100], [100, 0]])
pts_2 = np.float32([[100, 100], [50, 0], [0, 100]])
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow('Image mouse', dst_image)
cv2.waitKey(0)


"""
Perspective Transform

"""

pts_1 = np.float32([[0, 0], [100, 0], [0, 100], [100, 100]])
pts_2 = np.float32([[25, 0], [75, 0], [25, 300], [75, 300]])
M = cv2.getPerspectiveTransform(pts_1, pts_2)
dst_image = cv2.warpPerspective(image, M, (300, 300))

cv2.imshow('Image mouse', dst_image)
cv2.waitKey(0)

"""
Crop Image
"""
dst_image = image[80:200, 230:330]

"""
Applying Kernels
"""
kernel_averaging_5_5 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04], [0.04,
   0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04],[0.04, 0.04, 0.04,
   0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04]])

kernel_averaging_10_10 = np.ones((10, 10), np.float32) / 100

smooth_image_f2D = cv2.filter2D(image, -1, kernel_averaging_5_5)
smooth_image_f2D_10_10 = cv2.filter2D(image, -1, kernel_averaging_10_10)
smooth_image_b = cv2.blur(image, (10, 10))
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)


cv2.imshow('Image mouse', smooth_image_f2D)
cv2.waitKey(0)
cv2.imshow('Image mouse', smooth_image_f2D_10_10 )
cv2.waitKey(0)
cv2.imshow('Image mouse', smooth_image_b)
cv2.waitKey(0)

