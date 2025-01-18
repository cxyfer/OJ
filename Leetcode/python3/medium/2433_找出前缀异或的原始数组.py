#
# @lc app=leetcode.cn id=2433 lang=python3
#
# [2433] 找出前缀异或的原始数组
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
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        a ^ a = 0
        b ^ 0 = b
    """
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
# @lc code=end
sol = Solution()
print(sol.findArray([5,2,0,3,1]))

