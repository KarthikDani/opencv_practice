import cv2 as cv
import sys

img = cv.imread('saples/sample.png')

if img is None: 
    sys.exit('Couldnt read the image')

# Showing the Image
cv.imshow('Starry Night', img)
k = cv.waitKey(0)

# Saving the image
if k is ord('s'):
    cv.imwrite('StarryNight.jpg', img)