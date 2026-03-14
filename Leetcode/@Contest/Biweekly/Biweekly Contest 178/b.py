import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        pre_mx = list(accumulate(nums, func=max))
        arr = sorted(math.gcd(x, mx) for x, mx in zip(nums, pre_mx))
        return sum(math.gcd(arr[i], arr[n - 1 - i]) for i in range(n // 2))