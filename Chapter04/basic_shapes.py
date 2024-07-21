import cv2
import numpy as np

image = np.zeros((400,400,3),dtype="uint8")


image[:] = (200,200,200)

#img = line(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
cv2.line(image, (0,0),(400,400),(0,255,0),3)


#img = rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
cv2.rectangle(image, (0,100),(200,200),(255,0,0),-1)

#img = circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
#cv.arrowedLine(img, pt1, pt2, color, thickness=1, lineType=8, shift=0,tipLength=0.1)


# These points define a triangle
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes: this line is not necessary, only for visualization
print("shape of pts '{}'".format(pts.shape))
# Draw this poligon with True option
cv2.polylines(image, [pts], True, (0,0,255), 3)


def draw_float_circle(img, center, radius, color, thickness=1, lineType=8,
   shift=4):
       """Wrapper function to draw float-coordinate circles
       """
       factor = 2 ** shift
       center = (int(round(center[0] * factor)), int(round(center[1] *
   factor)))
       radius = int(round(radius * factor))
       cv2.circle(img, center, radius, color, thickness, lineType, shift)

draw_float_circle(image, (299.5, 299.5), 100, (255,255,0), 4, 8, 0)

cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2, cv2.LINE_4)

cv2.imshow('line image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()