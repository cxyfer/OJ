import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        cnt = defaultdict(int)
        ans = []
        for x in nums:
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(x)
        return ans