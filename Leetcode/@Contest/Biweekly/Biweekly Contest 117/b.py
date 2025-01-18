# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

from math import *

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 全部 - 1人大於limit - 2 人大於limit
        if n > 3 * limit:
            return 0
        ans = comb(n + 2, 2)
        if n > limit:
            ans -= 3 * comb(n - limit + 1, 2)
        if n - 2 >= 2 * limit:
            ans += 3 * comb(n - 2 * limit, 2)
        return ans
sol = Solution()
print(sol.distributeCandies(5, 2)) # 3
print(sol.distributeCandies(3, 3)) # 10
print(sol.distributeCandies(10001, 20001)) 
print(sol.distributeCandies(1, 2)) # 3
 