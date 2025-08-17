import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import xor

MOD = int(1e9 + 7)

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        mp = defaultdict(lambda: defaultdict(list))
        for l, r, k, v in queries:
            mp[k][l % k].append((l, r, v))

        for k, ms in mp.items():
            for m, lst in ms.items():
                ln = (n - 1 - m) // k + 1
                diff = [1] * (ln + 1)
                for l, r, v in lst:
                    st = (l - m) // k
                    ed = (r - m) // k
                    diff[st] = (diff[st] * v) % MOD
                    diff[ed + 1] = (diff[ed + 1] * pow(v, MOD - 2, MOD)) % MOD
                for i in range(ln):
                    if i > 0:
                        diff[i] = (diff[i] * diff[i-1]) % MOD
                    idx = m + i * k
                    nums[idx] = (nums[idx] * diff[i]) % MOD
        return reduce(xor, nums, 0)

sol = Solution()
print(sol.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]]))  # 4
print(sol.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))  # 31