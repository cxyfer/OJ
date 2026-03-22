import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution1:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = (n + 1) // 2

        def build(arr: List[int]) -> dict[int, int]:
            m = len(arr)
            mp = defaultdict(lambda: float("-inf"))
            for msk in range(1 << m):
                v = 0
                for i in range(m):
                    if (msk >> i) & 1:
                        v ^= arr[i]
                mp[v] = max(mp[v], msk.bit_count())
            return mp

        mp1 = build(nums[:mid])
        mp2 = build(nums[mid:])
        ans = float("inf")
        for k, v in mp1.items():
            ans = min(ans, n - (v + mp2[k ^ target]))
        return ans if ans != float("inf") else -1

class Solution2:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        B = max(nums).bit_length()
        U = (1 << B) - 1
        if target > U:
            return -1

        f = defaultdict(lambda: float("-inf"))
        f[0] = 0
        for x in nums:
            nf = f.copy()
            for k, v in f.items():
                nf[k ^ x] = max(nf[k ^ x], v + 1)
            f = nf
        return n - f[target] if f[target] != float("-inf") else -1

# Solution = Solution1
Solution = Solution2

sol = Solution()
print(sol.minRemovals([1,2,3], 2))  # 1