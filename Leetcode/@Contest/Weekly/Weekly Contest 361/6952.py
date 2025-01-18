# 6952. Count of Interesting Subarrays

# You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

# Your task is to find the count of subarrays that are interesting.

# A subarray nums[l..r] is interesting if the following condition holds:

# Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
# Return an integer denoting the count of interesting subarrays.

# Note: A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List
from collections import Counter 
from functools import cache

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        ans = 0
        mod_k = [x % modulo == k for x in nums]
        sum_k = [mod_k[0]] + [0] * (n-1)
        for i in range(1, n):
            sum_k[i] = sum_k[i-1] + mod_k[i]


        # DP
        # dp2[j] 表示從 i=0-j 表示從i到j的subarray 有幾個 sum(mod_k[i:j+1]) % modulo == k
        # dp[j][m] 表示從 從i到j的subarray(i=0-j)，cnt%modulo為m的subarray有幾個
        dp = [[0] * modulo for _ in range(n)]
        for i in range(n):
            dp[i][int(mod_k[i])] = 1
        dp[0][int(nums[0] % modulo == k)] = 1
        print(dp)
        for i in range(1, n):
            moduler = nums[i] % modulo
            for j in range(modulo):
                # 考慮只取自己的情況
                if nums[i] % modulo == k: # 即取nums[i]會影響cnt
                    dp[i][j] += dp[i-1][j-1] + 1
                    # dp[i][1] += 1
                else:
                    dp[i][j] += dp[i-1][j] + 1
                    # dp[i][0] += 1
        print(dp)
        return ans



        # for i in range(1, n):
        #     if nums[i] % modulo == k: # 即取nums[i]會影響cnt
        #         # 只取nums[i]或把nums[i]加到前面的subarray
        #         dp[i] = dp[i-1] + 1 + int (( dp[i-1] + 1 ) % modulo == k)
        #     else:
        #         dp[i] = dp[i-1]
        # return dp[-1]
    
        # TLE
        # for i in range(n):
        #     for j in range(i, n):
        #         cnt = sum(mod_k[i:j+1])
        #         if (cnt % modulo) == k:
        #             ans += 1

        return ans
    
sol = Solution()
print(sol.countInterestingSubarrays([3,2,4], 2, 1)) # 3 
print(sol.countInterestingSubarrays([3,1,9,6], 3, 0)) # 2
print(sol.countInterestingSubarrays([11,12,21,31], 10, 1)) # 5


