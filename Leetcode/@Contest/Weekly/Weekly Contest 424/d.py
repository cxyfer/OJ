import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        max_diff = 0
        pre = None
        D_candidate = 0
        i = 0
        while i < n:
            if nums[i] != -1:
                if pre != None:
                    max_diff = max(max_diff, abs(nums[i] - pre))
                pre = nums[i]
                i += 1
            else:
                st = i
                while i < n and nums[i] == -1:
                    i += 1

                # 處理區段兩端的已知值
                left = pre
                right = nums[i] if i < n else None

                ln = i - st  # 區段中 -1 的數量

                if left is not None and right is not None:
                    diff = abs(left - right)
                    D_candidate = max(D_candidate, math.ceil((diff) / (ln + 1)))
                else:
                    D_candidate = max(D_candidate, 0)
                pre = nums[i] if i < n else None
        return max(max_diff, D_candidate)

sol = Solution()
print(sol.minDifference([1,2,-1,10,8]))  # 4
print(sol.minDifference([-1,-1,-1]))  # 0
print(sol.minDifference([-1,10,-1,8]))  # 1
print(sol.minDifference([14,-1,-1,46]))  # 11