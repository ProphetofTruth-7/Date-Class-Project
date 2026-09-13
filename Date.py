from datetime import date
import calendar

class Date:
    def __init__(self, day: int = 1, month: int = 1, year: int = 1900):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year