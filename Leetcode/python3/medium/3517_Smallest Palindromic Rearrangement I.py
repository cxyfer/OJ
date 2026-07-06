#
# @lc app=leetcode id=3517 lang=python3
#
# [3517] Smallest Palindromic Rearrangement I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        ans = []
        mid = ""
        for c, val in enumerate(cnt):
            if val & 1:
                mid = chr(c + ord("a"))
            ans.append(chr(c + ord("a")) * (val // 2))
        ans = "".join(ans)
        return ans + mid + ans[::-1]


class Solution1b:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        # 因為題目確保給定的 s 也是回文，所以只需要統計前半段的字元數量即可
        cnt = [0] * 26
        for ch in s[: n // 2]:
            cnt[ord(ch) - ord("a")] += 1

        ans = []
        for c, val in enumerate(cnt):
            ans.append(chr(c + ord("a")) * val)

        ans = "".join(ans)
        mid = s[n // 2] if n & 1 else ""
        return ans + mid + ans[::-1]


# Solution = Solution1a
Solution = Solution1b
# @lc code=end

sol = Solution()
print(sol.smallestPalindrome("jjejj"))