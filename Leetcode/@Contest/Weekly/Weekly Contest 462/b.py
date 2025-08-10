import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        return ans if (ans := reduce(and_, [i for i in range(len(nums)) if nums[i] != i], -1)) != -1 else 0
        
sol = Solution()

print(sol.sortPermutation([0,3,2,1]))  # 1
print(sol.sortPermutation([0,1,3,2]))  # 2
print(sol.sortPermutation([3,2,1,0]))  # 0