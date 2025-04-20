import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f = [[0] * k for _ in range(n + 1)]
        for i, v in enumerate(nums, 1):
            m = v % k
            for j in range(k):
                f[i][(j * m) % k] += f[i-1][j]
            f[i][m] += 1
        return [sum(f[i][j] for i in range(n+1)) for j in range(k)]


sol = Solution()
print(sol.resultArray([1,2,3,4,5], 3))  # [9,2,4]
