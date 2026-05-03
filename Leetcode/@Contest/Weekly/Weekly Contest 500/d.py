import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4. 二維 LIS
若要選取 x = nums[i]，則此時需要在 i 之前刪除 i - x 個元素，記做 del[i] = i - x。
顯然只有 del[i] >= 0 時，才能選取 x。

根據題意，需要選出一組下標 j0, j1, ..., jk，使得 nums[j0] < nums[j1] < ... < nums[jk]
但除此之外，在選取 nums[j0] 時，需要刪除 del[j0] 個元素，因此在選取 j1 時，也需要至少刪除 del[j1] 個元素，以此類推。
故存在另一條限制，即 del[j0] <= del[j1] <= ... <= del[jk]

自此，我們可以將問題轉換為二維LIS問題，即 354. Russian Doll Envelopes，
但本題的第二維其實是非嚴格遞增的，這可以透過將 lower_bound 改為 upper_bound 來實現。
"""

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        P = []
        for i, x in enumerate(nums):
            if x <= i:
                P.append((x, i - x))

        f = []
        for x, d in sorted(P, key = lambda x : (x[0], -x[1])):
            idx = bisect_right(f, d)
            if idx == len(f):
                f.append(d)
            else:
                f[idx] = d
        return len(f)


sol = Solution()
print(sol.maxFixedPoints([0,2,1]))  # 2
print(sol.maxFixedPoints([3,1,2]))  # 2
print(sol.maxFixedPoints([1,0,1,2]))  # 3
print(sol.maxFixedPoints([1,2,2]))  # 1
print(sol.maxFixedPoints([1,0,2,2]))  # 2
print(sol.maxFixedPoints([3,1,1,3]))  # 2