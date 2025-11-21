#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        return (s := str(x)) == s[::-1]

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or x > 0 and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10

# Solution = Solution1
Solution = Solution2
# @lc code=end

