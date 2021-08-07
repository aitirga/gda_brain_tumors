from pathlib import Path
from config import config
import logging
from scripts.eda import EDA

import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Read a sample data')
    data_file = Path(config.paths.data_folder) / "train/00002/T1w/Image-10.dcm"
    data = EDA.read_mri(data_file)

    plt.figure(figsize=(5, 5))
    plt.imshow(data, cmap='gray')
    plt.show()


