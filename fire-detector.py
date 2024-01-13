
import cv2
import numpy as np
import os

cam = cv2.VideoCapture(0)
while 1:
    ret, frame = cam.read()

    frame = cv2.resize(frame, (960, 540))

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)

    no_red = cv2.countNonZero(mask)

    if int(no_red) > 1500:
        print('fire')
    else:
        print('no fire')

    cv2.imshow("output", output)
    cv2.waitKey(1)

cv2.destroyAllWindows()
cam.release()