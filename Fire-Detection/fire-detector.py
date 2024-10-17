
import cv2
import numpy as np
import serial
import time
import sys

message = "no fire"
cam = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.write(b"0!\n")
time.sleep(1)
print(message)

for i in range(1000):
    ret, frame = cam.read()

    if not ret:
        print('Image not found')
        exit()

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

    if int(no_red) > 10000:
        if message != "fire":
            message = "fire"
            ser.write(b"1\n")
            time.sleep(1)
            print(message)
            sys.stdout.flush()
    else:
        if message != "no fire":  
            message = "no fire"
            ser.write(b"0!\n")
            time.sleep(1)
            print(message)
            sys.stdout.flush()

    cv2.imshow("output", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()