# import modules

from tokenize import blank_re
import cv2 as cv
from cv2 import waitKey
import numpy as np

# creating a blank image to work with

# use the np.zeros method and pass it two args
# first args is the dimensions of the image i.e width and height
# second args is the data type in this case 'uint8' 
# which is the datatype of animage
# also give it a shape of 3 which is the number of color channels

blank = np.zeros((500,500,3), dtype= 'uint8')

# show the blank image

cv.imshow('Blank', blank)


# paint the image a certain color

# paint image blue
# call blank and reference all the pixels
# assign the color to all pixels
# then display the image using the cv.imshow methos

blank[:] = 255, 0, 0
cv.imshow('Blue', blank)

# paint a certain portion of the image

# This is done by giving the image a range of pixels
# Then display the image using cv.imshow method

blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Paint portion', blank)

# draw a rectangle using the cv.reactangle method

# cv.rectangle method takes in five args
# the first is the image to draw over in our case blank
# second args is pt1 which is the origin in our case (0,0)
# third args is pt2 which is the end point in our case (250,250)
# fourth args is the colour in our case (0, 255, 0) or green
# the fifth args is the thickness in our case 2 this will give an outline
# if you want to fill the reactangle change thicknes to cv.FILLED or -1
# instead of using value for dimension we can use .shape method
# lastly show the image using cv.imshow method


cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]), (0,255,0), thickness= -1)
cv.imshow('rectangle', blank)

# draw a circle using cv.circle method

# cv.circle method takes the following args
# first argument is the image to draw over in our case blank
# second args is the centre of the circle in our case (250,250) the midpoint of our image
# third argument is the radius of the circle in our case 40 pixels
# fourth args is the color in our case (0,0,255) or red
# fifth args id the thicknes in our case -1 for a fill
# lastly display the image using the cv.imshow method

cv.circle(blank, (250,250), 40, (0,0,255), thickness= -1)
cv.imshow('circle', blank)

# draw a stand alone line using the cv.line method

# cv.line method takes in the following args
# first the image to draw the line on in our case blank
# second is the starting poit of the line
# third is the ending point of the line
# fourth is the color
# fifth is the thickness
#lastly display the image

cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# write tex on an image using cv.putText method

# cv.putText method takes the following args
# first the image to write text on
# second the text we want to write
# third the origin which is where we want the text to start
# fourth is the font for the text
# fifth is the scale of the font
# Sixt is the color
# seventh is the thickness
# lastly display the text


cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)

# Add the wait key

cv.waitKey(0)