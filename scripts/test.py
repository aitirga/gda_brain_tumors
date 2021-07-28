from config import config
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Test')
    print(config)