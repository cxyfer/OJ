# @algorithm @lc id=2351 lang=python3 
# @title number-of-ways-to-buy-pens-and-pencils


from en.Python3.mod.preImport import *
# @test(20,10,5)=9
# @test(5,10,10)=1
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # """
        #     Dynamic Programming
        #     Unbounded Knapsack Problem
        # """
        # # dp[i][j] 表示前考慮前i個物品，且花費最多為j的方案數
        # dp = [[0] * (total + 1) for _ in range(3)] 
        # items = [cost1, cost2]
        # for j in range(total+1): # 從0件物品中選，總花費不超過j的方案數為1 (甚麼都不選)
        #     dp[0][j] = 1
        # for i in range(1, 3):
        #     for j in range(total+1):
        #         cost = cost1 if i == 1 else cost2
        #         # 不選第i個物品 + 選第i個物品
        #         dp[i][j] = (dp[i-1][j] + dp[i][j-cost]) if j >= items[i-1] else dp[i-1][j] 
        # return dp[2][total]
        """
            Greedy
            枚舉鋼筆(cost1)數量，計算鉛筆(cost2)數量
        """
        n = 1 + total // cost1
        return sum((total - cost1 * i) // cost2 + 1 for i in range(n))

