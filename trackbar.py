import cv2 as cv
import numpy as np

draw_area = np.zeros([1000, 1000, 3], dtype=np.uint8)
cv.createTrackbar