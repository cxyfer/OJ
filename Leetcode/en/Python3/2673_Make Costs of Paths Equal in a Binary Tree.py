# @algorithm @lc id=2780 lang=python3 
# @title make-costs-of-paths-equal-in-a-binary-tree


from en.Python3.mod.preImport import *
# @test(7,[1,5,2,2,3,3,1])=6
# @test(3,[5,3,3])=0
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
            if i > n:
                return 0
            l = dfs(2 * i)
            r = dfs(2 * i + 1)
            ans += abs(l - r) # 讓左右子樹的路徑和相等的最小代價
            return max(l, r) + cost[i - 1] # 編號從 1 開始
        dfs(1)
        return ans
    def solve2(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1): # 從最後一個internal node開始, i * 2 < n -> i <= n // 2
            ans += abs(cost[i * 2 - 1] - cost[i * 2]) # 讓左右子樹的路徑和相等的最小代價
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2]) # 累加路徑和
        return ans