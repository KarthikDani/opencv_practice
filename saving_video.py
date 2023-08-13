import cv2 as cv

capture = cv.VideoCapture(0)

# Defining codec, create VideoWriter object
# NOT Working on Mac for some reason..
fourcc = cv.VideoWriter_fourcc(*'DIVX')
output = cv.VideoWriter('MyVideo.avi', fourcc, 20.0, (640, 480))

if not capture.isOpened():
    print('Capture object is not initialised or Its the end of the video..')
    exit()

while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        print('Frames are not being received..')
        break

    frame = cv.flip(frame, 1)

    output.write(frame)

    cv.imshow('Frames', frame)
    if cv.waitKey(1) is ord('q'):
        break

capture.release()
output.release()
cv.destroyAllWindows()