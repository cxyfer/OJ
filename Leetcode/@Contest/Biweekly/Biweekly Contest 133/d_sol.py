import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        mp = defaultdict(int)
        for end, cnt in requirements:
            mp[end] = cnt

        dp = [[0] * 401 for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            if (i - 1) in mp:
                mn = mx = mp[i - 1]
            else:
                mn, mx = 0, 400
            for j in range(mn, mx + 1):
                for k in range(min(i, j+1)):
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= MOD

        return sum(dp[n]) % MOD


sol = Solution()
print(sol.numberOfPermutations(3, [[2, 2], [0, 0]]))  # 2
print(sol.numberOfPermutations(3, [[2, 2], [1, 1], [0, 0]]))  # 1
print(sol.numberOfPermutations(2, [[0, 0], [1, 0]]))  # 1
print(sol.numberOfPermutations(3, [[1, 0], [2, 1], [0, 0]]))  # 1
