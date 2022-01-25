import cv2 as cv

#use VideoCapture to reference the video with path and store in a variable capture
capture = cv.VideoCapture('opencv-course/Resources/Videos/dog.mp4')

#Use a while loop to read the video frame by frame
while True:
    #read video frame by frame using capture.read method
    isTrue, frame = capture.read()
    #Display each frame of the video using cv.imshow method
    cv.imshow('Video', frame)

    #The waitKey in video has to do with the speed of the vide
    #0xFF == ord('d') says if the letter d is pressed, exit the loop
    if cv.waitKey(30) & 0xFF == ord('d'):
        break

#release capture pointer
capture.release()

#Destroy all windows
cv.destroyAllWindows
