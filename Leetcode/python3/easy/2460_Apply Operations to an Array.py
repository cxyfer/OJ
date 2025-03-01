#
# @lc app=leetcode.cn id=2460 lang=python3
# @lcpr version=30204
#
# [2460] 对数组执行操作
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = 0
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

