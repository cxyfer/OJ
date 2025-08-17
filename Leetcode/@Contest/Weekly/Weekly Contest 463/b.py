import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import xor

from typing import List

MOD = int(1e9 + 7)

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        return reduce(xor, nums, 0)

sol = Solution()
print(sol.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]]))  # 4
print(sol.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))  # 31