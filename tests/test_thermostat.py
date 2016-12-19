import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(".."))

import unittest
from thermo_logger import ThermoLogger
from mock_temp_sensor_reader import MockTempSensorReader
from mock_csv_logger import MockCSVLogger
from thermostat import Thermostat

class TestThermostat(unittest.TestCase):

    def test_should_heat(self):
        mock_temp_sensor_reader = MockTempSensorReader("")
        mock_temp_sensor_reader.set_temperature(10.0)
        thermostat = Thermostat(mock_temp_sensor_reader)

        thermostat.set_target_temperature(20.0)

        self.assertTrue(thermostat.should_heat())

        mock_temp_sensor_reader.set_temperature(25.0)
        self.assertFalse(thermostat.should_heat())

if __name__ == '__main__':
    unittest.main()
