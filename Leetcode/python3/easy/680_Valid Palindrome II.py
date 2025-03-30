#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def validPalindrome(self, s: str) -> bool:
        def helper(i, j, used = False):
            while i < j:
                if s[i] != s[j]:
                    if used:
                        return False
                    return helper(i + 1, j, True) or helper(i, j - 1, True)
                i += 1
                j -= 1
            return True
        return helper(0, len(s) - 1, False)
    
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        def dfs(i, j, used = False):
            if i >= j:
                return True
            if s[i] != s[j]:
                if used:
                    return False
                return dfs(i + 1, j, True) or dfs(i, j - 1, True)
            return dfs(i + 1, j - 1, used)
        return dfs(0, len(s) - 1, False)
    
Solution = Solution1
# Solution = Solution2
# @lc code=end

