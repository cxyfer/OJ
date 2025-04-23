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
    
class Solution3:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        mx = max(ch for ch in s)
        lst = [i for i, ch in enumerate(s) if ch == mx]
        if len(lst) == 1:
            return s[lst[0]:]
        i, j, k = lst[0], lst[1], 1
        while j < n:
            ln = 0
            while j + ln < n and s[j + ln] == s[i + ln]:
                ln += 1
            if j + ln < n and s[j + ln] > s[i + ln]:
                k = bisect_right(lst, max(j, i + ln))
                i, j = j, lst[k] if k < len(lst) else n
            else:
                k = bisect_right(lst, j + ln)
                j = lst[k] if k < len(lst) else n
        return s[i:]

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.lastSubstring("abab"))  # "bab"
print(sol.lastSubstring("leetcode"))  # "tcode"
print(sol.lastSubstring("cacacb"))  # "cb"

