import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        BITS = max(nums).bit_length()
        f = [0] * (1 << BITS)
        for x in nums:
            f[x] = x
        
        for i in range(BITS):
            for msk in range(1 << BITS):
                if (msk >> i) & 1:
                    if f[msk ^ (1 << i)] > f[msk]:
                        f[msk] = f[msk ^ (1 << i)]
        # return reduce(max, [x * f[x ^ ((1 << BITS) - 1)] for x in nums])
        ans = 0
        msk = (1 << BITS) - 1
        for x in nums:
            if x * f[msk ^ x] > ans:
                ans = x * f[msk ^ x]
        return ans

sol = Solution()
print(sol.maxProduct([1,2,3,4,5,6,7]))  # 12
print(sol.maxProduct([5,6,4]))  # 0
print(sol.maxProduct([64,8,32]))  # 2048
print(sol.maxProduct([9,2,19]))  # 18
print(sol.maxProduct([15,9,18]))  # 162

# with open("test.txt", "w") as f:
#     N = int(1e5)
#     nums = list(range(1, int(9e4) + 1)) + [1] * (N - int(9e4))
#     f.write(str(nums))