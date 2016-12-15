from temperature_not_valid import TemperatureNotValid

class TempSensorReader:

    def __init__(self, path: str):
        self.path = path

    def read_temperature(self) -> float:
        lines = read_temperature_raw_lines()
        parse_temperature_from_lines(lines)

    def read_raw_lines(self) -> list:
        f = open(self.path, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def parse_temperature_from_lines(self, lines: list) -> float:
        if len(lines) < 2 or 'YES' not in lines[0] or 't=' not in lines[1]:
            raise TemperatureNotValid(
                "Temperature is not valid or it is not available")

        temperature_position = lines[1].find('t=')

        temperature_string = lines[1][temperature_position + 2:]
        temperature = float(temperature_string) / 1000.0
        return temperature
