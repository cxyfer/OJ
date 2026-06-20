#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[-1] += 1
        i = n - 1
        while i >= 0:
            if digits[i] < 10:
                break
            digits[i] -= 10
            if i == 0:
                digits.insert(0, 1)
                break
            digits[i - 1] += 1
            i -= 1
        return digits
# @lc code=end

