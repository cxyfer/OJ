#
# @lc app=leetcode id=344 lang=python3
# @lcpr version=30203
#
# [344] Reverse String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # self.solve1(s)
        self.solve2(s)
    def solve1(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
    def solve2(self, s: List[str]) -> None:
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

