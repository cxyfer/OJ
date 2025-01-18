# @algorithm @lc id=2979 lang=python3 
# @title maximize-the-profit-as-the-salesman


from en.Python3.mod.preImport import *
from typing import List
from math import inf
# @test(5,[[0,0,1],[0,2,2],[1,3,2]])=3
# @test(5,[[0,0,1],[0,2,10],[1,3,2]])=10
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # DP
        # Maintain a dict to previos possible offers
        prev = [[] for _ in range(n+1)]
        for st, ed, gd in offers:
            prev[ed+1].append((st, ed, gd))
        # def helper(idx, offers):
        #     # Find previos possible offers that can be combined with current offer
        #     for i in range(idx, -1, -1):
        #         if offers[i][1] < offers[idx][0]:
        #             return i+1
        #     return 0
        dp = [0] * (n+1)
        for i in range(1, n+1):
            # pre = helper(i-1, offers) # If select i-th offer, find previous possible offer
            # dp[i] = max(dp[i-1], dp[pre] + offers[i-1][2])
            dp[i] = max(dp[i], dp[i - 1])
            for st, ed, gd in prev[i]:
                dp[i] = max(dp[i], dp[st] + gd)
        return dp[-1]