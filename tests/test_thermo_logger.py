import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(".."))

import unittest
from thermo_logger import ThermoLogger
from mock_temp_sensor_reader import MockTempSensorReader
from mock_csv_logger import MockCSVLogger
from thermostat import Thermostat

class TestThermoLogger(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
