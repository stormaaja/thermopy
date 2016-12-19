import RPi.GPIO as GPIO

class HeatingRelay:

    def __init__(self, pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin

    def clean(self):
        GPIO.cleanup()

    def set_heating(self, heating: bool):
        GPIO.output(self.pin, heating)
