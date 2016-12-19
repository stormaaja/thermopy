import datetime

class CSVLogger:

    def __init__(self, file: str):
        self.file = file

    def log(self, running_time, temperature, heating):
        f = open(self.log_file, 'a')
        f.write("{0},{1},{2}\n".format(running_time, temperature, heating))
        f.close()
