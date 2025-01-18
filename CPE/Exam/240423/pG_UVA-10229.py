"""
    矩陣快速冪(平方求冪)
    這是 1 顆星，但 UVA-374 卻有 2 顆星 ?
"""

class Matrix:
    """
        a b
        c d
    """
    def __init__(self, a, b, c, d, mask):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.mask = mask

    def __mul__(self, other): # operator *
        return Matrix(
            (self.a * other.a + self.b * other.c) & self.mask,
            (self.a * other.b + self.b * other.d) & self.mask,
            (self.c * other.a + self.d * other.c) & self.mask,
            (self.c * other.b + self.d * other.d) & self.mask,
            self.mask
        )

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    M = Matrix(1, 1, 1, 0, (1 << m )- 1)
    X = Matrix(1, 0, 0, 0, (1 << m )- 1)
    while n: # exponentiation by squaring
        if n & 1:
            X = X * M
        M = M * M
        n >>= 1
    print(X.b)