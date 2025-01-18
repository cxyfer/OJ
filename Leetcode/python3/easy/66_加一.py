#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from preImport import *
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits # 避免進位
        n = len(digits)
        last = n-1
        digits[last] += 1
        while digits[last] >= 10:
            digits[last] -= 10
            last -= 1
            digits[last] += 1
        if digits[0] == 0:
            digits = digits[1:]
        return digits
# @lc code=end

