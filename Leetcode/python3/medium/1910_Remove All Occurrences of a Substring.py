#
# @lc app=leetcode id=1910 lang=python3
# @lcpr version=30204
#
# [1910] Remove All Occurrences of a Substring
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Built-in function
2. Stack
3. KMP
"""
# @lc code=start
class Solution1:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s
    
class Solution2:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        st = []
        for ch in s:
            st.append(ch)
            if len(st) >= m and ''.join(st[-m:]) == part:
                st[-m:] = []
        return ''.join(st)
    
class Solution3:
    def removeOccurrences(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and t[i] != t[ln]:
                ln = pi[ln - 1]
            if t[i] == t[ln]:
                ln += 1
            pi[i] = ln
        ans = [''] * n
        pi2 = [0] * (n + 1)
        sz = 0
        for ch in s:
            ans[sz] = ch
            ln = pi2[sz]
            sz += 1
            while ln and ch != t[ln]:
                ln = pi[ln - 1]
            if ch == t[ln]:
                ln += 1
            pi2[sz] = ln
            if ln == m:
                sz -= m
        return ''.join(ans[:sz])

class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.removeOccurrences("aabababa", "aba")) # ba

#
# @lcpr case=start
# "daabcbaabcbc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "axxxxyyyyb"\n"xy"\n
# @lcpr case=end

#

