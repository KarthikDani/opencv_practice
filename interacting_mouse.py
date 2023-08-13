import numpy as np
import cv2 as cv

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global img  # Use the global image variable
    if event == cv.EVENT_MOUSEMOVE:
        cv.circle(img, (x, y), 10, (255, 0, 0), -1)
        #cv.imshow('image', img)  # Update the image after drawing the circle

# Create a black image, a window, and bind the function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
