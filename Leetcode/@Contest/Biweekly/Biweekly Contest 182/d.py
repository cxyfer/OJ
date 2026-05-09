import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q4: ||二分答案 + 01BFS||
顯然當兩點連通且所有邊都是 light edge 的情況下，此時的代價為 0，故一定能到達。
而隨著 threshold 不斷變小，light edge 會被逐漸轉為需要代價的 heavy edge，此時代價會不斷變大，就可能無法到達。
故若 threshold 為 t 時能到達，則 threshold 為 t' > t 時也一定能到達；反之若 threshold 為 t 時無法到達，則 threshold 為 t' < t 時也一定無法到達。
因此能否到達具有單調性，故可以用二分答案來解決。

由於代價只有 0 和 1，所以我們可以使用 01BFS，用 Dijkstra 應該也是可以的。
不過恰好昨天下午在隔壁提到了 01BFS，所以就寫了 01BFS 。
https://discord.com/channels/1241949323240018041/1352562364016365628/1502261184433492038

這題最傻逼的地方是 edges 的長度居然可能為 0。
"""

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], st: int, ed: int, k: int) -> int:
        if st == ed:
            return 0
        if not edges:
            return -1

        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def check(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[st] = 0

            q = deque([st])
            while q:
                u = q.popleft()
                for v, w in g[u]:
                    c = 1 if w > mid else 0
                    nd = dist[u] + c
                    if nd < dist[v] and nd <= k:
                        dist[v] = nd
                        if c == 0:
                            q.appendleft(v)
                        else:
                            q.append(v)
            return dist[ed] <= k

        max_w = max(w for _, _, w in edges)
        left, right = 0, max_w
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= max_w else -1

sol = Solution()
print(sol.minimumThreshold(6, [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], 0, 3, 1))  # 4
print(sol.minimumThreshold(6, [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], 0, 4, 1))  # -1
print(sol.minimumThreshold(4, [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], 0, 0, 0))  # 0