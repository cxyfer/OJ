#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # dfs(i, j, hold) 表示在第 i 天，最多進行 j 次交易，是否持有股票的最大收益
        @cache
        def dfs(i: int, j: int, hold: bool) -> int:
            if i < 0 or j == 0:
                return -inf if hold else 0
            if not hold:  # 繼續前一天的未持有、或前一天持有但今天賣出
                return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
            # 繼續前一天的持有、或前一天未持有但今天買入，買入時計算交易次數
            return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])

        return dfs(n - 1, k, False)


class Solution1b:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[0, -inf] for _ in range(k + 1)] for _ in range(n + 1)]
        for i, p in enumerate(prices, 1):
            for j in range(1, k + 1):
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1] + p)
                f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - p)
        return f[n][k][0]


class Solution1c:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f = [[0, -inf] for _ in range(k + 1)]
        for p in prices:
            for j in range(1, k + 1):
                # 因為沒使用到 f[j][0] 的前一個狀態，所以可以直接覆蓋，不用同時更新
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
        return f[k][0]


# Solution = Solution1a
# Solution = Solution1b
Solution = Solution1c
# @lc code=end

sol = Solution()
print(sol.maxProfit(2,  [3,2,6,5,0,3]))  # Output: 7