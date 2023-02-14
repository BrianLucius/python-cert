import logging

FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'

logging.basicConfig(level=logging.DEBUG, filename='/Users/brian/Repositories/python-cert/pcpp1_logging/prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')