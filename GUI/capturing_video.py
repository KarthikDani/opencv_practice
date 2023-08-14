import cv2 as cv

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print('Camera cannot be opened..')
    exit()

while True:
    ret, frame = capture.read()

    if not ret:
        print('Frames are not being received, is streaming ended?..')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Frames', gray)

    if(cv.waitKey(1) is ord('q')):
        break

capture.release()
cv.destroyAllWindows()