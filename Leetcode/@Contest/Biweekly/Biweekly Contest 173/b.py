import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = float("inf")
        left = s = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] == 1:
                s += x
            while s >= k:
                ans = min(ans, right - left + 1)
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    s -= y
                left += 1
        return ans if ans != float("inf") else -1


sol = Solution()
print(sol.minLength([2,2,3,1], 4))  # 2