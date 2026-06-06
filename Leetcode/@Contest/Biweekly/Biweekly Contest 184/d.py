import math
from math import *
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q4: ||質數篩 + 排容原理||
題意：
給定一個數列 nums 和一個整數 maxVal，可以將 nums 中每個元素修改成 [1, maxVal] 之間的任意數字，每次修改代價為 1。
最終可以選定一個 nums[i]，使得修改後 nums[i] 與 nums 中其他元素皆互質，求最大的 nums[i] - cost，其中 cost 是修改的代價。

首先要注意到 1 <= maxVal <= 10​​​​​​​^5 和 1 <= nums[i] <= 10^5，這暗示了我們可以使用值域相關的解法。
另外任何數與 1 都互質，因此可以把其他元素修改為 1 來滿足條件。

那麼我們可以枚舉選擇的數字 v，並令與 v 不互質（即需要被修改）的元素的數量為 c，則有兩種情況：
1. v 在 nums 中，此時 cost 為 c - 1，因為 v 本身不需要修改
   但當 v = 1 時，會有 c = 0 的情況，此時 cost 也應該為 0，因此需要寫作 max(0, c - 1)
2. v 不在 nums 中，此時 cost 為 max(1, c)，因為至少需要修改 v

那麼接著考慮如何計算 c，即與 v 不互質的元素的數量呢？
由於與 v 不互質的元素必定是 v 的因數的倍數，
因此可以先預處理 cnt_mul[d] 表示 nums 中 d 的倍數的元素的數量，這個預處理是調和級數級別的。

接著可以對 v 進行質因數分解後，用二進制枚舉質因數的子集，
對於每個子集計算其對應的數字 prod，得到 cnt_mul[prod]，然後用根據子集的大小，使用排容原理計算答案。

舉例來說：
與 30 不互質的元素必定是 2、3 或 5 的倍數，
f(30) = cnt_mul[2] + cnt_mul[3] + cnt_mul[5] - cnt_mul[2 * 3] - cnt_mul[2 * 5] - cnt_mul[3 * 5] + cnt_mul[2 * 3 * 5]
"""

MAX_N = int(1e5 + 5)

spf = [0] * (MAX_N + 1)  # least prime factor
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
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        cnt = Counter(nums)
        U = max(max(nums), maxVal)  # U <= 1e5

        # cnt_m[x] 表示 nums 有多少元素是 x 的倍數
        # n/1 + n/2 + n/3 + ... + n/n = n(1/1 + 1/2 + 1/3 + ... + 1/n) = O(n log n)
        cnt_m = defaultdict(int)
        for v in range(1, U + 1):
            for x in range(v, U + 1, v):
                cnt_m[v] += cnt[x]

        ans = -inf
        for v in range(1, U + 1):
            if v > maxVal and cnt[v] == 0:
                continue
            factors = prime_factorization(v)

            m = len(factors)
            c = 0  # 與 v 不互質的元素的數量
            for msk in range(1, 1 << m):  # 二進位枚舉質因數的子集
                prod = 1
                for i in range(m):
                    if (msk >> i) & 1:
                        prod *= factors[i]
                # 排容原理
                if msk.bit_count() & 1:
                    c += cnt_m[prod]
                else:
                    c -= cnt_m[prod]
            # v 在 nums 中，此時 cost 為 max(0, c - 1)
            if cnt[v] > 0:
                ans = max(ans, v - max(0, c - 1))
            # v 不在 nums 中，需要滿足 v <= maxVal，此時 cost 為 max(1, c)
            if v <= maxVal:
                ans = max(ans, v - max(1, c))
        return ans


sol = Solution()
print(sol.maxScore([3, 4, 6], 5))  # 4
print(sol.maxScore([1, 2, 3], 4))  # 3
print(sol.maxScore([2, 2], 1))  # 1
print(sol.maxScore([1], 1))  # 1
