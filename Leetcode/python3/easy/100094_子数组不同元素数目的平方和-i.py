#
# @lc app=leetcode.cn id=100094 lang=python3
#
# [100094] 子数组不同元素数目的平方和 I
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
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(1, n+1):
            for i in range(n-l+1):
                ans += len(set(nums[i:i+l]))** 2
        return ans
# @lc code=end
sol = Solution()
print(sol.sumCounts([1,2,1])) # 15

