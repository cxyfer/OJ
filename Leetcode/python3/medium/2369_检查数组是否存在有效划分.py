#
# @lc app=leetcode.cn id=2369 lang=python3
#
# [2369] 检查数组是否存在有效划分
#
from preImport import *
# @lc code=start

class Solution:
    """
        DP
        令 dp[i] 表示 nums[:i] 是否存在Valid Partition
    """
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        for i, x in enumerate(nums):
            if i > 0 and dp[i - 1] and x == nums[i - 1]: # 情況1
                dp[i + 1] = True
            elif i > 1 and dp[i - 2]: # 情況2/3
                if (x == nums[i - 1] == nums[i - 2]) or (x == nums[i - 1] + 1 == nums[i - 2] + 2):
                    dp[i + 1] = True
        return dp[n]
# @lc code=end
sol = Solution()
print(sol.validPartition([4, 4, 4, 5, 6]))  # True
print(sol.validPartition([1, 1, 1, 2]))  # False
