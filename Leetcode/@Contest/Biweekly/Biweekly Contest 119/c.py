import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        Sliding window
    """
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        cnt = Counter()
        for idx, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, idx - left + 1)
        return ans
sol = Solution()
print(sol.maxSubarrayLength([1,2,3,1,2,3,1,2], 2)) # 6
print(sol.maxSubarrayLength([1,2,1,2,1,2,1,2], 1)) # 2
print(sol.maxSubarrayLength([5,5,5,5,5,5,5], 4)) # 4

        