import RPi.GPIO as GPIO

class HeatingRelay:

    def __init__(self, pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def clean(self):
        GPIO.cleanup()
