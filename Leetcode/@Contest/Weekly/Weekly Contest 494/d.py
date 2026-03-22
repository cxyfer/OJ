import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        B = max(nums).bit_length()

        L = [0] * n
        last = [-1] * B
        mp = defaultdict(lambda: -1)
        for i, x in enumerate(nums):
            L[i] = mp[x] + 1
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i
                else:
                    L[i] = max(L[i], last[b] + 1)
            mp[x] = i

        R = [n - 1] * n
        last = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i
                else:
                    R[i] = min(R[i], last[b] - 1)

        return sum((i - li + 1) * (ri - i + 1) for i, (li, ri) in enumerate(zip(L, R)))

sol = Solution()
print(sol.countGoodSubarrays([4,2,3]))  # 4
print(sol.countGoodSubarrays([1,3,1]))  # 6