#
# @lc app=leetcode id=3612 lang=python3
#
# [3612] Process String with Special Operations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch == '*':
                if ans:
                    ans.pop()
            elif ch == '#':
                ans += ans
            elif ch == '%':
                ans.reverse()
            else:
                ans.append(ch)
        return ''.join(ans)
# @lc code=end

