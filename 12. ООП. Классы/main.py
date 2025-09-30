class Person:
    first_name = ''
    last_name = ''
    birth_year = 0

# Создание экземпляра класса
stepan = Person()
# Присвоение полям класса значений
stepan.first_name = "Степан"
stepan.last_name = "Гумовский"
stepan.birth_year = 2009

# 2 проблемы:
# 1. Нарушена инкапсуляция, т.е. имеется возможность прямого доступа к полям класса, а это нежелательно
# 2. Не удобно (громоздко) задавать значения полям класса

# Решение проблемы создания экземпляров
# Использование конструкторов

class Person:
    def __init__(self, first_name, last_name, birth_year):
        # Создаём и инициализируем поля класса
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

stepan = Person("Степан", "Гумовский", 2009)

# Методы классов

class Person:
    def __init__(self, first_name, last_name, birth_year):
        # Создаём и инициализируем поля класса
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_age(self):
        from datetime import date
        current_year = date.today().year
        return current_year - self.birth_year



