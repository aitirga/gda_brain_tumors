from pathlib import Path
from config import config
import logging
from scripts.eda import EDA

import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Read a sample data')
    data_file = Path(config.paths.data_folder) / "train/00009/"
    # image_dict = find_images_for_case(data_file)
    EDA.make_gif(data_file)



