from datetime import date
import calendar

class Date:
    def __init__(self, day: int = 1, month: int = 1, year: int = 1900) -> None:
        self.__date = date(day, month, year)


    @property
    def day(self) -> int:
        return self.__date.day

    @property
    def month(self) -> int:
        return self.__date.month

    @property
    def year(self) -> int:
        return self.__date.year

    def set_date(self, month: int, day: int, year: int) -> None:
        revised_date = date(year, month, day)
        self.__date = revised_date

    def is_leap_year(self) -> bool:
        return calendar.isleap(self.__date.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return calendar.isleap(year)

    def last_day(self) -> int:
        return calendar.monthrange(self.__date.year, self.__date.month)[1]

    @staticmethod
    def last_day(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]

    def numeric_return(self) -> str:
        return self.__date.strftime("%m/%d/%Y")

    def alphabetic_return(self) -> str:
        return self.__date.strftime("%B %d, %Y")

    def alt_alphabetic_return(self) -> str:
        return self.__date.strftime("%d %B %Y")