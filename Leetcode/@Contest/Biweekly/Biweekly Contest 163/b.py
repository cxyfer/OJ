import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
"""
1. a * b > 0
|a + b| = |a| + |b|
|a - b| = ||a| - |b||
2. a * b < 0
|a + b| = ||a| - |b||
|a - b| = |a| + |b|

min(|a - b|, |a + b|) = ||a| - |b||
max(|a - b|, |a + b|) = |a| + |b| >= max(|a|, |b|) 恆成立

||a| - |b|| <= min(|a|, |b|)
assert |a| >= |b|
|a| <= 2 |b|
"""
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums.sort(key = lambda x : abs(x))
        ans = l = 0
        for r, x in enumerate(list(map(abs, nums))):
            while l < r and x > 2 * abs(nums[l]):
                l += 1
            ans += (r - l)
        return ans

sol = Solution()
print(sol.perfectPairs([0,1,2,3]))  # 2