import signal

from thermo_logger import ThermoLogger

TARGET_TEMPERATURE_CHANGE = 5
LOG_FILENAME = "{0}.csv".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'
RELAY_PIN = 4

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

thermo_logger = ThermoLogger(LOG_FILENAME)

def signal_handler(signal, frame):
    thermo_logger.clean()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

thermo_logger.set_temp_sensor_reader(DEVICE_FILE)
thermo_logger.set_target_temperature(
    thermo_logger.

thermo_logger.run()
