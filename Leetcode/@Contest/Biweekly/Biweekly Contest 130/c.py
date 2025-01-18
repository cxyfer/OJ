import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i): # 從 i 開始劃分
            if i == n:
                return 0
            res = float("inf")
            cnt = [0] * 26
            for j in range(i, n):
                cnt[ord(s[j]) - ord("a")] += 1
                mx, mn = -float("inf"), float("inf")
                for k in range(26):
                    if cnt[k]:
                        mx = max(mx, cnt[k])
                        mn = min(mn, cnt[k])
                if mx == mn:
                    res = min(res, 1 + dfs(j + 1))
            return res
        return dfs(0)
    
sol = Solution()
print(sol.minimumSubstringsInPartition("aabb")) # 1
print(sol.minimumSubstringsInPartition("fabccddg")) # 3
print(sol.minimumSubstringsInPartition("abababaccddb")) # 2