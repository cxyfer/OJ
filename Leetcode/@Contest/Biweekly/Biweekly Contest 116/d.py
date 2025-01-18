# You are given a 0-indexed integer array nums.

# The distinct count of a subarray of nums is defined as:

# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.

# Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List
from collections import defaultdict

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        cnt = defaultdict(int)
        ans = 0
        for l in range(1, n+1):
            last = defaultdict(lambda: -1) # last[num] = last index of num
            for i in range(n):
                if last[nums[i]] >= i - l + 1:
                    cnt[nums[i]] -= 1
                if i - l >= 0:
                    last[nums[i-l]] = -1
                last[nums[i]] = i
        for num in cnt:
            ans += cnt[num] * num ** 2
        return ans % MOD
sol = Solution()
print(sol.sumCounts([1,2,1])) # 15
print(sol.sumCounts([2,2])) # 3
print(sol.sumCounts([2,2,5,5])) # 22