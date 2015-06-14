#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, sys.argv[1] == "1")
