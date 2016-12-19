import RPi.GPIO as GPIO

class HeatingRelay(Relay):

    def __init__(self, pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.set_heating(False)

    def cleanup(self):
        GPIO.cleanup()

    def set_heating(self, heating: bool):
        self.heating = heating
        GPIO.output(self.pin, heating)

    def is_heating(self) -> bool:
        return self.heating
