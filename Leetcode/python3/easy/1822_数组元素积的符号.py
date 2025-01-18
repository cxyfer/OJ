#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#
from preImport import *
# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                ans = 0
                break
            elif num < 0:
                ans *= -1
        return ans
# @lc code=end

