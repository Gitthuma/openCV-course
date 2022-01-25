import cv2 as cv

#read-photo.py

# read the image using cv.imread method and store it in a variable img
img = cv.imread('opencv-course/Resources/Photos/cat_large.jpg')

# Show the image using the cv.imshow method
# inside the method you pass two args 
# the name of the image and the image that was 
# read using the cv.imread method and the value stored in img
cv.imshow('Cat', img)

# show the resized image


#rescaling

# create a function for rescaling images called rreascaleframe
# Define the function with two parametres the frame and the scale
def rescaledFrame(frame, scale = 0.75):
    # frame.shape[1] is for width while frame.shape[0] is for height
    # multiply with scale so that it can scale to the value of scale provided
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    # create a variable dimensions with a tuple of height and width
    dimensions = (width, height)

    # This will return the resize of the frame with the dimensions 
    # provided using cv.resize method
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# resize the image using the rescaledFrame function and pass the variable img 
# which holds the read image
resized_image = rescaledFrame(img)

# show the resized image
cv.imshow('resized_image', resized_image)

# capture.set method
# This only works for live videos and ont work for images

# define the function and pass it width and height
def changeRes(width, height):
    # 3 & 4 references properties of this capture close 
    # the width and height of the  respectifully
    capture.set(3, width)
    capture.set(4, height)

#read-videos.py

#use VideoCapture to reference the video with path and store in a variable capture
capture = cv.VideoCapture('opencv-course/Resources/Videos/dog.mp4')

#Use a while loop to read the video frame by frame
while True:
    #read video frame by frame using capture.read method
    isTrue, frame = capture.read()

    #After reading the frame, resize it and store it in a variable
    # You do this by calling the rescaledframe function and passing 
    # it the frame that has not been rescaled
    frame_resized = rescaledFrame(frame)

    #Display each frame of the video using cv.imshow method
    cv.imshow('Video', frame)

    #You can show this rescaled frame using cv.imshow method
    #To pass it the name of the frame with the variable frame_resized
    cv.imshow('resized_video',frame_resized )

    #The waitKey in video has to do with the speed of the vide
    #0xFF == ord('d') says if the letter d is pressed, exit the loop
    if cv.waitKey(30) & 0xFF == ord('d'):
        break

#release capture pointer
capture.release()

#Destroy all windows
cv.destroyAllWindows

