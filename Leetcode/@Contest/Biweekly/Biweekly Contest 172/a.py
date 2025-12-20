import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 正難則反
        n = len(nums)
        vis = set()
        ans = (n + 2) // 3
        i = (n - 1) // 3 * 3
        while i >= 0:
            for j in range(i, min(i + 3, n)):
                x = nums[j]
                if x in vis:
                    i = -1
                    break
                vis.add(x)
            else:
                ans -= 1
                i -= 3
        return ans 