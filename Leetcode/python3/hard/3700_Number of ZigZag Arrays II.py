#
# @lc app=leetcode id=3700 lang=python3
#
# [3700] Number of ZigZag Arrays II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
import numpy as np

MOD = int(1e9) + 7

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


def matrix_power_mul(A: np.ndarray, n: int, x: np.ndarray, mod: int):
    assert len(A[0]) == len(x)
    res = x
    while n > 0:
        if n & 1:
            res = A @ res % mod
        A = A @ A % mod
        n >>= 1
    return res

class Solution1:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = Matrix([[1] for _ in range(V * 2)])
        M = [[0] * (V * 2) for _ in range(V * 2)]
        for i in range(V):
            for j in range(V, V + i):
                M[i][j] = 1
            for j in range(i + 1, V):
                M[i + V][j] = 1
        M = Matrix(M)
        f = M.mul_pow(n - 1, f)
        return sum(map(sum, f.mat)) % MOD

class Solution1np:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = np.ones((V * 2, 1), dtype=np.object_)
        M = np.zeros((V * 2, V * 2), dtype=np.object_)
        for i in range(V):
            for j in range(V, V + i):
                M[i][j] = 1
            for j in range(i + 1, V):
                M[i + V][j] = 1
        f = matrix_power_mul(M, n - 1, f, MOD)
        return int(np.sum(f) % MOD)


class Solution2:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = Matrix([[1] for _ in range(V)])
        M = [[0] * V for _ in range(V)]
        for i in range(V):
            for j in range(V - i - 1):
                M[i][j] = 1
        M = Matrix(M)
        f = M.mul_pow(n - 1, f)
        return sum(map(sum, f.mat)) * 2 % MOD


class Solution2np:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = np.ones((V, 1), dtype=np.object_)
        M = np.tril(np.ones((V, V), dtype=np.object_)[::-1], k=-1)[::-1]
        f = matrix_power_mul(M, n - 1, f, MOD)
        return int(np.sum(f) * 2 % MOD)


Solution = Solution1
# Solution = Solution1np
# Solution = Solution2
# Solution = Solution2np
# @lc code=end

sol = Solution()
print(sol.zigZagArrays(3, 4, 5))  # 2
print(sol.zigZagArrays(3, 1, 3))  # 10
print(sol.zigZagArrays(7, 9, 39))  # 650716800
print(sol.zigZagArrays(3254, 1, 25))  # 572164226