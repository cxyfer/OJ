import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

"""
Q4. 樹狀DP

令 f0(u) 表示 u 不與 fa 連接能獲得的最大權重，f1(u) 表示 u 與 fa 連接能獲得的最大權重。
則對於 u 的每個子節點 v，可以先假設不保留 (u, v)，故無論如何都可以獲得 f0(v)。
再考慮需不需要保留 (u, v) 這條邊，可以計算保留相較不保留所能獲得的收益為 w + f1(v) - f0(v)。

接著考慮能保留的邊數：
- 與 fa 連接時，最多可以保留 k-1 條邊
- 不與 fa 連接時，最多可以保留 k 條邊

基於貪心思路，在這些收益中，從收益最大的邊開始保留，且只需要考慮正收益的邊，直到達到 k 或 k-1 條邊為止。
"""
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        # f0: 不與 fa 連接能獲得的最大權重
        # f1: 與 fa 連接能獲得的最大權重
        def dfs(u: int, fa: int) -> Tuple[int, int]:
            f0, f1 = 0, 0
            gains = []
            for v, w in g[u]:
                if v == fa:
                    continue
                g0, g1 = dfs(v, u)
                f0 += g0
                f1 += g0
                gain = w + g1 - g0 # 相較於不保留 (u, v) ，保留 (u, v) 能獲得的收益
                if gain > 0: # 只考慮正收益
                    gains.append(gain)
            gains.sort(reverse=True)
            f0 += sum(gains[:k]) # 不與 fa 連接時，最多可以保留 k 條邊
            f1 += sum(gains[:k - 1]) # 與 fa 連接時，最多可以保留 k-1 條邊
            return f0, f1

        return max(dfs(0, -1))

sol = Solution()
print(sol.maximizeSumOfWeights([[0,1,4],[0,2,2],[2,3,12],[2,4,6]], 2)) # 22
print(sol.maximizeSumOfWeights([[0,1,5],[1,2,10],[0,3,15],[3,4,20],[3,5,5],[0,6,10]], 3)) # 65
print(sol.maximizeSumOfWeights([[0,1,14],[0,3,44],[3,2,37]], 1)) # 51
print(sol.maximizeSumOfWeights([[0,1,17],[1,3,27],[3,2,30]], 1)) # 47
