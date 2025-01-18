import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cnt = defaultdict(int)
        cnt[nums[0]] = 1
        ans = cnt[k]
        for i in range(1, n):
            x = nums[i]
            new = defaultdict(int)
            for y in cnt:
                new[y & x] += cnt[y]
            new[x] += 1
            cnt = new
            ans += cnt[k]
        return ans

sol = Solution()
print(sol.countSubarrays([1,1,1], 1)) # 6
print(sol.countSubarrays([1,1,2], 1)) # 3
print(sol.countSubarrays([1,2,3], 2)) # 2


print(sol.countSubarrays([1,4,7,9,7], 3)) # 0