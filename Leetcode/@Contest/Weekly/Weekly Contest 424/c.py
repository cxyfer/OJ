import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)

        def check(k):
            diff = [0] * (n + 1)
            for l, r, val in queries[:k]:
                diff[l] += val
                diff[r + 1] -= val
            tot = 0
            for i in range(n):
                tot += diff[i]
                if tot < nums[i]:
                    return False
            return True

        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= m else -1

sol = Solution()
print(sol.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]])) # 2
print(sol.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]])) # -1
print(sol.minZeroArray([0], [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]])) # 0
