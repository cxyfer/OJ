#
# @lc app=leetcode.cn id=100102 lang=python3
#
# [100102] 数组的最小相等和
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
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)
        if sum1 == sum2:
            if zero1 == zero2:
                return sum1 + zero1
            elif zero1 == 0 or zero2 == 0:
                return -1
            else:
                return sum1 + max(zero1, zero2)
        elif sum1 > sum2:
            if zero2 == 0:
                return -1
            elif zero1 == 0 and sum2 + zero2 > sum1:
                return -1
            else:
                return max(sum1+zero1, sum2+zero2)
        else:
            if zero1 == 0:
                return -1
            elif zero2 == 0 and sum1 + zero1 > sum2:
                return -1
            else:
                return max(sum1+zero1, sum2+zero2)
# @lc code=end
sol = Solution()
print(sol.minSum([3,2,0,1,0], [6,5,0])) # 12
print(sol.minSum([2,0,2,0], [1,4])) # -1
print(sol.minSum([20,0,18,11,0,0,0,0,0,0,17,28,0,11,10,0,0,15,29], [16,9,25,16,1,9,20,28,8,0,1,0,1,27])) # 169
