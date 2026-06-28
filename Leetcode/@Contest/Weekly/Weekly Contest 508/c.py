import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import inf, floor, ceil

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        def solve(func) -> int:
            ans = -inf
            f = [-inf] * 3
            for x in nums:
                nf = [-inf] * 3
                y = func(x)

                nf[0] = max(f[0] + x, x)
                nf[1] = max(f[0] + y, f[1] + y, y)
                nf[2] = max(f[1] + x, f[2] + x)
    
                f = nf
                ans = max(ans, max(f[1], f[2]))
            return ans

        func1 = lambda x : x * k
        func2 = lambda x : floor(x / k) if x >= 0 else ceil(x / k)

        return max(solve(func1), solve(func2))

sol = Solution()
print(sol.maxSubarraySum([1,-2,3,4,-5], 2))  # Output: 14