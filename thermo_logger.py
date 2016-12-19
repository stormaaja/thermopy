#!/bin/python
import time
import datetime
import sys
import os
import glob

from csv_logger import CSVLogger
from thermostat import Thermostat

class ThermoLogger:

    def __init__(self):
        self.start_time = time.time()

    def set_csv_logger(self, csv_logger: CSVLogger):
        self.csv_logger = csv_logger

    def set_thermostat(self, thermostat: Thermostat):
        self.thermostat = thermostat

    def set_heating_relay(self, pin: int):
        self.heating_relay = HeatingRelay(pin)

    def get_running_time(self):
        return self.time.time() - self.start_time

    def set_heating(self, heating: bool):
        self.heating_relay.set_heating(heating)

    def set_target_temperature(self, target_temperature: int):
        self.target_temperature = target_temperature

    def run(self):
        self.set_heating(True)

        while True:
            current_temperature = self.thermostat.read_current_temperature()
            current_running_time = self.get_running_time()

            self.csv_logger.log(
                get_running_time(), current_temperature,
                self.heating_relay.is_heating())

            print("\r{0:.2f}: {1:.2f} {2}"\
                    .format(current_running_time, current_temperature, heating),
                end="")

            if self.heating and not self.thermostat.should_heat():
                self.set_heating(False)

            time.sleep(1)
