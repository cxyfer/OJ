import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # ans = 0
        # for x in nums:
        #     ans += (x % 3 != 0)
        # return ans
        return sum(x % 3 != 0 for x in nums)

[1,2,3,4]
[3,6,9]

sol = Solution()
print(sol.minimumOperations([3,6,9])) # 0
