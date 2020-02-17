#!/bin/bash
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 "$1" "$2" "$3"