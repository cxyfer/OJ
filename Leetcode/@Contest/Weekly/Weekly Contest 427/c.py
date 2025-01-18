import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        mp = [float('inf')] * k
        ans = -float('inf')
        for i in range(1, n + 1):
            m = i % k
            ans = max(ans, s[i] - mp[m])
            mp[m] = min(mp[m], s[i])
        return ans

sol = Solution()
print(sol.maxSubarraySum(nums = [-5,1,2,-3,4], k = 2)) # 4
