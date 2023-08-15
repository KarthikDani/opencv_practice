#  OpenCV's addition is a saturated operation while Numpy addition is a modulo operation.
import cv2 as cv
import numpy as np

# IMAGE ADDITION
x = np.array([252], dtype=np.uint8)
y = np.array([10], dtype=np.uint8)

# cv operation is saturated, > 255, will be stopped to 255
print(cv.add(x, y))

# numpy operation is modulo, > 255, will be starting over from 0
print(x + y)

# IMAGE BLENDING
img2 = cv.imread('../samples/ikigai.png')
img1 = cv.imread('../samples/trees.jpg')

min_height = min(img1.shape[0], img2.shape[0])
min_width = min(img1.shape[1], img2.shape[1])
img1 = img1[:min_height, :min_width]
img2 = img2[:min_height, :min_width]


# Formula: g(x) = (1−α)f0(x) + αf1(x)
# same as: dst = α⋅img1 + β⋅img2 + γ
dest = cv.addWeighted(img1, 0.4, img2, 0.5, 0)
cv.imshow('Destination Image', dest)


# BITWISE OPERATIONS
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)

cv.waitKey(0)
cv.destroyAllWindows()