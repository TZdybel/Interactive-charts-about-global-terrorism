class Date(object):
    """Class storing some date"""

    def __init__(self, day: int, month: int, year: int):
        # try:
        if month > 12 or month < 0:
            raise ValueError
        else:
            if month == 0:
                month = 1
            if month in [1, 3, 5, 7, 8, 10, 12]:
               possible_day = 31
            elif month == 2:
                if year % 4 == 0:
                    possible_day = 29
                else:
                    possible_day = 28
            else:
                possible_day = 30
        if day > possible_day or day < 0:
            raise ValueError
        if year > 2018 or year < 1970:
            raise ValueError
        if day == 0:
            day = 1
        # except ValueError:
        #     print("Invalid date provided, check your data")
        #     return
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return "{0}/{1}/{2}".format(self.__day, self.__month, self.__year)

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other
