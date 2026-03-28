import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q2: ||組合數||
||題意其實就是計算左邊選 l 個，右邊選 k - l 個的組合數，
另外中間位置兩種選擇，故最後乘 2 即可。||
"""

MOD = int(1e9 + 7)

MAX_N = int(1e5 + 5)
fact = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD
invf = [-1] * (MAX_N + 1)
invf[MAX_N] = pow(fact[MAX_N], -1, MOD)
for i in range(MAX_N - 1, -1, -1):
    invf[i] = invf[i + 1] * (i + 1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invf[k] * invf[n - k]

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        ans = 0
        for l in range(k + 1):
            L = comb(pos, l)
            R = comb(n - pos - 1, k - l)
            ans += L * R % MOD
        return ans * 2 % MOD