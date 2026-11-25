#
# @lc app=leetcode id=2981 lang=python3
# @lcpr version=30202
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Easy Version of 2982. Find Longest Special Substring That Occurs Thrice II
    - n <= 50
"""
# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # cnt[c][ln] 表示全為字母 c 且長度為 ln 的子字串的出現次數
        cnt = [[0] * (n + 1) for _ in range(26)]
        for i in range(n):  # 枚舉 substring 的起點和終點
            c = ord(s[i]) - ord("a")
            for j in range(i, n):
                if s[j] != s[i]:
                    break
                cnt[c][j - i + 1] += 1
        ans = -1
        for c in range(26):
            for ln in range(n, 0, -1):
                if cnt[c][ln] >= 3:
                    ans = max(ans, ln)
                    break
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumLength("aaaa")) # 2
print(sol.maximumLength("abcdef")) # -1
print(sol.maximumLength("abcaba")) # 1

#
# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

# @lcpr case=start
# "abcaba"\n
# @lcpr case=end

#

