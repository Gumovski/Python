class Rational:
    def __init__(self, n, d):  # n - числитель d - знаменатель
        self.n = n
        self.d = d
        if d == 0:
            print('Error')
        if d < 0:
            n = -n
            d = -d
        self.__reduce()

    def __reduce(self):
        if self.n == 0:
            self.n = 0
            self.d = self.d

        n1 = self.n if self.n >= 0 else -self.n
        d1 = self.d
        while d1:
            n1, d1 = d1, n1 % d1
        gcd = n1

        self.n //= gcd
        self.d //= gcd

    def __add__(self, other):
        new_n = self.n * other.d + self.d * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        new_n = self.n * other.d - self.d * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        return self.n * other.d < other.n * self.d

    def __gt__(self, other):
        return other < self

    def __str__(self):
        return f"{self.n}/{self.d}"


first = Rational(1, 2)
second = Rational(1, 3)
print(first + second)
