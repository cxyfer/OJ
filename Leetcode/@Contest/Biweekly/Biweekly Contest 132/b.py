import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return max(range(n), key=lambda i: skills[i])
        ans = 0
        win = 0
        for i in range(1, n):
            if skills[i] > skills[ans]:
                ans = i
                win = 0
            win += 1
            if win == k:
                break
        return ans
sol = Solution()
print(sol.findWinningPlayer([4,2,6,3,9], 2)) # 2
print(sol.findWinningPlayer([2,5,4], 3)) # 1
print(sol.findWinningPlayer([7,5,16,3,13,2,8,18], 826156069)) # 7