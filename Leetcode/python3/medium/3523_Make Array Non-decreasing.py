#
# @lc app=leetcode id=3523 lang=python3
#
# [3523] Make Array Non-decreasing
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        pre = nums[0]
        for i in range(1, n):
            if pre > nums[i]:  # 需要刪除 nums[i]
                ans -= 1
            else:
                pre = nums[i]
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumPossibleSize([1,2,3]))  # 3
print(sol.maximumPossibleSize([19,80,63,74]))  # 2