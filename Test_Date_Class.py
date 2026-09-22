import unittest
from Date_Class import Date


class TestDate(unittest.TestCase):
    def test_default_constructor(self):
        self.assertEqual(Date().alphabetic_return(), "January 01, 1900")

    def test_valid_constructor(self):
        self.assertEqual(Date(2026, 9, 14).alphabetic_return(), "September 14, 2026")

    def setUp(self):
        self.date = Date(2026, 9, 13)
        self.datebefore = Date(2026, 8, 4)
        self.dateafter = Date(2026, 10, 26)
        self.dateleap = Date(2024, 2, 29)




    # Part 2 Tests
# Subtraction Tests
    def test_subtraction_basic(self):
        self.assertEqual(self.date - self.datebefore, 40)
        self.assertEqual(self.date - self.dateafter, -43)
        self.assertEqual(self.date - self.date, 0)
        self.assertEqual(self.date - self.dateleap, 927)
    def test_subtraction_invalid_type(self):
        with self.assertRaises(TypeError):
            self.date - 5
    def test_subtraction_demands(self):
        self.assertEqual(Date(2014, 4, 18) - Date(2014, 4, 10), 8)
        self.assertEqual(Date(2006, 2, 2) - Date(2003, 11, 10), 815)

# Increment Tests
    def test_increment_single(self):
        self.date.increment()
        self.assertEqual(self.date.alphabetic_return(), "September 14, 2026")
    def test_increment_request1(self):
        testDate = Date(2026, 4, 30)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "May 01, 2026")
    def test_increment_request2(self):
        testDate = Date(2026, 1, 31)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "February 01, 2026")
    def test_increment_request3(self):
        testDate = Date(2026, 2, 28)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "March 01, 2026")
    def test_increment_request4(self):
        testDate = Date(2024, 2, 28)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "February 29, 2024")
    def test_increment_request5(self):
        testDate = Date(2024, 2, 29)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "March 01, 2024")
    def test_increment_request6(self):
        testDate = Date(2026, 12, 31)
        testDate.increment()
        self.assertEqual(testDate.alphabetic_return(), "January 01, 2027")
    def test_proper_increment_return(self):
        self.assertIs(self.date.increment(), self.date)

# Decrement Tests
    def test_decrement_single(self):
        self.date.decrement()
        self.assertEqual(self.date.alphabetic_return(), "September 12, 2026")
    def test_decrement_request1(self):
        testDate = Date(2026, 5, 1)
        testDate.decrement()
        self.assertEqual(testDate.alphabetic_return(), "April 30, 2026")
    def test_decrement_request2(self):
        testDate = Date(2026, 3, 1)
        testDate.decrement()
        self.assertEqual(testDate.alphabetic_return(), "February 28, 2026")
    def test_decrement_request3(self):
        testDate = Date(2024, 3, 1)
        testDate.decrement()
        self.assertEqual(testDate.alphabetic_return(), "February 29, 2024")
    def test_decrement_request4(self):
        testDate = Date(2026, 1, 1)
        testDate.decrement()
        self.assertEqual(testDate.alphabetic_return(), "December 31, 2025")
    def test_proper_decrement_return(self):
        self.assertIs(self.date.decrement(), self.date)


    # Part 1 Tests

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
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

    def test_is_leap_year_instance(self):
        self.assertFalse(self.date.is_leap_year(self.date.year))
        self.date.set_date(2024, 4, 3)
        self.assertTrue(self.date.is_leap_year(self.date.year))

    def test_is_leap_year_static(self):
        self.assertTrue(self.date.is_leap_year(2024))
        self.assertFalse(self.date.is_leap_year(2023))

    def test_last_day_instance(self):
        self.assertEqual(self.date.last_day(self.date.year, self.date.month), 30)

    def test_last_day_static(self):
        self.assertEqual(self.date.last_day(2024, 2), 29)

    def test_numeric_return(self):
        self.date.set_date(2021, 12, 25)
        self.assertEqual(self.date.numeric_return(), "12/25/2021")

    def test_alphabetic_return(self):
        self.date.set_date(2021, 12, 25)
        self.assertEqual(self.date.alphabetic_return(), "December 25, 2021")

    def test_alt_alphabetic_return(self):
        self.date.set_date(2021, 12, 25)
        self.assertEqual(self.date.alt_alphabetic_return(), "25 December 2021")

if __name__ == "__main__":
    unittest.main()