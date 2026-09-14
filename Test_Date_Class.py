import unittest
from Date_Class import Date

class TestDate(unittest.TestCase):
    def test_default_constructor(self):
        self.assertEqual(Date().alphabetic_return(), "January 01, 1900", msg="Among Us")
        """ Very simple. We run the constructor naturally and automatically. The assertEqual runs, checking if the value returned by alphabetic_return = what we expect/know the datetime value should be stored as"""

if __name__ == "__main__":
    unittest.main()