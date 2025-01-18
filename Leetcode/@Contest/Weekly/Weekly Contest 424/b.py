import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * n

        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        
        cnt = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            cnt[i] = cur
        
        return all(x <= y for x, y in zip(nums, cnt))

sol = Solution()
print(sol.isZeroArray([1,0,1], [[0,2]])) # true
print(sol.isZeroArray([4,3,2,1], [[1,3],[0,2]])) # false
