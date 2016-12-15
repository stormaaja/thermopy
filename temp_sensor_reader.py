from array import array

class TempSensorReader:

    def __init__(self, path: str):
        self.path = path

    def get_temperature(self) -> float:
        return 0.0

    def read_temperature_raw_lines(self) -> array:
        f = open(self.path, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp_from_lines(self, lines: array) -> float:
        lines = read_temperature_raw_lines()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temperature_raw_lines()
        equals_pos = lines[1].find('t=')

        if equals_pos == -1: raise RuntimeError("No data available")

        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
