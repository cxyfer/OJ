import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

# class Solution:
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#         MOD = 10**9 + 7
#         cnt = [0] * 26
#         for ch in s:
#             cnt[ord(ch) - ord('a')] += 1

#         for _ in range(t):
#             new_cnt = [0] * 26
#             for i in range(26):
#                 cur = cnt[i]
#                 if cur == 0:
#                     continue
#                 if i == 25:  # z -> ab
#                     new_cnt[0] = (new_cnt[0] + cur) % MOD
#                     new_cnt[1] = (new_cnt[1] + cur) % MOD
#                 else:
#                     new_cnt[i + 1] = (new_cnt[i + 1] + cur) % MOD
#             cnt = new_cnt

#         return sum(cnt) % MOD

MOD = 10**9 + 7

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        p, q, r = len(self.mat), len(other.mat), len(other.mat[0])
        res = [[0] * r for _ in range(p)]
        for i, row in enumerate(self.mat):
            for j, col in enumerate(zip(*other.mat)):
                res[i][j] = sum(x * y for x, y in zip(row, col)) % MOD
        return Matrix(res)
    
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

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        T = [[0] * 26 for _ in range(26)] # Transition Matrix
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                T[i][j] = 1
        T = Matrix(T)
        T_t = T ** t

        ans = [0] * 26
        for i in range(26):
            for j in range(26):
                ans[j] += cnt[i] * T_t.mat[i][j]
                ans[j] %= MOD
        return sum(ans) % MOD

sol = Solution()
print(sol.lengthAfterTransformations("abcyy", 2)) # 7
print(sol.lengthAfterTransformations("azbk", 1)) # 5
 
