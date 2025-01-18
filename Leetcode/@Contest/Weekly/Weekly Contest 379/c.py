import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        cnt = Counter()
        for k, v in cnt1.items():
            cnt[k] += 1
        for k, v in cnt2.items():
            cnt[k] += 2
        # 3: both, 1: nums1, 2: nums2
        cntcnt = Counter(cnt.values())
        ans = 0
        # 考慮在左邊的
        if cntcnt[1] >= (n//2):
            ans += n//2
        else:
            ans += cntcnt[1]
            c = n//2 - cntcnt[1] # 還可以有多少個
            t = min(c, cntcnt[3]) # 從兩邊都有的拿
            ans += t
            cntcnt[3] -= t

        if cntcnt[2] >= (n//2):
            ans += n//2
        else:
            ans += cntcnt[2]
            c = n//2 - cntcnt[2] # 還可以有多少個
            t = min(c, cntcnt[3]) # 從兩邊都有的拿
            ans += t
            cntcnt[3] -= t
        return ans

sol = Solution()
print(sol.maximumSetSize([1,2,1,2], [1,1,1,1])) #2
print(sol.maximumSetSize([1,2,3,4,5,6], [2,3,2,3,2,3])) #5
print(sol.maximumSetSize([1,1,2,2,3,3], [4,4,5,5,6,6])) #6