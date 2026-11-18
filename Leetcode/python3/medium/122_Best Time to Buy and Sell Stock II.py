#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Greedy
可以無限次交易，且同一天允許先賣再買，所以任何一段上漲都能完整吃到
因此只要把相鄰兩天的正價差全部加總即可
O(n)

2. 狀態機 DP
令 f[i][j] 表示前 i 天（第 i 天結束後）的狀態，j = 0 表示不持有股票，j = 1 表示持有股票
- f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-1])  # 繼續不持有 / 今天賣出
- f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i-1])  # 繼續持有 / 今天買入
初始 f[0][0] = 0, f[0][1] = -inf（第 0 天不可能持有股票）
答案為 f[n][0]，最後一天不持有股票一定不劣於持有
O(n)

2a. 遞迴 + 記憶化：dfs(i, hold) 表示考慮前 i+1 天、第 i 天結束後是否持股的最大收益
2b. 迭代：轉移式與 2a 相同，只是改成由前往後填表
2c. 空間優化：f[i] 只依賴 f[i-1]，用兩個變數滾動即可，O(1) 空間
"""
# @lc code=start
class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(b - a, 0) for a, b in pairwise(prices))


class Solution2a:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        # dfs(i, hold) 表示在第 i 天，是否持有股票的最大收益
        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if not hold:  # 繼續前一天的未持有、或前一天持有但今天賣出
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
            else:  # 繼續前一天的持有、或前一天未持有但今天買入
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])

        return dfs(n - 1, False)  # 最終是不持有股票的狀態


class Solution2b:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf
        for i, p in enumerate(prices, 1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + p)
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - p)
        return f[n][0]


class Solution2c:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            # 注意這裡需要同時更新 f0 和 f1
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0


# Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
Solution = Solution2c
# @lc code=end

