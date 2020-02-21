import time

import cv2
import imutils
import numpy as np
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream

import driver

driver.init()
driver.light(True)
driver.forward()

cap = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
# current contour
(xg, yg, wg, hg) = (0, 0, 0, 0)
# previous contour
(xg1, yg1, wg1, hg1) = (0, 0, 0, 0)
frame = cap.read()
# centre of contour coordinates
points = []
while fps._numFrames < 500:
    frame = cap.read()
    # TODO define best size
    frame = imutils.resize(frame, width=400)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of desired color in HSV
    lower_color_range = np.array([155, 80, 142])
    upper_color_range = np.array([171, 225, 212])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color_range, upper_color_range)
    # TODO try different contour detectors
    found_contourse = cv2.findContours(mask.copy(),
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(found_contourse) > 0:
        color_contour_area = max(found_contourse, key=cv2.contourArea)
        (xg, yg, wg, hg) = cv2.boundingRect(color_contour_area)
        if (xg1, yg1, wg1, hg1) != (xg, yg, wg, hg):
            # cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)
            (xg1, yg1, wg1, hg1) = (xg, yg, wg, hg)
            cX = int(xg + wg / 2)
            cY = int(yg + hg / 2)
            print((xg, yg, wg, hg), cX, cY)
            points.append((cX, cY))
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    #
    # k = cv2.waitKey(5)
    # if k == 27:
    #     break
    fps.update()
# draw marker path
for point in points:
    cv2.circle(frame, point, 1, (0, 255, 255), -1)
cv2.imwrite('marker_path.jpg', frame)

driver.clean()
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cap.stop()
cv2.destroyAllWindows()
