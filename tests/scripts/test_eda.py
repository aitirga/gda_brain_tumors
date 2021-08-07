import unittest
# from config import config
from scripts.eda import EDA


class EDACase(unittest.TestCase):
    def setUp(self) -> None:
        self.eda = EDA('../../data/rsna-miccai-brain-tumor-radiogenomic-classification')

    def test_find_training_directories(self):
        test_paths = self.eda.get_training_mri_paths()
        self.assertEqual(len(test_paths), 586)

    def test_find_test_directories(self):
        test_paths = self.eda.get_test_mri_paths()
        self.assertEqual(len(test_paths), 88)


if __name__ == '__main__':
    unittest.main()