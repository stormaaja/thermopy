import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(".."))

import unittest
from thermo_logger import ThermoLogger
from mock_temp_sensor_reader import MockTempSensorReader
from mock_csv_logger import MockCSVLogger

class TestThermoLogger(unittest.TestCase):

    def test_should_heat(self):
        mock_temp_sensor_reader = MockTempSensorReader("")
        mock_temp_sensor_reader.set_temperature(10.0)

        thermo_logger = ThermoLogger()
        thermo_logger.set_csv_logger(MockCSVLogger(""))

        thermo_logger.set_target_temperature(20.0)

        thermo_logger.set_temp_sensor_reader(mock_temp_sensor_reader)
        self.assertTrue(thermo_logger.should_heat())

        mock_temp_sensor_reader.set_temperature(25.0)
        self.assertFalse(thermo_logger.should_heat())

if __name__ == '__main__':
    unittest.main()
