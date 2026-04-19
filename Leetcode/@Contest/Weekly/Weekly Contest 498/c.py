import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import *

"""
BFS
在答案之外，維護每個格子被塗色的時間，如果遇到尚未被塗色的格子，則直接塗色，如果遇到已經被塗色的格子，則更新為更大的值。
需要注意的地方：
1. 實際上顏色可能會因後續塗色而改變，因此不應將顏色也放入 queue 中。
2. 相同時間塗色的格子仍只應被推入 queue 一次，因此在遇到相同時間塗色的格子時，只應更新為更大的值。
"""

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        ans = [[0] * m for _ in range(n)]
        vis = [[-1] * m for _ in range(n)]
        
        q = deque()
        for r, c, v in sources:
            ans[r][c] = v
            vis[r][c] = 0
            q.append((r, c, 0))

        while q:
            r, c, t = q.popleft()
            v = ans[r][c]
            nt = t + 1
            for nx, ny in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if vis[nx][ny] == -1:
                        ans[nx][ny] = v
                        vis[nx][ny] = nt
                        q.append((nx, ny, nt))
                    elif vis[nx][ny] == nt:
                        ans[nx][ny] = max(ans[nx][ny], v)
        return ans

sol = Solution()
print(sol.colorGrid(3, 3, [[0,0,1],[2,2,2]]))
print(sol.colorGrid(1, 5, [[0,0,5],[0,3,4],[0,2,1]]))  # [[5,5,1,4,4]]