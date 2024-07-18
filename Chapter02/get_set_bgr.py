import cv2

img = cv2.imread('resources/logo.png')

dimensions = img.shape

print("image dimensions: ", dimensions)

(h, w, c) = img.shape

print("Dimensions of the image - Height: {}, Width: {}, Channels: {}".format(h, w, c))

# Get the value of the pixel (x=40, y=6):
(b, g, r) = img[6, 40]

# Set the pixel to red ((b - g - r) format):
img[6, 40] = (0, 0, 255)

top_left_corner = img[0:50, 0:50]

# We show this ROI:
cv2.imshow("top left corner original", top_left_corner)

# Wait indefinitely for a key stroke (in order to see the created window):
cv2.waitKey(0)

img[20:70, 20:70] = top_left_corner

# We show the modified image:
cv2.imshow("modified image", img)

# Wait indefinitely for a key stroke (in order to see the created window):
cv2.waitKey(0)

# Set top left corner of the image to blue
img[0:50, 0:50] = (255, 0, 0)

# Show modified image;
cv2.imshow("modified image", img)

# Wait indefinitely for a key stroke (in order to see the created windows):
cv2.waitKey(0)

gray_img = cv2.imread('resources/logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("gray image",gray_img)

cv2.waitKey(0)
