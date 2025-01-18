import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] * nums[0]
        
        def all_gcd(lst: List[int]) -> int:
            res = lst[0]
            for num in lst[1:]:
                res = math.gcd(res, num)
            return res

        def all_lcm(lst: List[int]) -> int:
            res = lst[0]
            for num in lst[1:]:
                res = math.lcm(res, num)
            return res

        n = len(nums)
        ans = all_gcd(nums) * all_lcm(nums)
        for i in range(n):
            lst = nums[:i] + nums[i+1:]
            ans = max(ans, all_gcd(lst) * all_lcm(lst))
        return ans

sol = Solution()
    # Example 1
nums1 = [2, 4, 8, 16]
print(sol.maxScore(nums1))  # 輸出應為 64

    # Example 2
nums2 = [1, 2, 3, 4, 5]
print(sol.maxScore(nums2))  # 輸出應為 60

    # Example 3
nums3 = [3]
print(sol.maxScore(nums3))  # 輸出應為 9
