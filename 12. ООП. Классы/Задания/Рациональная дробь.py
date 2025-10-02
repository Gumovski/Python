class Rational:
    def __init__(self,n,d): #n - числитель d - знаменатель
        self.n = n
        self.d = d
        if d  == 0:
            print('Error')
        if d < 0:
            n = -n
            d = -d
        if n == 0:
            self.n = 0
            self.d = d

