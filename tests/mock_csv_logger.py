from csv_logger import CSVLogger

class MockCSVLogger(CSVLogger):

    def __init__(self, file: str):
        self.file = file

    def log(self, running_time, temperature, heating):
        ""
