"""
100257. Find the Median of the Uniqueness Array

You are given an integer array nums. The uniqueness array of nums is the sorted array that contains the number of distinct elements of all the subarrays of nums. In other words, it is a sorted array consisting of distinct(nums[i..j]), for all 0 <= i <= j < nums.length.

Here, distinct(nums[i..j]) denotes the number of distinct elements in the subarray that starts at index i and ends at index j.

Return the median of the uniqueness array of nums.

Note that the median of an array is defined as the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the smaller of the two values is taken.

"""

import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *
import time

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = Counter()
        ans[1] = n
        cnt = Counter()
        left = 0
        for right in range(n):
            cnt[nums[right]] += 1
            tmp = cnt.copy()
            while right - left + 1 >= 2:
                ans[len(cnt)] += 1
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            cnt = tmp
            left = 0
        m = sum(ans.values())
        mid = m // 2 if m & 1 else m // 2 - 1
        for k, v in sorted(ans.items()):
            mid -= v
            if mid < 0:
                return k
            
from random import *

nums = [randint(1, 10**5) for _ in range(10**4)]
sol = Solution()
print(sol.medianOfUniquenessArray([1,2,3])) # 1
print(sol.medianOfUniquenessArray([3,4,3,4,5])) # 2
print(sol.medianOfUniquenessArray([4,3,5,4])) # 2
t1 = time.time()
print(sol.medianOfUniquenessArray(nums))
t2 = time.time()
print('time:', t2-t1)