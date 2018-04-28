#!/usr/bin/env python

import RPi.GPIO as GPIO
import signal
import time
import sys

onPin = 18
on = False

def activate(signum, frame):
    global on
    if not on:
        GPIO.output(onPin, GPIO.LOW)
    else:
        GPIO.output(onPin, GPIO.HIGH)

    on = not on
    wait()


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(onPin, GPIO.OUT)
    GPIO.output(onPin, True)


def wait():
    signal.pause()


def destroy(signum, frame):
    print("Cleaning up...")
    GPIO.output(onPin, False)
    GPIO.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, activate)
    signal.signal(signal.SIGTERM, destroy)
    setup()
    wait()

