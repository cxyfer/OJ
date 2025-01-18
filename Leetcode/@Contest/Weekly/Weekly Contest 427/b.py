import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        s = set(tuple(point) for point in points)
        ans = -1
        for comb in combinations(points, 4):
            X = sorted(set(point[0] for point in comb))
            Y = sorted(set(point[1] for point in comb))
            if len(X) != 2 or len(Y) != 2:
                continue
            corners = {(X[0], Y[0]), (X[0], Y[1]), (X[1], Y[0]), (X[1], Y[1])}
            if set(tuple(point) for point in comb) != corners:
                continue
            minX, maxX = X[0], X[1]
            minY, maxY = Y[0], Y[1]
            others = s - corners
            for px, py in others:
                if minX <= px <= maxX and minY <= py <= maxY:
                    break
            else:
                ans = max(ans, (maxX - minX) * (maxY - minY))
        return ans

sol = Solution()
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3]])) # 4
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[2,2]])) # -1
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]])) # 2