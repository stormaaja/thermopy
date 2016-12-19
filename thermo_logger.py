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
START_TIME = time.time()
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'
RELAY_PIN = 4

temp_sensor_reader = TempSensorReader(DEVICE_FILE)

def get_running_time():
    return time.time() - START_TIME

def set_heating(enable):
    not_used_yet = enable
    return enable

def log_temperature(running_time, temperature, heating):
    f = open(LOG_FILENAME, 'a')
    f.write("{0},{1},{2}\n".format(running_time, temperature, heating))
    f.close()

def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

heating = set_heating(True)
target = temp_sensor_reader.read_temperature() + TARGET_TEMPERATURE_CHANGE

while True:
    current_temperature = read_temperature()
    current_running_time = get_running_time()

    log_temperature(get_running_time(), current_temperature, heating)
    print("\r{0:.2f}: {1:.2f} {2}"\
        .format(current_running_time, current_temperature, heating), end="")

    if heating and current_temperature >= TARGET_TEMPERATURE:
        heating = set_heating(False)
    time.sleep(1)
