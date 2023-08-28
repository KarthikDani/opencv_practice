"""
# TRANSFORMATION FUNCS:
cv.warpAffine()      ->     takes 2x3 transformation matrix
cv.warpPerspective() ->     takes 3x3 transformation matrix
-----------------------------------------------------------

# SCALING
- INTERPOLATION METHODS:
Shrinking   ->  cv.INTER_CUBIC (slow)
Zooming     ->  cv.INTER_LINEAR
-----------------------------------------------------------

# ROTATION:
=> scaled rotation with adjustable center of rotation
[ α   -β   (1 - α) * center_x + β * center_y ]
[ β    α   -β * center_x + (1 - α) * center_y ]

-> where -> α=scale⋅cosθ | β=scale⋅sinθ
-----------------------------------------------------------


"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('samples/ikigai.png')
assert img is not None, 'file couldnt be read'


# Resizing
resized = cv.resize(img, None, fx=5, fy=1, interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Translation
M_T = np.float32([[1, 0, 200], [0, 1, 50]])   # 1,0,100 -> no scaling and shearing in x direction, & add 100 pixels in the x direction
                                            # 0,1,100 -> no scaling and shearing in y direction, & add 100 pixels in the y direction
translated_img = cv.warpAffine(img, M_T, (img.shape[1], img.shape[0]))
cv.imshow('Translation', translated_img)


# Rotation
M_R = cv.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 90, 1)
rotated = cv.warpAffine(img, M_R, (img.shape[1], img.shape[0]))
cv.imshow('Rotated', rotated)


# Affine Transformation
# -> To find the transformation matrix, we need three points from the input image and their corresponding locations in the output image.
                   # pt-a   # pt-b   # pt-c
pts1 = np.float32([[30,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M_affine = cv.getAffineTransform(pts1,pts2)
affined = cv.warpAffine(img,M_affine,(img.shape[1], img.shape[0]))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(affined),plt.title('Output')
plt.show()


# Perspective Transformation
ppts_1 = np.float32([[480, 225],[1500, 220],[28,387],[389,390]])
ppts_2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M_perspective = cv.getPerspectiveTransform(ppts_1,ppts_2)
perspectived = cv.warpPerspective(img, M_perspective, (300, 300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(perspectived),plt.title('Output')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()