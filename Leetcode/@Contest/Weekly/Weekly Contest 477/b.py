import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        ans = 0
        s = d = 0
        mp = defaultdict(lambda : float('inf'))
        mp[(0, 0)] = -1
        for i, x in enumerate(nums):
            s ^= x
            d += 1 if x & 1 else -1
            ans = max(ans, i - mp[(s, d)])
            if mp[(s, d)] == float('inf'):
                mp[(s, d)] = i
        return ans