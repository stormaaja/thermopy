import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest
from temp_sensor_reader import TempSensorReader

class TestTempSensorReader(unittest.TestCase):

    def setUp(self):
        self.mock_file = "/tmp/mock_temp_file"
        data = TestTempSensorReader.create_mock_data(20.812)
        TestTempSensorReader.write_file(self.mock_file, data)

    def tearDown(self):
        os.remove(self.mock_file)

    def write_file(path: str, lines: list):
        f = open(path, 'w')
        for line in lines:
            f.write(line)
            f.write("\n")
        f.close()

    def create_mock_data(temperature: float):
        return [
            "4d 01 4b 46 7f ff 0c 10 c0 : crc=c0 YES",
            "4d 01 4b 46 7f ff 0c 10 c0 t={}".format(int(temperature * 1000))
        ]

    def test_read_temperature_raw_lines(self):
        reader = TempSensorReader(self.mock_file)
        lines = reader.read_temperature_raw_lines()
        self.assertEqual("4d 01 4b 46 7f ff 0c 10 c0 : crc=c0 YES\n",
            lines[0])
        self.assertEqual("4d 01 4b 46 7f ff 0c 10 c0 t=20812\n",
            lines[1])

if __name__ == '__main__':
    unittest.main()
