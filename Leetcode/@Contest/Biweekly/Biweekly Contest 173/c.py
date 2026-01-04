import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
a[i] - diff[i] <= a[i + 1] <= a[i] + diff[i]
"""
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        ans = [float("inf")] * n
        for idx, x in restrictions:
            ans[idx] = x
        ans[0] = 0

        for i in range(n - 1):
            ans[i + 1] = min(ans[i + 1], ans[i] + diff[i])
        for i in range(n - 1, 0, -1):
            ans[i - 1] = min(ans[i - 1], ans[i] + diff[i - 1])
        return max(ans)


sol = Solution()
print(sol.findMaxVal(10, [[3,1],[8,1]], [2,2,3,1,4,5,1,1,2]))  # 6