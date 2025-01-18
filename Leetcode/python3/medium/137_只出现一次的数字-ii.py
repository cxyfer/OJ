#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
from preImport import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b1, b0 = 0, 0
        for num in nums:
            b0 = b0 ^ num & ~b1
            b1 = b1 ^ num & ~b0
        return b0
# @lc code=end

