import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + (1 if (nums[i] == target) else -1)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                ans += s[j] - s[i] > 0
        return ans

sol = Solution()
print(sol.countMajoritySubarrays([1,2,2,3], 2))  # 5
print(sol.countMajoritySubarrays([1,1,1,1], 1))  # 10