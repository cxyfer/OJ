from itertools import *
from typing import *

"""
決策單調性優化DP

Problems:
- 3826. Minimum Partition Score
- 3500. Minimum Cost to Divide Array Into Subarrays (Python TLE, C++ AC)
"""

class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        def cost(l: int, r: int) -> int:  # cost of [l, r)
            v = s[r]  - s[l]
            return v * (v + 1) // 2
        
        f = [float('inf')] * (n + 1)
        nf = [float('inf')] * (n + 1)
        f[0] = 0

        def solve(l: int, r: int, opt_l: int, opt_r: int):
            if l > r:
                return
            mid = (l + r) // 2

            best_val = float('inf')
            opt = -1
            for p in range(opt_l, min(opt_r, mid - 1) + 1):
                val = f[p] + cost(p, mid)
                if val < best_val:
                    best_val = val
                    opt = p
            nf[mid] = best_val

            solve(l, mid - 1, opt_l, opt)
            solve(mid + 1, r, opt, opt_r)
        
        for j in range(1, k + 1):
            solve(j, n, j - 1, n - 1)
            f = nf[:]
        return f[n]


sol = Solution()
print(sol.minPartitionScore([5,1,2,1], 2))  # 25
print(sol.minPartitionScore([1,2,3,4], 1))  # 55
print(sol.minPartitionScore([1,1,1], 3))  # 3