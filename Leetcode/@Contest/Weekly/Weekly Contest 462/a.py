import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        ans = [[x for x in row] for row in grid]
        for i in range(x, x + k):
            for j in range(y, y + k):
                ans[i][j] = grid[x + x + k - i - 1][j]
        return ans
    
sol = Solution()

print(sol.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3))
print(sol.reverseSubmatrix([[3,4,2,3],[2,3,4,2]], 0, 2, 2))