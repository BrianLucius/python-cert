import logging
import random

FORMAT = '%(levelname)s - %(message)s C'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('/Users/brian/Repositories/python-cert/pcpp1_logging/battery_temperature.log', 'w')
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
handler.setLevel(level=logging.DEBUG)
logger.addHandler(handler)

for i in range(60):
    batt_temp = random.randrange(20, 41)
    if batt_temp > 35:
        logger.critical(str(batt_temp))
    elif batt_temp >= 30 and batt_temp <= 35:
        logger.warning(str(batt_temp))
    elif batt_temp <= 20:
        logger.debug(str(batt_temp))