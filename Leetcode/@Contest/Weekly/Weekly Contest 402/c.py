import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        keys = sorted(cnt.keys())
        m = len(keys)

        dp = [0] * m
        dp[0] = keys[0] * cnt[keys[0]]
        mx = [dp[0]] + [0] * m # mx[i] = max(dp[0], dp[1], ..., dp[i])
        for i in range(1, m):
            for j in range(i-1, -1, -1): # 每次最多看 3 個數
                d = keys[i] - keys[j]
                if d == 1 or d == 2:
                    continue
                # dp[i] = max(dp[i], dp[j]) # 可以維護 mx ，這樣就能用下面兩行取代
                dp[i] = max(dp[i], mx[j])
                break
            dp[i] += keys[i] * cnt[keys[i]]
            mx[i] = max(mx[i - 1], dp[i])
        return max(dp)

        
sol = Solution()
print(sol.maximumTotalDamage([1,1,3,4])) # 6
print(sol.maximumTotalDamage([7,1,6,6])) # 13
print(sol.maximumTotalDamage([7,1,6,3])) # 10
print(sol.maximumTotalDamage([5,9,2,10,2,7,10,9,3,8])) # 31