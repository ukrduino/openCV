# import the necessary packages

import argparse
import time

import cv2
import imutils
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream

import driver

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
				help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
				help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# allow the camera to warmup and start the FPS counter
# created a *threaded *video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
driver.init()
driver.light(True)
# driver.forward()


# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels

	# TODO Start rotation here after5 seconds

	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	# update the FPS counter
	fps.update()
# TODO stop rotation here after 2 seconds
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
driver.clean()
