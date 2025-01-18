#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while (left <= right): # [left, right]
            middle = left + (right-left)//2
            if middle*middle == num:
                return True
            elif middle*middle < num:
                left = middle + 1
            else:
                right = middle - 1
        return False
# @lc code=end

