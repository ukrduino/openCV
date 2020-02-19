#!/bin/bash
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 opencv_object_tracking.py --video dashcam_boston.mp4 --tracker csrt
