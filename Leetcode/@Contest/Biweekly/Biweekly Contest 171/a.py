import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

def is_prime(x):
    if x == 1:
        return False
    for p in range(2, math.isqrt(x) + 1):
        if x % p == 0:
            return False
    return True

class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)
        n = len(s)
        return all(is_prime(int(s[:i + 1])) and is_prime(int(s[i:])) for i in range(n))

sol = Solution()
print(sol.completePrime(23))  # True