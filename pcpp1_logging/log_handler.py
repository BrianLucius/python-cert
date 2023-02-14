import logging

FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'

logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter(FORMAT)

handler = logging.FileHandler('/Users/brian/Repositories/python-cert/pcpp1_logging/prod_handler.log', 'a')
handler.setLevel(logging.CRITICAL)
handler.setFormatter(formatter)
logger.addHandler(handler)

handler_screen = logging.StreamHandler()
handler_screen.setLevel(logging.DEBUG)
handler_screen.setFormatter(formatter)
logger.addHandler(handler_screen)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')