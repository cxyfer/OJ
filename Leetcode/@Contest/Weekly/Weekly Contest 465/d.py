import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import xor

"""
倍數排容原理 + BIT 優化 DP
- 1626. Best Team With No Conflicts
- 673. Number of Longest Increasing Subsequence
"""
MOD = int(1e9 + 7)
MAX_V = int(7e4 + 5)
divisors = [[] for _ in range(MAX_V)]
for i in range(1, MAX_V):
    for j in range(i, MAX_V, i):
        divisors[j].append(i)

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        mx = max(nums)

        # 因數分解，方便後續枚舉 gcd
        groups = defaultdict(list)
        for x in nums:
            for d in divisors[x]:
                groups[d].append(x)

        # f1[g] 表示 gcd 為 g 的倍數的 LIS 數量
        f1 = [0] * (mx + 1)
        for g, vals in groups.items():
            # 離散化
            mp = {v: i + 1 for i, v in enumerate(sorted(set(vals)))}
            sz = len(mp)

            # f[v] 表示最大值恰好為 v 的 LIS 數量，使用 BIT 維護
            tree = [0] * (sz + 1)
            def update(k: int, x: int) -> None: # 令 f[k] += x
                while k < len(tree):
                    tree[k] += x
                    k += (k & -k)

            def query(k: int) -> int: # 返回 sum(f[:k+1])
                res = 0
                while k > 0:
                    res += tree[k]
                    k -= (k & -k)
                return res
            
            for v in vals:
                update(mp[v], 1 + query(mp[v] - 1))
            f1[g] = query(sz)

        # f2[g] = GCD 恰好為 g 的 LIS 數量
        f2 = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            if f1[g] == 0: continue
            f2[g] = f1[g]
            for v in range(2 * g, mx + 1, g):
                f2[g] = (f2[g] - f2[v]) % MOD

        return sum(g * f2[g] for g in range(1, mx + 1)) % MOD

sol = Solution()
print(sol.totalBeauty([1,2,3]))  # 10
print(sol.totalBeauty([4,6]))  # 12
print(sol.totalBeauty([78,53]))  # 131