from temp_sensor_reader import TempSensorReader

class Thermostat:

    def __init__(self, temp_sensor_reader: TempSensorReader):
        self.temp_sensor_reader = temp_sensor_reader
        self.set_target_temperature(0.0)

    def set_target_temperature(self, temperature: float):
        self.target_temperature = temperature

    def read_current_temperature(self) -> float:
        return self.temp_sensor_reader.read_temperature()

    def should_heat(self):
        return self.read_current_temperature() < self.target_temperature
