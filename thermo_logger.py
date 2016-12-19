#!/bin/python
import time

from csv_logger import CSVLogger
from thermostat import Thermostat
from relay import Relay

class ThermoLogger:

    def __init__(self):
        self.start_time = time.time()

    def set_csv_logger(self, csv_logger: CSVLogger):
        self.csv_logger = csv_logger

    def set_thermostat(self, thermostat: Thermostat):
        self.thermostat = thermostat

    def set_heating_relay(self, heating_relay: Relay):
        self.heating_relay = heating_relay

    def get_running_time(self):
        return time.time() - self.start_time

    def run(self):
        self.heating_relay.set_state(True)

        while True:
            current_temperature = self.thermostat.read_current_temperature()
            current_running_time = self.get_running_time()

            self.csv_logger.log(
                get_running_time(), current_temperature,
                self.heating_relay.is_heating())

            print("\r{0:.2f}: {1:.2f} {2}"\
                    .format(current_running_time, current_temperature, heating),
                end="")

            if self.heating_relay.get_state() and \
                    not self.thermostat.should_heat():
                self.heating_relay.set_state(False)

            time.sleep(1)
