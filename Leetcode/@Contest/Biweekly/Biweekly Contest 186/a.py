import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt = Counter(nums)
        return cnt[nums[n // 2]] == 1


sol = Solution()
print(sol.isMiddleElementUnique([1, 2, 3]))  # true
print(sol.isMiddleElementUnique([1, 2, 2]))  # false
