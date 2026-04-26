import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import *

"""
Q4: ||線段樹/BIT 優化DP||
令 f[i][0/1] 表示以第 i 個數字作為最小值/最大值結尾的最大分數
則 f[i][0] 的轉移來源 j 需滿足 j <= i - k 且 nums[j] > nums[i]，f[i][1] 同理。
直接 O(n) 枚舉轉移來源，總共需要 O(n^2) 時間，顯然不能接受。

注意到轉移來源皆滿足 nums[j] > nums[i] 的性質，且 nums[i] 最大為 1e5，
因此我們可以對值域使用動態維護區間最大值的資料結構來優化轉移。
當考慮到 i 時，區間內需維護所有滿足 j <= i - k 的 f[j][0/1]

設 ds1[x] 表示以 x 最小值結尾時的最大分數，ds2[x] 表示以 x 最大值結尾時的最大分數，且 query(l, r) 表示求 [l, r] 區間的最大值。
記 x = nums[i], MX = max(nums)，則有：
f[i][0] = ds2.query(nums[i] + 1, MX) + nums[i]
f[i][1] = ds1.query(0, nums[i] - 1) + nums[i]

理論上可以用 Segment Tree 來實現，但我的模板被卡常了(哭)
改成用 Fenwick Tree 來實現，但 Fenwick Tree 只能求前綴最大值，因此對需要求後綴最大值的 ds2 可以反轉值域來維護。
"""


class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def update(self, k: int, x: int) -> None:
        while k < len(self.tree):
            self.tree[k] = max(self.tree[k], x)
            k += k & -k

    def preMax(self, k: int) -> int:
        res = 0
        while k > 0:
            res = max(res, self.tree[k])
            k -= k & -k
        return res


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # 離散化
        Xs = sorted(set(nums))
        mp = {x: i for i, x in enumerate(Xs, start=1)}
        m = len(Xs)

        bit1 = BIT(m + 1)  # bit1[x] 表示以 x 最小值結尾時的最大分數
        bit2 = BIT(m + 1)  # bit2[MX - x + 1] 表示以 x 最大值結尾時的最大分數

        # f[i][0/1] 表示以第 i 個數字作為最小值/最大值結尾的最大分數
        f = [[0, 0] for _ in range(n)]

        for i, x in enumerate(nums):
            if i - k >= 0:
                y = nums[i - k]
                bit1.update(mp[y], f[i - k][0])
                bit2.update(m + 1 - mp[y], f[i - k][1])
            f[i][0] = bit2.preMax(m + 1 - (mp[x] + 1)) + x
            f[i][1] = bit1.preMax(mp[x] - 1) + x
        return max(map(max, f))


sol = Solution()
print(sol.maxAlternatingSum(nums=[5, 4, 2], k=2))  # 7
print(sol.maxAlternatingSum(nums=[3, 5, 4, 2, 4], k=1))  # 14
print(sol.maxAlternatingSum(nums=[1, 2], k=1))
print(sol.maxAlternatingSum(nums=[5, 1], k=1))  # 6
