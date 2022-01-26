# import modules

import cv2 as cv
from cv2 import dilate

# read and display image

img = cv.imread('opencv-course/Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

# converting to gray scale

# call cv.cvtColor pass it args and store the value in gray
# first args is the image to convert
# second args is the color code for conversion
# Display the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an image

# Use gausian blur technique
# first create a variable blur to hold the blurred img
# Use cv.GaussianBlur method that takes several args
# first args is the source image
# second arg is the ksize and has to be an odd number
# ksize determines the amount of blur
# third args is the border
# Display the image

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade

# we will be using canny edge detector
# use alot of step process computation in the background(read more on it) 
# we first call the cv.Canny() method and pass it the following args
# first we pass in the image for the function to work on
# pass in the first and the second threshholds
# store the method in a variable canny
# display the image

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# dieleting the image

# This is the proces of making the brighter parts of the edges stand out 
# making the edges on the resulting image look bigger or thicker
# this is done by using the properties of canny
# use the cv.dilate function and pass it the following args
# the image to be dilated
# the ksize
# the iterations, the number of times the dilation will occur
# store cv.dilate method iniside a variable and display it

dilated = cv.dilate(canny, (10,10), iterations= 3)
cv.imshow('Dilated', dilated)

# eroding and image

# this is the opposite of dilation
# the edges seem to thin out is like they are being swallowed by the darker parts
# We use the cv.erode method which takes in the following properties
# the image to be eroded
# the kernel size
# the iterations or number of times the erosion will happen
# store the method ina variable and print the image

eroded = cv.erode(dilated, (10,10),  iterations= 3)
cv.imshow('Eroded', eroded)

# resize image using cv.resize method

# call cv.resize method and pass it the following args
# the image to be resized
# the destination size
# there are interpolation used to maintain the aspect ratio i think
# store the method in a variable and display the image

resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping and image
# here we apply erase slicing, we are selectiong a portion of the 
# image based on their pixel values
# select image to slice and give it the coordinates to slice
# store the sliced image in a variable and display the image

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# call waitKey

cv.waitKey(0)

