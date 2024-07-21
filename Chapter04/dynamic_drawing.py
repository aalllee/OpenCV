"""
Drawing circles on mouse click
"""

import cv2

image = cv2.imread("resources/logo.png")

def draw_circle(event, x, y, flags, param):
       if event == cv2.EVENT_LBUTTONDBLCLK:
           print("event: EVENT_LBUTTONDBLCLK")
       if event == cv2.EVENT_MOUSEMOVE:
           print("event: EVENT_MOUSEMOVE")
       if event == cv2.EVENT_LBUTTONUP:
           print("event: EVENT_LBUTTONUP")
       if event == cv2.EVENT_LBUTTONDOWN:
           print("event: EVENT_LBUTTONDOWN")
           cv2.circle(image, (x, y), 10, (0,255,0), -1)


cv2.namedWindow('Image mouse')
cv2.setMouseCallback('Image mouse',draw_circle)


while True:
    cv2.imshow('Image mouse', image)

    if cv2.waitKey(400) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()