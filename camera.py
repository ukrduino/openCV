from time import sleep

from picamera import PiCamera


def capture_image(path):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture(path)  # '/home/pi/open_cv/image.jpg'
    camera.stop_preview()
