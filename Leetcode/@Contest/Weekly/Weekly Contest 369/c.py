# You are given a 0-indexed integer array nums having length n, and an integer k.

# You can perform the following increment operation any number of times (including zero):

# Choose an index i in the range [0, n - 1], and increase nums[i] by 1.
# An array is considered beautiful if, for any subarray with a size of 3 or more, its maximum element is greater than or equal to k.

# Return an integer denoting the minimum number of increment operations needed to make nums beautiful.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    # dp[i][j] 表示nums[:i+1]且以nums[j]作為subarray最後一個>=k的值的最小操作次數
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            
            for j in range(i+1):
                if nums[i] >= k:
                    dp[i][j] = 0
                elif nums[i] < k:
                    dp[i][j] = dp[i-1][j] + 1
            if nums[i] < k:
                dp[i][i] = 0

        return 

sol = Solution()
print(sol.minIncrementOperations([2,3,0,0,2], 4)) # 3
print(sol.minIncrementOperations([0,1,3,3], 5)) # 2
print(sol.minIncrementOperations([1,1,2], 1)) # 0

print(sol.minIncrementOperations([1,2,3,4,5], 3)) # 0