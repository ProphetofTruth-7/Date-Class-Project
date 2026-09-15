import unittest
from Date_Class import Date

class TestDate(unittest.TestCase): #Allows unittest in. It then runs thorugh all code that begins with test_ and checks the assert
    def test_default_constructor(self):
        self.assertEqual(Date().alphabetic_return(), "January 01, 1900")
        #Very simple. We run the constructor naturally and automatically. The assertEqual runs, checking if the value returned by alphabetic_return = what we expect/know the datetime value should be stored as

    def test_valid_constructor(self):
        self.assertEqual(Date(2026, 9, 14).alphabetic_return(), "September 14, 2026")

    def setUp(self): # Mandatory. Establishes a baseline to be used in all tests. It is run before each test, giving a grappling point for action
        self.date = Date(2026, 9, 13)

    def test_invalid_month(self):
        with self.assertRaises(ValueError): #assertRaises expects that the code inside returns/raises whatever is within (). If it does, the test passes. If not, it fails. Since ValueError is within the (), assertRaises expects a ValueError to be returned.
            Date(1900, 13, 1)

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            Date(1900, 11, 60)

    def test_invalid_leap_year(self):
        with self.assertRaises(ValueError):
            Date(2026, 2, 29)

    def test_read_property_assignment(self):
        with self.assertRaises(AttributeError):
            self.date.day = 10

    def test_set_date(self):
        self.date.set_date(2007, 4, 2)
        self.assertEqual(self.date.alphabetic_return(), "April 02, 2007")

    def test_set_invalid_date(self):
        with self.assertRaises(ValueError):
            self.date.set_date(2007, 4, 60)

    def test_original_date_unchanged(self):
        with self.assertRaises(ValueError):
            self.date.set_date(2007, 4, 60)
        self.assertEqual(self.date.alphabetic_return(), "September 13, 2026")

if __name__ == "__main__":
    unittest.main()