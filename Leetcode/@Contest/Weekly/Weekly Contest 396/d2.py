import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        相等後的數不一定是最大值
    """
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        mx, mn = max(nums), min(nums)
        if cost2 >= 2 * cost1: # 用 cost1 就好
            return (mx * n - sum(nums)) * cost1 % MOD # 除了最大值以外的都變成最大值
        
        cnt0 = Counter(nums)
        def f(target): # 將所有數變成 target 的最小成本
            hp = [x for x in nums]
            heapify(hp)
            ans1, ans2 = 0, 0
            while len(hp) > 1:
                x = heappop(hp)
                y = heappop(hp)
                d = target - y
                ans2 += d
                heappush(hp, x+d)
            if hp:
                ans1 = target - hp[0]
            return ans1 * cost1 + ans2 * cost2
        ans = float("inf")
        for x in range(mx, mx + 100):
            ans = min(ans, f(x))
        return ans % MOD
sol = Solution()
print(sol.minCostToEqualizeArray([4,1], 5, 2)) # 15
print(sol.minCostToEqualizeArray([2,3,3,3,5], 2, 1)) # 6
print(sol.minCostToEqualizeArray([3,5,3], 1, 3)) # 4
print(sol.minCostToEqualizeArray([1,14,14,15], 2, 1)) # 20
print(sol.minCostToEqualizeArray([4,3], 2, 6)) # 2
print(sol.minCostToEqualizeArray([4,3,1,8], 5, 1)) # 8