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