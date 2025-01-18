import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = float('inf')
        for ln in range(l, r + 1):
            for i in range(n - ln + 1):
                cur = s[i + ln] - s[i]
                if cur > 0:
                    ans = min(ans, cur)
        return ans if ans != float('inf') else -1

sol = Solution()
print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))  # 1
print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))  # -1
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))  # 3
