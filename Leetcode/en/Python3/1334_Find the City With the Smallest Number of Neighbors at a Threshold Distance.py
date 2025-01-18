# @algorithm @lc id=1456 lang=python3 
# @title find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance


from en.Python3.mod.preImport import *
# @test(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4)=3
# @test(5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2)=0
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