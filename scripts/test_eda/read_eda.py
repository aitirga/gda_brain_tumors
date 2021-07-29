from pathlib import Path
from config import config
import logging
from scripts.eda import read_xray

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Read a sample data')
    data_file = Path(config.paths.data_folder) / "/train/00000/FLAIR/Image-1.dcm"
    data = read_xray(data_file)
    print(data)


