# Инкапсуляция

class Date:
    def __init__(self, day=0, month=0, year=0):
        self.__day = day
        self.__month = month
        self.__year = year

    def is_leap(self):
        return self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0

    # Свойство (property) - это способ предоставить доступ к приватным атрибутам класса через методы.
    @property
    def day(self):
        return self.__day

    # Сеттер - это метод для изменения значения приватного атрибута класса.
    @day.setter
    def day(self, value):
        if self.__month in [4, 6, 9, 11]:
            max_day = 30
        elif self.__month == 2 and self.is_leap():
            max_day = 29
        elif self.__month == 2:
            max_day = 28
        else:
            max_day = 31
        if not isinstance(value, int):
            raise TypeError("Ошибка!\nДень должен быть целым числом!")
        elif not (1 <= value <= max_day):
            raise ValueError("Ошибка!\nНекорректный день!")
        else:
            self.__day = value

    def __str__(self):
        return f"{self.__day:02}.{self.__month:02}.{self.__year}"

# Ошибка! Прямой доступ к полям класса
date = Date(5, 9, 2006)
date.month = 155
#

try:
    date.day = "hello"
except Exception as e:
    print(e)

print(date)

