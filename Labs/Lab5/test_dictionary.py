# Prerna Prerna, A01195525
# Saksham Bhardwaj,A01185352

from unittest import TestCase
from dictionary import Dictionary

"""
Unit tests for applicable functions in Dictionary class.
"""


class TestDictionary(TestCase):
    """
    Test functions in Dictionary class.
    """

    def test_is_data_loaded_false(self):
        """
        Test whether is_data_loaded returns false when no data is loaded
        into the dictionary.
        :return: False
        """
        dictionary = Dictionary()
        msg = "FAILED: Data was loaded without calling load_data"
        self.assertFalse(dictionary.is_data_loaded(), msg)

    def test_is_data_loaded_true(self):
        """
        Test whether is_data_loaded returns true when data is loaded into
        the dictionary.
        :return: True
        """
        dictionary = Dictionary()
        dictionary.load_dictionary("./data.json")
        msg = "FAILED: Data was not loaded when load_data was called"
        self.assertTrue(dictionary.is_data_loaded(), msg)

    def test__definitions(self):
        """
        Test the formatted output of definitions stored in an array.
        :return: String
        """
        dictionary = Dictionary()
        dictionary.load_dictionary("./data.json")
        result = "\n== sadly ==\n" \
                 "In an unfortunate manner.\n" \
                 "With sadness.\n"
        self.assertEqual(dictionary._definitions("sadly"), result)
