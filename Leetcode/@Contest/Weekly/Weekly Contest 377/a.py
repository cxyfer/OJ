import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # return self.solve1(nums)
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> List[int]:
        ans = []
        hp = [x for x in nums]
        heapify(hp)
        while len(hp) > 1:
            x = heappop(hp)
            y = heappop(hp)
            ans.append(y)
            ans.append(x)
        return ans
    def solve2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for i in range(1, n, 2):
            nums[i-1], nums[i] = nums[i], nums[i-1]
        return nums

sol = Solution()
