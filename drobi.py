class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return f'{self.numer} / {self.denom}'
    def __add__(self, other):
        result = (self.numer * other.denom + other.numer * self.denom)
        result2 = (self.denom * other.denom)
        return Fraction(result, result2)
    def __sub__(self, other):
        a = (self.numer * other.denom - other.numer *self.denom)
        b = (self.denom * other.denom)
        return Fraction(a, b)
    def convert(self):
        return  self.numer / self.denom
oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)
print(oneHalf.convert())
