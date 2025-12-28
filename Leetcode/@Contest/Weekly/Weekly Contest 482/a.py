import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        pre = list(accumulate(nums))
        suf = list(accumulate(nums[::-1], func=lambda x, y: min(x, y)))[::-1]
        ans = float("-inf")
        for i in range(n - 1):
            ans = max(ans, pre[i] - suf[i + 1])
        return ans

sol = Solution()
print(sol.maximumScore([10,-1,3,-4,-5]))  # 17
print(sol.maximumScore([-7,-5,3]))  # -2