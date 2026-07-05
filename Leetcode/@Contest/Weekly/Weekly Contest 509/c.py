from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *

"""
## Q3: Maximum Subarray

如果 k 是固定的，那麼本題就是最大子陣列和問題，可以用前綴和或 Kadane 解決，這裡不贅述。
但直接對 k 枚舉的話顯然還是不行的，因此還要考慮如何優化枚舉。

由於我們要最大化能被 k 整除的數字的和，因此若 k 為合數，則結果一定不會比枚舉質數時優，因此只要枚舉質數即可。
但這題直接枚舉 <= 1e6 所有質數的話，範圍內有約 8e4 個質數，實測還是會超時。
改成僅枚舉質因數即可。
"""

MAX_N = int(1e6) + 5
MOD = int(1e9) + 7

# least prime factor
spf = [0] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    if spf[i] == 0:
        spf[i] = i
        for j in range(i * i, MAX_N + 1, i):
            if spf[j] == 0:
                spf[j] = i


def prime_factorization(x: int) -> list[int]:
    factors = []
    while x > 1:
        p = spf[x]
        factors.append(p)
        while spf[x] == p:
            x //= p
    return factors


class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        # 僅枚舉質因數
        pfs = set()
        for x in nums:
            pfs.update(set(prime_factorization(x)))

        # 若沒有質因數，則所有數字都是 1
        # 此時最大子陣列和為 -1，k = 2，答案為 -1 * 2 = -2
        if not pfs:
            return -2 % MOD

        # k 固定就是 Kadane
        ans = -inf
        min_k = inf
        for k in pfs:
            mx = -inf
            """Kadane's Algorithm"""
            # f = 0
            # for x in nums:
            #     x = x if x % k == 0 else -x
            #     f = max(f + x, x)
            #     mx = max(mx, f)
            """Prefix Sum"""
            s = mn = 0
            for x in nums:
                x = x if x % k == 0 else -x
                s += x
                mx = max(mx, s - mn)
                mn = min(mn, s)

            if mx > ans:
                ans = mx
                min_k = k
            elif mx == ans:
                min_k = min(min_k, k)
        return ans * min_k % MOD


sol = Solution()
print(sol.divisibleGame([1, 1, 19, 17, 14]))  # 361
