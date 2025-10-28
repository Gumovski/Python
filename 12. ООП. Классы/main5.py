class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_name(self):
        return "Rectangle"


# Создаём класс Square на основе класса Rectangle
class Square(Rectangle):
    def __init__(self, size):
        # Вызываем конструктор базового (родительского) класса
        super().__init__(size, size)

    def get_name(self):
        return "Square"


square = Square(5)
print(square.area())  # Выведет: 25
print(square.perimeter())  # Выведет: 20
print(square.get_name())  # Выведет: Square

