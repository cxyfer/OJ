import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def dfs(day, city):
            if day == k:
                return 0
            res = stayScore[day][city] + dfs(day + 1, city)
            for dest in range(n):
                if dest != city:
                    res = max(res, travelScore[city][dest] + dfs(day + 1, dest))
            return res

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(0, i))
        return ans

# 範例測試
sol = Solution()
# 範例 1
n1 = 2
k1 = 1
stayScore1 = [[2, 3]]
travelScore1 = [
        [0, 2],
        [1, 0]
    ]
print(sol.maxScore(n1, k1, stayScore1, travelScore1))  # 輸出: 3

# 範例 2
n2 = 3
k2 = 2
stayScore2 = [
        [3, 4, 2],
        [2, 1, 2]
    ]
travelScore2 = [
        [0, 2, 1],
        [2, 0, 4],
        [3, 2, 0]
    ]
print(sol.maxScore(n2, k2, stayScore2, travelScore2))  # 輸出: 8
