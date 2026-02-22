from math import gcd


class Fraction:
    __slots__ = ["num", "dem"]

    def __init__(self, num, dem=1):
        if dem == 0:
            raise ZeroDivisionError("Fraction denominator cannot be zero")

        if dem < 0:
            num = -num
            dem = -dem

        g = gcd(num, dem)
        self.num = num // g
        self.dem = dem // g

    def __eq__(self, other):
        if isinstance(other, int):
            return self.dem == 1 and self.num == other
        if isinstance(other, Fraction):
            return self.num == other.num and self.dem == other.dem
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.num < other * self.dem
        if isinstance(other, Fraction):
            return self.num * other.dem < other.num * self.dem
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, int):
            return self.num <= other * self.dem
        if isinstance(other, Fraction):
            return self.num * other.dem <= other.num * self.dem
        return NotImplemented

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __bool__(self):
        return self.num != 0

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.num + other * self.dem, self.dem)
        if isinstance(other, Fraction):
            return Fraction(
                self.num * other.dem + other.num * self.dem, self.dem * other.dem
            )
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            return Fraction(self.num - other * self.dem, self.dem)
        if isinstance(other, Fraction):
            return Fraction(
                self.num * other.dem - other.num * self.dem, self.dem * other.dem
            )
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.dem - self.num, self.dem)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.num * other, self.dem)
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.dem * other.dem)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.num, self.dem * other)
        if isinstance(other, Fraction):
            return Fraction(self.num * other.dem, self.dem * other.num)
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.dem, self.num)
        return NotImplemented

    def __neg__(self):
        res = Fraction.__new__(Fraction)
        res.num = -self.num
        res.dem = self.dem
        return res

    def __abs__(self):
        res = Fraction.__new__(Fraction)
        res.num = abs(self.num)
        res.dem = self.dem
        return res

    def __float__(self):
        return self.num / self.dem

    def __hash__(self):
        return hash((self.num, self.dem))

    def __str__(self):
        return f"{self.num}/{self.dem}" if self.dem != 1 else str(self.num)

    def __repr__(self):
        return f"Fraction({self.num}, {self.dem})"
