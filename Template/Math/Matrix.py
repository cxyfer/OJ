MOD = int(1e9 + 7)
class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        return Matrix([[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*other.mat)]
                for row in self.mat])
    
    def __pow__(self, k):
        assert len(self.mat) == len(self.mat[0])
        n = len(self.mat)
        res = Matrix([[int(i == j) for j in range(n)] for i in range(n)])
        base = self
        while k > 0:
            if k & 1:
                res *= base
            base *= base
            k >>= 1
        return res
    
    def mul_pow(self, k, x):
        assert len(self.mat[0]) == len(x.mat)
        res = x
        base = self
        while k > 0:
            if k & 1:
                res = base * res
            base *= base
            k >>= 1
        return res
    
    def __getitem__(self, i):
        return self.mat[i]

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self.mat))
    
"""
    numpy version
"""

import numpy as np

def matrix_power(A: np.ndarray, n: int, mod: int):
    res = np.eye(len(A), dtype=object)
    while n > 0:
        if n & 1:
            res = A @ res % mod
        A = A @ A % mod
        n >>= 1
    return res

def matrix_power_mul(A: np.ndarray, n: int, x: np.ndarray, mod: int):
    assert len(A[0]) == len(x)
    res = x
    while n > 0:
        if n & 1:
            res = A @ res % mod
        A = A @ A % mod
        n >>= 1
    return res

if __name__ == "__main__":
    mat = Matrix([[1, 1], [1, 0]])
    x = Matrix([[1], [0]])
    print(mat ** 10 * x)

    mat = np.array([[1, 1], [1, 0]])
    x = np.array([[1], [0]])
    print(matrix_power(mat, 10, MOD) @ x % MOD)
    print(matrix_power_mul(mat, 10, x, MOD))

