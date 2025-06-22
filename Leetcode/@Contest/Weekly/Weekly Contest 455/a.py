import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

MAX_N = 105
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, MAX_N):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        return any(is_prime[v] for v in cnt.values())