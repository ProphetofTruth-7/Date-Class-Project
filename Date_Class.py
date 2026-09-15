from datetime import date
import calendar

class Date:
    """A wrapper class that provides extra, specific, user-friendly functionality for the datetime class. Forbids access to the main values(year, month, day) via read-only properties, and answers many EDGECASES expected in calendar programs"""

    def __init__(self, year: int = 1900, month: int = 1, day: int = 1) -> None:
        self.__date = date(year, month, day)
    """ Constructor for the Date Class. Establishes the baseline values, but does not force validation. Importantly, does not initialize each value separately, keeping them firmly housed in datetime """

    @property
    def day(self) -> int:
        return self.__date.day
    """ Returns the day currently stored in datetime as a integer """

    @property
    def month(self) -> int:
        return self.__date.month
    """ Returns the month currently stored in datetime as a integer """

    @property
    def year(self) -> int:
        return self.__date.year
    """ Returns the year currently stored in datetime as a integer """

    def set_date(self, year: int, month: int, day: int) -> None:
        revised_date = date(year, month, day)
        self.__date = revised_date
    """ Sets the date to the specified month, day, and year, creating a revised datetime object with said values """

    def is_leap_year(self) -> bool:
        return calendar.isleap(self.__date.year)
    """ Checks if the currently stored year is a leap year, returning True if so """

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return calendar.isleap(year)
    """ Checks if the provided year is a leap year, returning True if so """

    def last_day(self) -> int:
        return calendar.monthrange(self.__date.year, self.__date.month)[1]
    """ Returns the last day of the currently stored month(and year, if it matters) """

    @staticmethod
    def last_day(year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]
    """ Returns the last day of the provided month(and year, if it matters) """

    def numeric_return(self) -> str:
        return self.__date.strftime("%m/%d/%Y")
    """ Returns the data in numeric format(# Month/# Day/# Year) """

    def alphabetic_return(self) -> str:
        return self.__date.strftime("%B %d, %Y")
    """ Returns the data in alphabetic format(Month Day, Year) """

    def alt_alphabetic_return(self) -> str:
        return self.__date.strftime("%d %B %Y")
    """ Returns the data in an alternative alphabetic format(Day Month Year) """