import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        ans = 0
        idx = 0
        vis = [False] * n
        while 0 <= idx < n and not vis[idx]:
            vis[idx] = True
            if instructions[idx] == "jump":
                idx += values[idx]
            else:
                ans += values[idx]
                idx += 1
        return ans

sol = Solution()
print(sol.calculateScore(["jump","add","add","jump","add","jump"], [2,1,3,1,-2,-3]))  # 1
