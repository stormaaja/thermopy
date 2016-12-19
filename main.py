import signal
import datetime
import glob
import os
import sys

from thermo_logger import ThermoLogger
from csv_logger import CSVLogger
from temp_sensor_reader import TempSensorReader
from heating_relay import HeatingRelay
from thermostat import Thermostat

TARGET_TEMPERATURE_CHANGE = 5
LOG_FILENAME = "{0}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'
RELAY_PIN = 4

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

heating_relay = HeatingRelay(RELAY_PIN)

def signal_handler(signal, frame):
    heating_relay.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

thermostat = Thermostat(TempSensorReader(DEVICE_FILE))
thermostat.set_target_temperature(
    thermostat.read_current_temperature() + TARGET_TEMPERATURE_CHANGE)

thermo_logger = ThermoLogger()

thermo_logger.set_csv_logger(CSVLogger(LOG_FILENAME)
thermo_logger.set_thermostat(thermostat)
thermo_logger.set_heating_relay(heating_relay)

thermo_logger.run()
