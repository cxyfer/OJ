import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + nums[i]
        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                if pre[i] == suf[i]:
                    ans += 2
                elif abs(pre[i] - suf[i]) == 1:
                    ans += 1
        return ans


sol = Solution()
print(sol.countValidSelections([1,0,2,0,3])) # 2
