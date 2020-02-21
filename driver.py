import time

import RPi.GPIO as gpio


def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.OUT)
    gpio.setup(20, gpio.OUT)
    gpio.setup(21, gpio.OUT)
    gpio.output(20, False)
    gpio.output(21, False)
    gpio.output(16, False)


def forward_for(sec: int):
    forward()
    time.sleep(sec)
    stop()


def forward():
    gpio.output(20, True)
    gpio.output(21, False)


def reverse():
    gpio.output(20, False)
    gpio.output(21, True)


def reverse(sec):
    reverse()
    time.sleep(sec)
    stop()


def light(on):
    gpio.output(16, on)


def clean():
    gpio.cleanup()


def stop():
    gpio.output(20, False)
    gpio.output(21, False)


if __name__ == '__main__':
    init()
    gpio.cleanup()
