#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
輾轉相除法，類似求 gcd 的過程。
"""
# @lc code=start
class Solution1:
    def countOperations(self, num1: int, num2: int) -> int:
        def f(a: int, b: int) -> int:
            if b == 0:
                return 0
            return a // b + f(b, a % b)
        return f(num1, num2)

class Solution2:
    def countOperations(self, a: int, b: int) -> int:
        ans = 0
        while b > 0:
            ans += a // b
            a, b = b, a % b
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end