# You are given a 0-indexed array of positive integers nums and a positive integer limit.

# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

# Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

# An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

from typing import List
import collections
from heapq import *

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ans = [0] * n

        lst = [(num, idx) for idx, num in enumerate(nums)]
        lst.sort()

        i = 0
        while i < n:
            num, idx = lst[i]
            hp_idx = []
            hp_num = []
            heappush(hp_idx, idx)
            heappush(hp_num, num)
            j = i + 1
            while j < n and lst[j][0] - lst[j-1][0] <= limit:
                heappush(hp_idx, lst[j][1])
                heappush(hp_num, lst[j][0])
                j += 1
            # print(i, j, lst[i:j])
            # print(hp_idx, hp_num)
            while hp_idx:
                ans[heappop(hp_idx)] = heappop(hp_num)
            i = j
        return ans


sol = Solution()
print(sol.lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2)) # [1,3,5,8,9]
print(sol.lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3)) # [1,6,7,18,1,2]
print(sol.lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3)) # [1,7,28,19,10]