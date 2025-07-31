#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
分組循環
"""
# @lc code=start
min = lambda x, y: x if x < y else y
class Solution1:
    def makeFancyString(self, s: str) -> str:
        # return "".join(c * min(2, len(list(g))) for c, g in groupby(s))
        n = len(s)
        ans = ""
        i = 0
        while i < n:
            j = i
            while i < n and s[i] == s[j]:
                i += 1
            ans += min(2, i - j) * s[j]
        return ans
    
class Solution2:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            if i < 2 or s[i] != s[i - 1] or s[i] != s[i - 2]:
                ans += s[i]
        return ans
    
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.makeFancyString("aaabaaaa"))
print(sol.makeFancyString("aaabaaa"))
print(sol.makeFancyString("aaabaaaa"))
print(sol.makeFancyString("aaabaaaa"))