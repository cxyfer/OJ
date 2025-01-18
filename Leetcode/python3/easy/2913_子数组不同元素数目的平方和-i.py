#
# @lc app=leetcode.cn id=2913 lang=python3
#
# [2913] 子数组不同元素数目的平方和 I
#

# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(1, n+1):
            for i in range(n-l+1):
                ans += len(set(nums[i:i+l]))** 2
        return ans
# @lc code=end

