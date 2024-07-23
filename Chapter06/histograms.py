import cv2
import numpy as np


from matplotlib import pyplot as plt
plt.subplots_adjust(hspace=0.9) 

def hist_color_img(img):
       """Calculates the histogram from a three-channel image"""
       histr = []
       histr.append(cv2.calcHist([img], [0], None, [256], [0, 256]))
       histr.append(cv2.calcHist([img], [1], None, [256], [0, 256]))
       histr.append(cv2.calcHist([img], [2], None, [256], [0, 256]))
       return histr


def plot_histogram(hist,name,pos):
    ax = plt.subplot(3, 2, pos)
    plt.plot(hist)
    plt.title(name)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    

def show_img_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 2, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')

image = cv2.imread('resources/image.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

M = np.ones(gray_image.shape, dtype="uint8") * 35
added_img = cv2.add(gray_image,M)
hist_added_img = cv2.calcHist([added_img],[0],None,[256],[0,256])




show_img_with_matplotlib(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray", 1)
plot_histogram(hist,"original",2)
show_img_with_matplotlib(cv2.cvtColor(added_img, cv2.COLOR_GRAY2BGR), "gray added", 3)
plot_histogram(hist_added_img,"added",4)
show_img_with_matplotlib(image, "color", 5)

hist_color = hist_color_img(image)

ax = plt.subplot(3, 2, 6)

plt.title('RGB Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.plot(hist_color[0], color='b', label='Blue')
plt.plot(hist_color[1], color='g', label='Green')
plt.plot(hist_color[2], color='r', label='Red')




plt.show()



