import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        groups = []
        i = 0
        while i < n:
            st = i
            while i + 1 < n and nums[i] <= nums[i + 1]:
                i += 1
            groups.append((st, i))
            i += 1
        ans = min(n, max(r - l + 2 for l, r in groups))
        
        L = [0] * n
        R = [0] * n
        for l, r in groups:
            for i in range(l, r + 1):
                L[i] = l
                R[i] = r
        for i in range(1, n - 1):
            if nums[i - 1] <= nums[i + 1]:
                ans = max(ans, R[i + 1] - L[i - 1] + 1)
        return ans

sol = Solution()
print(sol.longestSubarray([1,2,3,1,2]))  # 4
print(sol.longestSubarray([2,2,2,2,2]))  # 5
print(sol.longestSubarray([1,5,-10,5]))  # 4
print(sol.longestSubarray([1,2,3,1,2]))  # 4
print(sol.longestSubarray([8, -8]))  # 2