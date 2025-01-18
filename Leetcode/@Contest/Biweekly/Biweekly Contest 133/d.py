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

        @cache
        def dfs(i, j):
            if j == 0:  # 只有由小到大的排列才能有 0 個 Inversions
                return 1
            if i == 0:
                return 0
            if i in mp:
                print(i, j, mp[i], dfs(i - 1, j - mp[i]))
                return dfs(i - 1, j - mp[i]) if j == mp[i] else 0
            ans = 0
            for k in range(i):  # 這個數字與前面的數字有 k 個 Inversions
                if k <= i:
                    ans += dfs(i - 1, j - k)
                    ans %= MOD
                else:
                    break
            return ans % MOD

        mx = max(mp.values())

        return sum(dfs(n - 1, j) for j in range(mx + 1)) % MOD


sol = Solution()
print(sol.numberOfPermutations(3, [[2, 2], [0, 0]]))  # 2
print(sol.numberOfPermutations(3, [[2, 2], [1, 1], [0, 0]]))  # 1
print(sol.numberOfPermutations(2, [[0, 0], [1, 0]]))  # 1
print(sol.numberOfPermutations(3, [[1, 0], [2, 1], [0, 0]]))  # 1
