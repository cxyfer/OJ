#
# @lc app=leetcode.cn id=458 lang=python3
#
# [458] 可怜的小猪
#


# @lcpr-template-start
import math
from math import *
from typing import *
from collections import *
from functools import *
from itertools import *
from bisect import *
from heapq import *
from decimal import Decimal
# @lcpr-template-end
# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # base ^ ans >= buckets
        # ans >= log(buckets) / log(base)
        times = minutesToTest // minutesToDie # 測試次數
        base = times + 1 # 每頭豬可以測試的桶數
        # log的精準度問題
        # print(math.log(buckets), math.log(base), math.log(buckets) / math.log(base))
        # print(math.log10(buckets), math.log10(base), math.log10(buckets) / math.log10(base))
        return math.ceil(math.log10(buckets) / math.log10(base))
# @lc code=end

sol = Solution()
print(sol.poorPigs(1000, 15, 60)) # 5
print(sol.poorPigs(4, 15, 15)) # 2
print(sol.poorPigs(4, 15, 30)) # 2
print(sol.poorPigs(125, 1, 4)) # 3