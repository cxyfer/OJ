#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#
from preImport import *
# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # dp[i][d] 表示以 nums[i] 結尾，公差為 d 的等差數列的個數
        dp = [defaultdict(int) for _ in range(n)]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j] # 公差
                ans += dp[j][d]
                dp[i][d] += (dp[j][d] + 1)
        return ans
# @lc code=end
sol = Solution()
print(sol.numberOfArithmeticSlices([2,4,6,8,10])) # 7
