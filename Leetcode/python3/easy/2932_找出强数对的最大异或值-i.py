#
# @lc app=leetcode.cn id=2932 lang=python3
#
# [2932] 找出强数对的最大异或值 I
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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                x, y = nums[i], nums[j]
                if abs(x-y) <= min(x, y):
                    ans = max(ans, x^y)
        return ans
# @lc code=end

