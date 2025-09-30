class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set_date(self, date_str):
        self.day, self.month, self.year = list(map(int, date_str.split(".")))

    def add_day(self, days):
        for i in range(days):
            if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                n = 30
            elif self.month == 2:
                 n = 29 if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 else 28
            else:
                n = 31

            if self.day < n:
                self.day += 1
            else:
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1

answer = Date(1,1,1970)
answer.set_date("1.2.2000")
answer.add_day(28)
print(answer.day,answer.month,answer.year)
