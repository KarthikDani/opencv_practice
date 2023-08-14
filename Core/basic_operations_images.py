import cv2 as cv
import numpy as np

img = cv.imread('../samples/sample.png')
assert img is not None, "file could not be read, check with os.path.exists()"

# returns rgb pixel values
px = img[100, 10]
print('RGB value: ', px)

# modifying the pixel values
img[100, 100] = [250, 0, 120]
px = img[100, 100]
print('Pixel value: ', px)

# since the above method is slow, the alternative is, numpy
img.itemset((100, 100, 0), 240)      # modifying a red value
img.item(100, 100, 0)                          # accessing a pixel value
print('Pixel value with item-set(): ', img[100, 100])

# tuple of no of rows, columns, channels
print('Shape: ', img.shape)

# no of pixels
print('Pixels in the Image: ', img.size)

# large number of errors in OpenCV-Python code are caused by invalid datatype.
print(img.dtype)

# split is costly operation in terms of time!--
b, g, r = cv.split(img)
cv.imshow('green by split method', g)

# Here's the alternative for split!
b = img[:, :, 0]
cv.imshow('Blue by slicing the array', b)
cv.waitKey(0)