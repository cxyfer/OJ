#
# @lc app=leetcode id=1163 lang=python3
#
# [1163] Last Substring in Lexicographical Order
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def lastSubstring(self, s: str) -> str:
        mx = max(ch for ch in s)
        return max(s[i:] for i, ch in enumerate(s) if ch == mx)

class Solution2:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j = 0, 1
        while j < n:
            ln = 0
            while j + ln < n and s[j + ln] == s[i + ln]:
                ln += 1
            if j + ln < n and s[j + ln] > s[i + ln]:
                i, j = j, max(j + 1, i + ln + 1)
            else:
                j = j + ln + 1
        return s[i:]
    
Solution = Solution2
# @lc code=end

