# 1. Avoid using loops in Python as much as possible, especially double/triple loops etc. They are inherently slow.
# 2. Vectorize the algorithm/code to the maximum extent possible, because Numpy and OpenCV are optimized for vector
# operations. 3. Exploit the cache coherence. 4. Never make copies of an array unless it is necessary. Try to use
# views instead. Array copying is a costly operation. If your code is still slow after doing all of these operations,
# or if the use of large loops is inevitable, use additional libraries like Cython to make it faster.

import cv2 as cv
img1 = cv.imread('../samples/ikigai.png')

e1 = cv.getTickCount()

for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)

e2 = cv.getTickCount()

t = (e2 - e1)/cv.getTickFrequency()
print(t)

