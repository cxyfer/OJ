import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        pre = [0] * (2 * n)
        for i in range(2 * n):
            pre[i] = pre[i-1] + (colors[i % n] != colors[(i-1) % n])
        ans = 0
        for i in range(n):
            if pre[i + k - 1] - pre[i] == k - 1:
                ans += 1
        return ans
        
sol = Solution()

print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3)) # 3
print(sol.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6)) # 2
print(sol.numberOfAlternatingGroups([1,1,0,1], 4)) # 0