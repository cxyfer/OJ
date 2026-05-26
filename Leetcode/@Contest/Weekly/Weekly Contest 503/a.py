import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        cnt = defaultdict(int)
        for x in nums:
            if cnt[x] >= k:
                continue
            ans.append(x)
            cnt[x] += 1
        return ans