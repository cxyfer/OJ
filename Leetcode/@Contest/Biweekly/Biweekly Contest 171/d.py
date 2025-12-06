import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class BIT:  # PURQ, 1-based
    __slots__ = ['tree']

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= (k & -k)
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)

        B = list(sorted(set(nums)))
        mp = {x: i for i, x in enumerate(B, start=1)}
        m = len(mp)

        bit = BIT(m)
        cur = 0
        for r in range(k):
            x = nums[r]
            cur += bit.query(mp[x] + 1, m)
            bit.add(mp[x], 1)

        ans = cur
        for r in range(k, n):
            x = nums[r]
            y = nums[r - k]
            cur -= bit.query(1, mp[y] - 1)
            bit.add(mp[y], -1)
            cur += bit.query(mp[x] + 1, m)
            bit.add(mp[x], 1)
            ans = min(ans, cur)
        return ans

sol = Solution()
print(sol.minInversionCount([3,1,2,5,4], 3))  # 0

print(sol.minInversionCount([5,3,2,1], 4))  # 6