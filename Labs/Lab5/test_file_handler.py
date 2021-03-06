# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352

from unittest import TestCase
from file_handler import FileHandler
from file_handler import InvalidFileTypeError

"""
Unit testing for FileHandler methods.
"""


class TestFileHandler(TestCase):
    """
    Test functions associated with FileHandler class.
    """

    def test_load_data_file_not_found(self):
        """
        Test whether FileNotFoundError is raised if the path does not exist.
        :return: FileNotFoundError
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data,
                          "./abc.exe", ".exe")

    def test_load_data_ext_mismatch(self):
        """
        Test whether path and file extension mismatch will raise ValueError.
        :return: ValueError
        """
        self.assertRaises(ValueError, FileHandler.load_data,
                          "./data.json", ".txt")

    def test_load_data_wrong_ext(self):
        """
        Test whether a non-accepted file extension (see FIleExtensions enum)
        raises InvalidFileTypeError.
        :return:
        """
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          "./dictionary.py", ".py")
