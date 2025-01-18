3#
# @lc app=leetcode.cn id=1334 lang=python3
#
# [1334] 阈值距离内邻居最少的城市
#
from preImport import *
# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        w = [[inf] * n for _ in range(n)]
        for x, y, wt in edges:
            w[x][y] = w[y][x] = wt

        @cache # memoization
        def dfs(k: int, i: int, j: int) -> int:
            if k < 0: # base case
                return w[i][j]
            return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))

        ans = 0
        min_cnt = inf
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j != i and dfs(n - 1, i, j) <= distanceThreshold:
                    cnt += 1
            if cnt <= min_cnt: # min_cnt相等時，取最大的i
                min_cnt = cnt
                ans = i
        return ans
# @lc code=end

