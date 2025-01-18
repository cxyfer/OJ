#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    """
        2D DP
    """
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[i][j] 表示第 i 行第 j 列的香檳量
        dp = [[0] * (query_row + 2) for _ in range(query_row + 2)]
        dp[0][0] = poured # 初始倒入的香檳
        # 由上往下遍歷，考慮每個杯子的溢出情況
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1: # 溢出
                    half = (dp[i][j] - 1) / 2 # 溢出的部分
                    dp[i][j] = 1 # 剩餘的部分
                    dp[i+1][j] += half
                    dp[i+1][j+1] += half
        return dp[query_row][query_glass]
# @lc code=end

