# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

from functools import lru_cache
from math import *

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit+1):
            for j in range(limit+1):
                k = n - i - j
                if k >= 0 and k <= limit:
                    ans += 1
        return ans
sol = Solution()
print(sol.distributeCandies(5, 2)) # 3
print(sol.distributeCandies(3, 3)) # 10
print(sol.distributeCandies(10001, 20001)) 
 