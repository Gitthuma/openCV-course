import cv2 as cv

img = cv.imread('opencv-course/Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)
