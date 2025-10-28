"""
Абстрактный класс - это класс, экземпляры которого не могут быть созданы.
Также, абстрактные классы необходимы, чтобы обязать наследникам реализовать определенные методы.
"""
import abc
from math import pi


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass
    @abc.abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


s = Circle(5)
print(s.area())
print(s.perimeter())
