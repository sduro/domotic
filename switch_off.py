from time import sleep
import RPi.GPIO as GPIO
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, False)
