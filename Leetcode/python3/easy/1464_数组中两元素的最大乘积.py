#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#
from preImport import *
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1 = mx2 = -1
        for num in nums:
            if num > mx1:
                mx1, mx2 = num, mx1
            elif num > mx2:
                mx2 = num
        return (mx1 - 1) * (mx2 - 1)
# @lc code=end

