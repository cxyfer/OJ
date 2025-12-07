import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

MAX_N = int(5e5 + 5)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

st = set(primes)
A = [0]
s = 0
for p in primes:
    s += p
    if s in st:
        A.append(s)

class Solution:
    def largestPrime(self, n: int) -> int:
        i = bisect_right(A, n) - 1
        return A[i]