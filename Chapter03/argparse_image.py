import argparse
import cv2

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("path_image", help="path to input image to be displayed")

args = parser.parse_args()

image = cv2.imread(args.path_image)

args = vars(args)

image2 = cv2.imread(args["path_image"])


cv2.imshow("loaded image", image)
#cv2.imshow("loaded image2", image2)


cv2.waitKey(0)


cv2.destroyAllWindows()