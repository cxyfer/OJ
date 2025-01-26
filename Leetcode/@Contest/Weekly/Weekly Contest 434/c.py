import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for d in range(k - 50, k + 50):
            target = k - d
            if target < 1 or target > 50 or d == 0:
                continue
            D = [0] * n
            for i, x in enumerate(nums):
                if x == target:
                    D[i] = 1
                elif x == k:
                    D[i] = -1
            s = mn = 0
            for x in D:
                s += x
                ans = max(ans, s - mn)
                mn = min(mn, s)
        return nums.count(k) + ans

sol = Solution()
print(sol.maxFrequency([1,2,3,4,5,6], 1)) # 2
print(sol.maxFrequency([10,2,3,4,5,5,4,3,2,2], 10)) # 4

print(sol.maxFrequency([2,3,7,1,7], 7)) # 4