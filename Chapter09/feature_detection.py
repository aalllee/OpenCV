import cv2
import numpy as np

image = cv2.imread("resources/opencv_logo_with_text.png")
image_scene = cv2.imread("resources/opencv_logo_with_text_scene.png")


orb = cv2.ORB_create()
keypoints = orb.detect(image, None)
keypoints, descriptors = orb.compute(image, keypoints)

image_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(255, 0,255), flags=0)
cv2.imshow("window",image_keypoints)
cv2.waitKey(0)


keypoints_2, descriptors_2 = orb.detectAndCompute(image_scene,None)

bf_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

bf_matches = bf_matcher.match(descriptors,descriptors_2)

bf_matches = sorted(bf_matches, key=lambda x: x.distance)

result = cv2.drawMatches(image, keypoints, image_scene,keypoints_2, bf_matches[:20], None, matchColor=(255, 255, 0),singlePointColor=(255, 0, 255), flags=0)

cv2.imshow("window",result)
cv2.waitKey(0)


best_matches = bf_matches[:40]

pts_src = np.float32([keypoints[m.queryIdx].pt for m in best_matches]).reshape(-1,1,2)
pts_dst = np.float32([keypoints_2[m.trainIdx].pt for m in best_matches]).reshape(-1,1,2)

M, mask = cv2.findHomography(pts_src, pts_dst, cv2.RANSAC, 5.0)

h, w = image.shape[:2]
pts_corners_src = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
pts_corners_dst = cv2.perspectiveTransform(pts_corners_src, M)


img_obj = cv2.polylines(image_scene, [np.int32(pts_corners_dst)], True, (0,255, 255), 10)
cv2.imshow("window",img_obj)
cv2.waitKey(0)
