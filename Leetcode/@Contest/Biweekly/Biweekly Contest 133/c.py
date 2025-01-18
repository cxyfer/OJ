import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x == 0:
                ans += (ans % 2 == 0)
            else:
                ans += (ans % 2 == 1)
        return ans
    

sol = Solution()
print(sol.minOperations([0,1,1,0,1])) # 4
print(sol.minOperations([1,0,0,0])) # 1