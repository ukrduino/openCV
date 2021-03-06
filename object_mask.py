import time

import cv2
import numpy as np
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream

import driver


def nothing(x):
    pass


driver.init()
driver.light(True)
driver.forward()

cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

cap = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
while fps._numFrames < 1000:
    # frame = cv2.imread('smarties.png')
    frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # l_b = np.array([l_h, l_s, l_v])
    # u_b = np.array([u_h, u_s, u_v])

    l_b = np.array([155, 80, 142])
    u_b = np.array([171, 225, 212])

    mask = cv2.inRange(hsv, l_b, u_b)

    countures = cv2.findContours(mask.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
    print(countures)
    # if len(countures) > 0:
    #     blue_area = max(countures, key=cv2.contourArea)
    #     (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
    #     cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)

    # res = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    # cv2.imshow("res", res)
    fps.update()
    # https://answers.opencv.org/question/204175/how-to-get-boundry-and-center-information-of-a-mask/
    key = cv2.waitKey(1)
    if key == 27:
        break
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cap.release()
cv2.destroyAllWindows()
driver.clean()
