#
# @lc app=leetcode id=3448 lang=python3
# @lcpr version=30204
#
# [3448] Count Substrings Divisible By Last Digit
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        # 令 f[i+1][m][r] 表示以 s[i] 結尾，mod m 餘數為 r 的子字串個數
        f = [[0] * 9 for _ in range(10)]
        for ch in s:
            d = int(ch)
            nf = [[0] * 9 for _ in range(10)]
            for m in range(1, 10):
                nf[m][d % m] += 1  # s[i] 本身
                for r in range(m):
                    nf[m][(r * 10 + d) % m] += f[m][r]  # 從 f[i][m][r] 轉移
            f = nf
            ans += f[d][0]  # 以 s[i] 結尾，mod s[i] 餘數為 0 的子字串個數
        return ans
# @lc code=end

#
# @lcpr case=start
# "12936"\n
# @lcpr case=end

# @lcpr case=start
# "5701283"\n
# @lcpr case=end

# @lcpr case=start
# "1010101010"\n
# @lcpr case=end

#

