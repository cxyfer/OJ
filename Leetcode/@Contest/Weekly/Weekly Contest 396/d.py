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
            cnt = cnt0.copy()
            ans = 0
            hp = []
            for k in range(mn, target+1):
                d = target - k
                if d == 0: continue
                if cnt[k] == 0: continue
                # print(k, d, ans, hp, cnt, sep="\t")
                while hp and hp[0] < k and cnt[k] > 0:
                    x = heappop(hp)
                    v = min(cnt[k], (target-x) // d) # 可給/需要的完整組數
                    ans += v * d * cost2
                    x += d * v
                    cnt[k] -= v
                    if x < target and cnt[k]: # 需要不完整的組數
                        dx = min(target - x, target - k)
                        ans += dx * cost2
                        cnt[k] -= 1
                        cnt[k+dx] += 1
                        x += dx
                    if x < target:
                        if x < k:
                            heappush(hp, x)
                        else:
                            cnt[x] += 1
                    # print("while", ans, hp, cnt, sep="\t")
                v = cnt[k]
                ans += (d * (v // 2) * cost2)
                cnt[k] -= (v // 2) * 2
                if cnt[k] != 0:
                    heappush(hp, k)
                del cnt[k]
                # print(ans, hp, cnt, sep="\t")
            # print(ans, hp, cnt, sep="\t")
            if hp:
                ans += (target - hp[0]) * cost1
            return ans
        ans = float("inf")
        for x in range(mx, mx + 100):
            res = f(x)
            if res < ans:
                ans = res
                print(x, ans)
            # ans = min(ans, f(x))
        return ans % MOD
sol = Solution()
# print(sol.minCostToEqualizeArray([4,1], 5, 2)) # 15
# print(sol.minCostToEqualizeArray([2,3,3,3,5], 2, 1)) # 6
# print(sol.minCostToEqualizeArray([3,5,3], 1, 3)) # 4
# print(sol.minCostToEqualizeArray([1,14,14,15], 2, 1)) # 20
# print(sol.minCostToEqualizeArray([4,3], 2, 6)) # 2
print(sol.minCostToEqualizeArray([4,3,1,8], 5, 1)) # 8