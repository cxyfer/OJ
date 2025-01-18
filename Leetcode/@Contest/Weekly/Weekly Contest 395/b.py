import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        k1 = sorted(cnt1.keys())
        mx2 = max(cnt2.keys())

        def check(x): # 若差是 x ，其缺失的數字數量
            res = 0
            for k, v in cnt1.items():
                if k + x not in cnt2:
                    res += v
                elif cnt2[k + x] < v:
                    res += v - cnt2[k + x]
            return res
        
        for i in range(3): # 0, 1, 2
            mx1 = k1[-1-i] # -1, -2, -3
            x = mx2 - mx1
            if check(x) == 2-i: # 缺失的數字數量必須是 2, 1, 0
                return x
            cnt1[mx1] -= 1
        return -1

sol = Solution()
print(sol.minimumAddedInteger([4,20,16,12,8], [14,18,10])) # -2
print(sol.minimumAddedInteger([3,5,5,3], [7,7])) # 2
print(sol.minimumAddedInteger([7,2,6,8,7], [7,6,5])) # -1
print(sol.minimumAddedInteger([9,4,3,9,4], [7,8,8])) # 4
print(sol.minimumAddedInteger([9,10,0,7,8,0], [0,8,7,0])) # 0