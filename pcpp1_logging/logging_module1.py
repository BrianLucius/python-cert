import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)

hello_logger.warning('Your critical message')
hello_world_logger.warning('Your critical message')
recommended_logger.warning('Your critical message')
recommended_logger.debug('Your critical message')
logger.critical('Your critical message')
logger.error('Your error message')
logger.warning('Your warning message')
logger.info('Your info message')
logger.debug('Your debug message')