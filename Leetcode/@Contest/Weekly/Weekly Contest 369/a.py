# You are given a 0-indexed integer array nums, and an integer k.

# The K-or of nums is a non-negative integer that satisfies the following:

# The ith bit is set in the K-or if and only if there are at least k elements of nums in which bit i is set.
# Return the K-or of nums.

# Note that a bit i is set in x if (2i AND x) == 2i, where AND is the bitwise AND operator.
from typing import List
from collections import Counter

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        for num in nums:
            idx = 0
            while num:
                cnt[idx] += num & 1
                num >>= 1
                idx += 1
        ans = 0
        for b in cnt.keys():
            ans += (1 << b) if cnt[b] >= k else 0
        return ans


sol = Solution()
print(sol.findKOr([7,12,9,8,9,15], 4)) # 9
print(sol.findKOr([2,12,1,11,4,5], 6)) # 0
print(sol.findKOr([10,8,5,9,11,6,8], 1)) #15