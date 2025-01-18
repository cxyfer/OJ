#
# @lc app=leetcode.cn id=2370 lang=python3
#
# [2370] 最长理想子序列
#

# @lc code=start
class Solution:
    """
        DP - LIS

        令 dp[i][j] 表示以第 i 個字符為結尾，且字符為 j 的最長理想子序列
        - dp[i][j] = dp[i-1][j] (if j != s[i])
        - max(dp[i-1][k] + 1) (if j == s[i] and k in [max(0, x-k), min(26, x+k+1)) )
        可以壓縮空間複雜度為 O(26)
    """
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        # dp = [[0] * 26 for _ in range(n+1)] # dp[i][j] 表示以第 i 個字符為結尾，且字符為 j 的最長理想子序列
        # for i, ch in enumerate(s):
        #     x = ord(ch) - ord('a')
        #     for j in range(26):
        #         dp[i+1][j] = dp[i][j]
        #     for j in range(max(0, x-k), min(26, x+k+1)):
        #         dp[i+1][x] = max(dp[i+1][x], dp[i][j] + 1)
        # return max(dp[n])
        dp = [0] * 26
        for i in range(n):
            x = ord(s[i]) - ord('a')
            mx = 0
            for j in range(max(0, x-k), min(26, x+k+1)):
                mx = max(mx, dp[j])
            dp[x] = mx + 1
        return max(dp)
# @lc code=end
# @test("acfgbd",2)=4
# @test("abcd",3)=4
sol = Solution()
print(sol.longestIdealString("acfgbd", 2)) # 4
print(sol.longestIdealString("abcd", 3)) # 4
