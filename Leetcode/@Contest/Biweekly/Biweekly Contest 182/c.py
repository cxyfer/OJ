import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from typing import List

"""
## Q3: ||BFS||
注意值域，三維座標的值域範圍為 [0, 6]，而產生的新點也必然在值域內，因此最多只有 7^3 個點。
此時問題就變得很簡單了，我們只要維護目前能夠產生的點，以及新世代中能產生的點即可。
姑且算是 BFS ?
"""

class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target = tuple(target)
        vis = set((x, y, z) for x, y, z in points)

        ans = 0
        while target not in vis:
            new = set()
            P = list(vis)
            n = len(P)
            for i, (x1, y1, z1) in enumerate(P):
                for j in range(i + 1, n):
                    x2, y2, z2 = P[j]
                    x = (x1 + x2) // 2
                    y = (y1 + y2) // 2
                    z = (z1 + z2) // 2
                    if (x, y, z) not in vis:
                        new.add((x, y, z))
            if not new:
                return -1
            vis.update(new)
            ans += 1
        return ans

sol = Solution()
print(sol.minGenerations([[0,0,0],[6,6,6]], [3,3,3]))  # 1
print(sol.minGenerations([[0,0,0],[5,5,5]], [1,1,1]))  # 2
print(sol.minGenerations([[0,0,0],[2,2,2],[3,3,3]], [2,2,2]))  # 0
print(sol.minGenerations([[1,2,3]], [5,5,5]))  # -1
print(sol.minGenerations([[5,0,5],[3,6,2]], [2,1,5]))  # -1
