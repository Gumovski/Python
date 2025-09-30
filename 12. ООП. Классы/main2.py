class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
            Магический метод для преобразования объекта класса Date в строку.
        Returns:
            str: Возвращает строковое представление даты в формате 'день.месяц.год'.
        """
        return f"{self.day:02}.{self.month:02}.{self.year}"


date = Date(5, 7, 2021)
print(date)
