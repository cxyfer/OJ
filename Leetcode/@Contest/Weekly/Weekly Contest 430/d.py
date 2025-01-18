import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

MOD = 10**9 + 7
MAXN = int(1e5 + 5)
fact = [1] * (MAXN + 1)
invFact = [1] * (MAXN + 1)
for i in range(2, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD
invFact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN - 1, 0, -1):
    invFact[i] = (invFact[i+1] * (i+1)) % MOD

def comb(n, r):
    return (fact[n] * invFact[r] % MOD) * invFact[n-r] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return (m * pow(m-1, n-1, MOD)) % MOD
        ans = m
        ans = (ans * comb(n - 1, k)) % MOD
        ans = (ans * pow(m - 1, (n - 1) - k, MOD)) % MOD
        return ans

sol = Solution()
print(sol.countGoodArrays(3, 2, 1)) # 4
print(sol.countGoodArrays(4, 2, 2)) # 6
print(sol.countGoodArrays(5, 2, 0)) # 2