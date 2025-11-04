import abc
from math import pi, sqrt, acos, degrees
import random

class Shape(abc.ABC):               #1),2),3)
    @abc.abstractmethod
    def area(self):
        pass
    @abc.abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть больше 0')
        self.__radius = radius

    def area(self):
        return pi * self.__radius**2

    def perimeter(self):
        return 2 * pi * self.__radius

    def __str__(self):
        return f"Circle(radius={self.__radius:.2f})"

class Rectangle(Shape):
    def __init__(self,width,height):
        if width <= 0 or height <= 0:
            raise ValueError('Значение ширины и длины должны быть > 0')
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"Rectangle({self.__width:.2f}, {self.__height:.2f})"

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        return f"Square({self.__width:.2f})"

class Ellipse(Shape):
    def __init__(self,major,minor):
        if major <=0 or minor <= 0:
            raise ValueError('Значение ширины и длины должны быть > 0')
        self.__major = major
        self.__minor = minor

    def area(self):
        return pi * self.__major * self.__minor

    def perimeter(self):
        a, b = self.__major, self.__minor
        h = ((a - b) / (a + b)) ** 2
        return pi * (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

    def __str__(self):
        return f"Ellipse({self.__major:.2f}, {self.__minor:.2f})"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Все стороны треугольника должны быть > 0')

        if (side1 + side2 <= side3 or
                side1 + side3 <= side2 or
                side2 + side3 <= side1):
            raise ValueError('Треугольника с такими сторонами не существует')

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Triangle({self.__side1:.2f},{self.__side2:.2f},{self.__side3:.2f})"

    def get_coordinates(self):
        a, b, c = self.__side1, self.__side2, self.__side3

        A = (0, 0)


        B = (a, 0)
        cos_angle_C = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

        sin_angle_C = sqrt(1 - cos_angle_C ** 2)

        C_x = b * cos_angle_C
        C_y = b * sin_angle_C

        C = (C_x, C_y)

        return [A, B, C]

    def get_angles(self):
        a, b, c = self.__side1, self.__side2, self.__side3

        angle_A = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        angle_B = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B

        return angle_A, angle_B, angle_C

def random_generate(count = 100):               #4)
    shapes = []
    list_of_s = [Circle, Rectangle, Square, Ellipse, Triangle]

    for i in range(count):
        list_of_shapes = random.choice(list_of_s)

        try:
            if list_of_shapes == Circle:
                radius = random.uniform(1.0, 20.0)
                shapes.append(Circle(radius))

            elif list_of_shapes == Rectangle:
                width = random.uniform(1.0, 15.0)
                height = random.uniform(1.0, 15.0)
                shapes.append(Rectangle(width, height))

            elif list_of_shapes == Square:
                side = random.uniform(1.0, 15.0)
                shapes.append(Square(side))

            elif list_of_shapes == Ellipse:
                major = random.uniform(1.0, 12.0)
                minor = random.uniform(1.0, major)
                shapes.append(Ellipse(major, minor))

            elif list_of_shapes == Triangle:
                while True:
                    side1 = random.uniform(1.0, 10.0)
                    side2 = random.uniform(1.0, 10.0)
                    side3 = random.uniform(1.0, 10.0)
                    if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
                        shapes.append(Triangle(side1, side2, side3))
                        break

        except ValueError:
            continue

    return shapes


def shape_with_max_area(shapes):            #5)
    if not shapes:
        raise ValueError("Список фигур пуст")

    max_area_shape = shapes[0]

    for shape in shapes:
        if shape.area() > max_area_shape.area():
            max_area_shape = shape

    return max_area_shape

def main():
    shapes = random_generate(100)

    max_shape = max(shapes, key=lambda x: x.area())
    position = shapes.index(max_shape)

    print("Фигура с Максимальной площадью:")
    print(f"Позиция в списке: {position}")
    print(f"{max_shape}, Площадь: {max_shape.area()}")
    print(f"{round(max_shape.area())}")
if __name__ == "__main__":
    main()