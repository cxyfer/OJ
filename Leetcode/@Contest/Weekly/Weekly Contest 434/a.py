import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = list(accumulate(nums))
        for i in range(n - 1):
            if abs(s[i] - (s[n-1] - s[i])) % 2 == 0:
                ans += 1
        return ans