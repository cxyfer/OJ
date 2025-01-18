#
# @lc app=leetcode id=2981 lang=python3
# @lcpr version=30202
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Easy Version of 2982. Find Longest Special Substring That Occurs Thrice II
         - n <= 50
    """
    def maximumLength(self, s: str) -> int:
        n = len(s)
        cnt = [[0] * (n+1) for _ in range(26)]
        for i in range(n): # 枚舉 substring 的起點和終點
            for j in range(i, n):
                for k in range(i+1, j+1):
                    if s[k] != s[i]:
                        break
                else:
                    cnt[ord(s[i])-ord('a')][j-i+1] += 1
        ans = -1
        for i in range(26):
            for j in range(n, 0, -1):
                if cnt[i][j] >= 3:
                    ans = max(ans, j)
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

