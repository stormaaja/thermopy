#!/bin/python
import time
import datetime
import signal
import sys
import os
import glob

from temp_sensor_reader import TempSensorReader
from heating_relay import HeatingRelay

class ThermoLogger:

    def __init__(self, log_file: str):
        self.start_time = time.time()
        self.log_file = log_file

    def set_temp_sensor_reader(self, device_file: str):
        self.temp_sensor_reader = TempSensorReader(device_file)

    def read_temperature(self) -> float:
        return self.temp_sernor_reader.read_temperature()

    def set_heating_relay(self, pin: int):
        self.heating_relay = HeatingRelay(pin)

    def clean(self):
        self.heating_relay.cleanup()

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
