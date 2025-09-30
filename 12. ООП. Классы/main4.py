class Date:
    def __init__(self, day=0, month=0, year=0):
        self.__day = day
        self.__month = month
        self.__year = year

    def is_leap(self):
        return self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0

    def __str__(self):
        return f"{self.__day:02}.{self.__month:02}.{self.__year}"

    def add_day(self, days):
        for i in range(days):
            if self.__month == 4 or self.__month == 6 or self.__month == 9 or self.__month == 11:
                n = 30
            elif self.__month == 2:
                n = 29 if (self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0 else 28
            else:
                n = 31

            if self.__day < n:
                self.__day += 1
            else:
                self.__day = 1
                if self.__month == 12:
                    self.__month = 1
                    self.__year += 1
                else:
                    self.__month += 1

    # Перегрузка оператора сложения (+)
    def __add__(self, other):
        new_date = Date(self.__day, self.__month, self.__year)
        new_date.add_day(other)
        return new_date





date = Date(29, 2, 2020)
print(date + 5)
