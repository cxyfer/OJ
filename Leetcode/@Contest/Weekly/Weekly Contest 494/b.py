import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution1:
    def uniformArray(self, nums1: list[int]) -> bool:
        arr = [[] for _ in range(2)]
        for x in nums1:
            arr[x & 1].append(x)
        arr[1].sort()

        def check(b: int) -> bool:
            for x in nums1:
                if x & 1 == b:
                    continue
                idx = bisect_right(arr[1], x - 1) - 1
                if idx < 0:
                    return False
            return True

        return check(0) or check(1)

class Solution2:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1:
            return True
        cnt = [0] * 2
        for x in nums1:
            cnt[x % 2] += 1
        return cnt[0] == 0 or cnt[1] == 0

# Solution = Solution1
Solution = Solution2