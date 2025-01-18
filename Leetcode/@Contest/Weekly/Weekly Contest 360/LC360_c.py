# 8021. Minimum Operations to Form Subsequence With Target Sum

# You are given a 0-indexed array nums consisting of non-negative powers of 2, and an integer target.

# In one operation, you must apply the following changes to the array:

# Choose any element of the array nums[i] such that nums[i] > 1.
# Remove nums[i] from the array.
# Add two occurrences of nums[i] / 2 to the end of nums.
# Return the minimum number of operations you need to perform so that nums contains a subsequence whose elements sum to target. If it is impossible to obtain such a subsequence, return -1.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

from typing import List
from collections import Counter
import math
from itertools import combinations
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        if sum(nums) == target:
            return 0
        # cnt = Counter(nums)
        n = len(nums)
        nums.sort()
        nums2 = [int(math.log2(num)) for num in nums]
        max_k = max(nums2) # 最大的k
        # DP
        # dp[i] 表示從數組中湊出和為 i 的子序列，最少需要的操作數
        # dp[i] = min(dp[i], dp[i - nums[j]] + 1)
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for num in nums:
            if num <= target:
                dp[num] = 0
        # exp2 = [0 for _ in range(32)] # 表示 2^k需要的操作數
        # # print(max_k)
        # for i in range(max_k, 0, -1):
        #     if 2**i in nums:   # 2^i在nums中
        #         exp2[i] = 0
        #     else:               # 2^i不在nums中
        #         exp2[i] = exp2[i+1] + 1
        # # print(exp2[:max_k+1])
        # print(nums2)
        cnt = Counter(nums)
        for i in range(1, target + 1):
            for j in range(n):
                if i - nums[j] in nums:
                    dp[i] = min(dp[i], dp[i - nums[j]])
                for k in range(1, nums2[j]+1): # 2^k
                    # print(i, nums[j], nums2[j], k, nums[j]//(2**k), i - nums[j]//(2**k))
                    if i - nums[j]//(2**k) >= 0:
                        dp[i] = min(dp[i], dp[i - 2**(nums2[j]-k)] + k)
        print(dp)
        return dp[target] if dp[target] != float('inf') else -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations([1,2,8], 7)) # 1
    print(sol.minOperations([1,32,1,2], 12)) # 2
    print(sol.minOperations([1,32,1], 35)) # -1
    print(sol.minOperations([1,1,1,1,1], 5)) # 0

