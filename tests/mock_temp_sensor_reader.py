from temp_sensor_reader import TempSensorReader

class MockTempSensorReader(TempSensorReader):

    def __init__(self, path: str):
        self.path = path
        self.set_temperature(0.0)

    def read_temperature(self) -> float:
        return self.temperature

    def set_temperature(self, temperature: float):
        self.temperature = temperature
