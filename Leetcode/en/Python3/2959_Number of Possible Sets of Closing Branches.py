# @algorithm @lc id=3217 lang=python3 
# @title number-of-possible-sets-of-closing-branches


from en.Python3.mod.preImport import *
# @test(3,5,[[0,1,2],[1,2,10],[0,2,10]])=5
# @test(3,5,[[0,1,20],[0,1,10],[1,2,2],[0,2,2]])=7
# @test(1,10,[])=2
class Solution:
    """
        Floyd-Warshall
    """
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        # 建圖只要一次
        g = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, w in roads:
            g[x][y] = min(g[x][y], w)
            g[y][x] = min(g[y][x], w)

        ans = 0
        g2 = [None] * n # subgraph
        for mask in range(1 << n):
            # Copy subgraph
            for i, row in enumerate(g):
                if mask >> i & 1: # 這個點在子圖裡
                    g2[i] = row[:] # copy

            # Floyd-Warshall
            for k in range(n):
                if (mask >> k & 1) == 0: continue # k 不在子圖裡
                for i in range(n):
                    if (mask >> i & 1) == 0: continue # i 不在子圖裡
                    for j in range(n):
                        if g2[i][k] + g2[k][j] < g2[i][j]:
                            g2[i][j] = g2[i][k] + g2[k][j]
            # Check
            flag = True
            for i in range(n):
                if (mask >> i & 1) == 0: continue # i 不在子圖裡
                for j in range(n):
                    if (mask >> j & 1) == 0: continue # j 不在子圖裡
                    if g2[i][j] > maxDistance:
                        flag = False
                        break
            if flag:
                ans += 1
        return ans