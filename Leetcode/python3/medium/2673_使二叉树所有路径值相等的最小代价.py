#
# @lc app=leetcode.cn id=2673 lang=python3
#
# [2673] 使二叉树所有路径值相等的最小代价
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy
        1. Top-Down
        2. Bottom-Up
    """
    def minIncrements(self, n: int, cost: List[int]) -> int:
        return self.solve1(n, cost)
        # return self.solve2(n, cost)
    def solve1(self, n: int, cost: List[int]) -> int:
        ans = 0
        def dfs(i: int) -> int: # 表示節點 i 以下的最大路徑和
            nonlocal ans
            # if i > n: return 0
            if 2 * i > n: return cost[i - 1] # leaf node
            l = dfs(2 * i)
            r = dfs(2 * i + 1)
            ans += abs(l - r) # 讓左右子樹的路徑和相等的最小代價
            return max(l, r) + cost[i - 1] # 編號從 1 開始
        dfs(1)
        return ans
    def solve2(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1): # 從最後一個internal node開始
            ans += abs(cost[i * 2 - 1] - cost[i * 2]) # 讓左右子樹的路徑和相等的最小代價
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2]) # 累加路徑和
        return ans
# @lc code=end

