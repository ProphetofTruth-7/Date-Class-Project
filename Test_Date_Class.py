import unittest
from date_class import Date

class TestDate(unittest.TestCase):
    def test_default_constructor(self):
        self.assertEqual(Date().alphabetic_return(), "January 01, 1900")

if __name__ == "__main__":
    unittest.main()