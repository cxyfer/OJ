#
# @lc app=leetcode id=633 lang=python3
# @lcpr version=30203
#
# [633] Sum of Square Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    1. Enumeration
    2. Two pointers
"""

class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        for x in range(int(c**0.5)+1):
            # 也可以用 double y，然後判斷 y == int(y)
            y = int((c - x**2)**0.5)
            if x ** 2 + y ** 2 == c:
                return True
        return False

class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            cur = left**2 + right**2
            if cur == c:
                return True
            elif cur < c: # 太小
                left += 1
            else: # 太大
                right -= 1
        return False

# class Solution(Solution1):
#     pass
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

