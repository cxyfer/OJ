#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def rotateString(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        s += s
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and t[i] != t[ln]:
                ln = pi[ln - 1]
            if t[i] == t[ln]:
                ln += 1
            pi[i] = ln
        ln = 0
        for i in range(2 * n):
            while ln and s[i] != t[ln]:
                ln = pi[ln - 1]
            if s[i] == t[ln]:
                ln += 1
            if ln == m:
                return True
        return False

class Solution2:
    def rotateString(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        s = t + "#" + s + s
        n = len(s)
        pi = [0] * n
        ln = 0
        for i in range(1, n):
            while ln and s[i] != s[ln]:
                ln = pi[ln - 1]
            if s[i] == s[ln]:
                ln += 1
            if ln == m:
                return True
            pi[i] = ln
        return False

Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.rotateString("aa", "a")) # False