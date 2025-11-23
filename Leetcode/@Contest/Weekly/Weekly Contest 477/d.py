import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

MOD = int(1e9 + 7)
MAX_N = int(1e5 + 5)
pow2 = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    pow2[i] = (pow2[i - 1] * 2) % MOD

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        n = len(nums)
        tot = reduce(or_, nums)

        B = max(nums).bit_length()
        U = 1 << B
        f = [0] * U
        for x in nums:
            f[x] += 1
        
        for i in range(B):
            # for msk in range(U):
            #     if (msk >> i) & 1:
            #         f[msk] += f[msk ^ (1 << i)]
            s = 0
            while s < U:
                s |= (1 << i)
                f[s] += f[s ^ (1 << i)]
                s += 1

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        ans = pow2[n]
        cnt0 = tot.bit_count()
        for msk in range(U):
            if (msk | tot) == tot:
                cnt = msk.bit_count()
                if (cnt0 - cnt) & 1:
                    ans += pow2[f[msk]]
                else:
                    ans -= pow2[f[msk]]
                ans %= MOD
        return ans

sol = Solution()
print(sol.countEffective([1, 2, 3]))  # 3