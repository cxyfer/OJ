#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
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

class Solution1:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        M = Matrix([[0] * 26 for _ in range(26)])
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                M[i][j] = 1
        x = Matrix([[1] for i in range(26)])
        # f = (M ** t) * x
        f = M.mul_pow(t, x)
        return sum(f[i][0] * cnt[i] for i in range(26)) % MOD
    
import numpy as np

def matrix_power(A: np.ndarray, n: int, mod: int):
    res = np.eye(len(A), dtype=object)
    while n > 0:
        if n & 1:
            res = res @ A % mod
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

class Solution2:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        M = np.zeros((26, 26), dtype=object)
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                M[i, j] = 1
        
        x = np.ones((26, 1), dtype=object)
        f = matrix_power_mul(M, t, x, MOD)
        return sum(f[i, 0] * cnt[i] for i in range(26)) % MOD
    
# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
# print(sol.lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))  # 7
print(sol.lengthAfterTransformations("mppgvcssluzhipednraxbdfbyn", 3719, [5,3,8,1,4,2,2,4,5,2,8,5,8,2,6,10,8,1,4,1,7,4,2,4,7,5]))  # 1000000006
# 467065288
