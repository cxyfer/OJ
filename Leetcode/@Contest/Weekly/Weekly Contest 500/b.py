import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q2. 質數篩 + 二分 + 前綴和
預處理範圍中的質數，則可以利用二分找到 [L, R] 中的質數數量以及對應的下標，
利用前綴和計算區間和即可。
"""

MAX_N = int(1e4 + 5)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]
s = list(accumulate(primes, initial=0))

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = int(str(n)[::-1])
        L, R = min(n, rev), max(n, rev)
        idx1 = bisect_left(primes, L)
        idx2 = bisect_right(primes, R)
        return s[idx2] - s[idx1]