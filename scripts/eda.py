'''
This script contains various useful methods to carry out Exploratory Data Analysis (EDA)
The dicom reading method has been taken from 'https://www.kaggle.com/raddar/convert-dicom-to-np-array-the-correct-way'
'''
import pathlib

import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pathlib import Path
import matplotlib.pyplot as plt
import imageio
import natsort
import logging

logger = logging.getLogger(__file__)

def read_mri(path, voi_lut=True, fix_monochrome=True):
    dicom = pydicom.read_file(path)

    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array

    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data

    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)
    return data


def find_images_for_case(path) -> dict:
    """This method finds and orders the images corresponding to a given case
    Args:
        path: path of the case

    Returns:
        A dictionary containing the image paths
    """
    case_path = Path(path)
    case_dict = {}
    case_dict['flair'] = natsort.natsorted(list(Path(case_path / "FLAIR").glob('*.dcm')),
                                           key=lambda x: str(x))
    case_dict['t1w'] = natsort.natsorted(list(Path(case_path / "T1w").glob('*.dcm')),
                                         key=lambda x: str(x))
    case_dict['t1wce'] = natsort.natsorted(list(Path(case_path / "T1wCE").glob('*.dcm')), key=lambda x: str(x))
    case_dict['t2w'] = natsort.natsorted(list(Path(case_path / "T2w").glob('*.dcm')), key=lambda x: str(x))

    return case_dict


def make_gif(path: pathlib.Path, set='flair'):
    case_dict = find_images_for_case(path)
    images = []
    for filename in case_dict[set]:
        images.append(read_mri(filename))
    output_name = f"{path.stem}-{set}.gif"
    imageio.mimsave(output_name, images)


