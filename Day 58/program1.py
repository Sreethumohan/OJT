import cv2
import numpy as np

image = cv2.imread('hedghog.jpg')

if image is None:
    print("couldn't read the img")
    exit()

# cv2.imshow('orginal image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows

grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(grey_image,(5,5),0)

edges = cv2.Canny(blurred_image,50,150)

cv2.imshow('orginal image', image)
cv2.waitKey(0)

cv2.imshow('grayscale image', grey_image)
cv2.waitKey(0)

cv2.imshow('blurred image', blurred_image)
cv2.waitKey(0)

cv2.imshow('edge image', edges)
cv2.waitKey(0)

# cv2.imshow()
cv2.destroyAllWindows


# cv2.imshow("grayscale image:",grey_image)
# cv2.destroyAllWindows

