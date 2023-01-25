import logging

def get_logs(level, format):
    logging.basicConfig(level=level)
    formatter = logging.Formatter(format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    return logger

# poniżej przykład
logger = get_logs(logging.DEBUG, '%(asctime)s - %(levelname)s - %(message)s')
logger.debug('Debug wiadomosci')
logger.info('Info wiadomosci')