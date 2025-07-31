#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
min = lambda x, y: x if x < y else y
class Solution:
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
# @lc code=end

sol = Solution()
print(sol.makeFancyString("aaabaaaa"))
print(sol.makeFancyString("aaabaaa"))
print(sol.makeFancyString("aaabaaaa"))
print(sol.makeFancyString("aaabaaaa"))