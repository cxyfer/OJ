import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        mx = max(nums1)
        ans = 0
        cnt = defaultdict(int)
        for num in nums1:
            if num % k == 0:
                cnt[num] += 1
        cnt2 = Counter(nums2)
        for x, v in cnt2.items():
            x = x * k
            cur = x
            while cur <= mx:
                if cur in cnt:
                    ans += cnt[cur] * v
                cur += x
        return ans
    
sol = Solution()
print(sol.numberOfPairs([1,3,4], [1,3,4], 1)) # 5
print(sol.numberOfPairs([1,2,4,12], [2,4], 3)) # 2
print(sol.numberOfPairs([2,8,17,6], [3,1,1,8], 2)) # 7