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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)

        ans = 0
        cnt = 0
        left = 0
        for right in range(n):
            if nums[right] == mx:
                cnt += 1
            if cnt >= k:
                while cnt >= k:
                    ans += n - right
                    if nums[left] == mx:
                        cnt -= 1
                    left += 1
        return ans

sol = Solution()
print(sol.countSubarrays([1,3,2,3,3], 2)) # 6
print(sol.countSubarrays([1,4,2,1], 3)) # 0
print(sol.countSubarrays([1,1,1,1,1,1], 3)) # 4