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
        cnt = [0, 0]
        for x in nums1:
            cnt[x & 1] += 1

        def check(b: int) -> bool:
            for x in nums1:
                if x & 1 == b:
                    continue
                if cnt[1] - (x & 1) == 0:
                    return False
            return True

        return check(0) or check(1)

class Solution2:
    def uniformArray(self, _: list[int]) -> bool:
        return True

# Solution = Solution1
Solution = Solution2