class Modular:
    def __init__(self, val):
        self.val = val % MOD

    def __int__(self):
        return self.val

    def __add__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val + other.val)
        else:
            return Modular(self.val + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val - other.val)
        else:
            return Modular(self.val - other)

    def __rsub__(self, other):
        return Modular(other - self.val)

    def __mul__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val * other.val)
        else:
            return Modular(self.val * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Modular):
            return self * other.inv()
        else:
            return self * pow(other, MOD - 2, MOD)

    def __rtruediv__(self, other):
        return Modular(other) / self

    def __pow__(self, other):
        return Modular(pow(self.val, other, MOD))

    def __neg__(self):
        return Modular(-self.val)

    def inv(self):
        return pow(self, MOD - 2)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

Z = lambda x: Modular(x)