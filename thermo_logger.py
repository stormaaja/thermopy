#!/bin/python
import time
import datetime
import signal
import sys
import os
import glob
import RPi.GPIO as GPIO

from temp_sensor_reader import TempSensorReader

TARGET_TEMPERATURE_CHANGE = 5
LOG_FILENAME = "{0}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'
RELAY_PIN = 4

class ThermoLogger:

    def __init__(self, log_file: str):
        self.start_time = time.time()
        self.log_file = log_file

    def set_temp_sensor_reader(self, device_file: str):
        self.temp_sensor_reader = TempSensorReader(device_file)

    def read_temperature(self) -> float:
        return self.temp_sernor_reader.read_temperature()

    def set_heating_relay(self, pin: int):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def clean(self):
        GPIO.cleanup()

    def get_running_time(self):
        return self.time.time() - self.start_time

    def set_heating(self, heating: bool):
        self.heating = heating
        return

    def log_temperature(self, running_time, temperature, heating):
        f = open(self.log_file, 'a')
        f.write("{0},{1},{2}\n".format(running_time, temperature, heating))
        f.close()

    def set_target_temperature(self, target_temperature: int):
        self.target_temperature = target_temperature

    def run(self):
        self.set_heating(True)

        while True:
            current_temperature = self.read_temperature()
            current_running_time = self.get_running_time()

            log_temperature(get_running_time(), current_temperature, heating)

            print("\r{0:.2f}: {1:.2f} {2}"\
                .format(current_running_time, current_temperature, heating), end="")

            if self.heating and current_temperature >= self.target_temperature:
                set_heating(False)
            time.sleep(1)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

thermo_logger = ThermoLogger(LOG_FILENAME)

def signal_handler(signal, frame):
    thermo_logger.clean()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

thermo_logger.set_temp_sensor_reader(DEVICE_FILE)
thermo_logger.set_target_temperature(
    thermo_logger.
thermo_logger.run()
