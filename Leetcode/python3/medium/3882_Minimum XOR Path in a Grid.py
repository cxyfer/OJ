#
# @lc app=leetcode id=3882 lang=python3
#
# [3882] Minimum XOR Path in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
賽時寫了很暴力的DP，dfs(i, j) 維護了到達 (i, j) 位置時的所有可能 XOR 值。

注意到值域只有 2^10，而 XOR 的結果不會超出值域範圍。
因此只要記錄到達每個位置時的所有可能 XOR 值 即可。
時空複雜度均為 O(nmV)，但用滾動的方式應該可以把空間複雜度優化到 O(mV)。

也可以令 dfs(i, j, s) 為到達 (i, j) 位置時的 XOR 值為 s 的最小代價，
則有 dfs(i, j, s) = min(dfs(i - 1, j, s ^ grid[i][j]), dfs(i, j - 1, s ^ grid[i][j]))。

也能用網格圖DFS理解，dfs(i, j, s) 表示到達 (i, j) 位置時的 XOR 值為 s ，
則只要從 (0, 0) 開始 DFS 到 (n - 1, m - 1) 位置，並在到達 (n - 1, m - 1) 位置時更新答案即可。
另外也可以用一個 vis 陣列來記錄已經訪問過的位置，避免重複訪問同一個位置。
這種做法的好處是可以在已知 ans 到達最小值時停止 DFS，避免不必要的遞迴。
"""
class Solution1:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> set:
            x = grid[i][j]
            if i == 0 and j == 0:
                return set([x])
            res = set()
            if i > 0:
                for y in dfs(i - 1, j):
                    res.add(x ^ y)
            if j > 0:
                for y in dfs(i, j - 1):
                    res.add(x ^ y)
            return res

        return min(dfs(n - 1, m - 1))


class Solution2:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i, j, s):
            if i < 0 or j < 0:
                return float("inf")
            s ^= grid[i][j]
            if i == 0 and j == 0:
                return s
            return min(dfs(i - 1, j, s), dfs(i, j - 1, s))

        ans = dfs(n - 1, m - 1, 0)
        dfs.cache_clear()
        return ans


class Solution3:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        ans = float("inf")
        vis = set()

        def dfs(i: int, j: int, xor: int) -> None:
            nonlocal ans
            if ans == 0 or (i, j, xor) in vis:  # 剪枝
                return
            vis.add((i, j, xor))
            xor ^= grid[i][j]
            if i == n - 1 and j == m - 1:
                ans = min(ans, xor)
                return
            if i + 1 < n:
                dfs(i + 1, j, xor)
            if j + 1 < m:
                dfs(i, j + 1, xor)

        dfs(0, 0, 0)
        vis.clear()  # 避免 MLE
        return ans


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

