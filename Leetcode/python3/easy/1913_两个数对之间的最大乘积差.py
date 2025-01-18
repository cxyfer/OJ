#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#
from preImport import *
# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1, mx2 = float('-inf'), float('-inf')
        mn1, mn2 = float('inf'), float('inf')
        for num in nums:
            if num > mx1:
                mx1, mx2 = num, mx1
            elif num > mx2:
                mx2 = num
            if num < mn1:
                mn1, mn2 = num, mn1
            elif num < mn2:
                mn2 = num
        return mx1 * mx2 - mn1 * mn2
# @lc code=end

