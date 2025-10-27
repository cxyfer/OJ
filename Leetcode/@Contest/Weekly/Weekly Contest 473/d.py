import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = 0
        mp = defaultdict(int)
        mp[0] = 1
        for r, x in enumerate(nums):
            s = (s + x) % k
            ans += mp[s]
            mp[s] += 1
        for x, lst in groupby(nums):
            ln = len(list(lst))
            g = math.gcd(x, k)
            m = k // g
            t = ln // m
            if t > 0:
                ans -= t * ln - m * t * (t + 1) // 2
        return ans

sol = Solution()
print(sol.numGoodSubarrays([1,2,3], 3))  # 3
print(sol.numGoodSubarrays([2,2,2,2,2,2], 6))  # 2