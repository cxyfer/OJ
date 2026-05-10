import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from typing import List

"""
Q3: ||調和級數||
注意值域，nums[i] <= 1e5 。
如果 x 存在於 nums 中，那麼 2x, 3x, 4x, ... 都可以被替換成 x。
直接標記所有 x 的倍數，時間複雜度為可以寫成調和級數的形式。
n/1 + n/2 + n/3 + ... + n/n = O(n log n)。
"""

class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        U = max(nums)
        f = [float("inf")] * (U + 1)
        vis = set()
        for x in nums:
            if x in vis:
                continue
            vis.add(x)
            for y in range(x, U + 1, x):
                f[y] = min(f[y], x)
        return sum(f[x] for x in nums)

sol = Solution()
print(sol.minArraySum([3,6,2]))  # 7