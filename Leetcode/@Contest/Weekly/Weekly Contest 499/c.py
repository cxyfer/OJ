import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import *

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # return sum(max(x - y, 0) for x, y in pairwise(nums))
        n = len(nums)
        ans = s = 0
        for i in range(1, n):
            nums[i] += s
            # 貪心：如果需要讓 nums[i] 增加 x，那麼 nums[i...n-1] 都增加 x 也不會影響結果
            # 用差分的思想來維護，但由於區間右端點一定是 n-1，所以不用維護右端點
            if nums[i] < nums[i - 1]:
                a = nums[i - 1] - nums[i]
                s += a
                nums[i] += a
                ans += a
        return ans

sol = Solution()
print(sol.minOperations(nums = [3,3,2,1]))  # 2