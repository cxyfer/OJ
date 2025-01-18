#
# @lc app=leetcode id=2974 lang=python3
# @lcpr version=30204
#
# [2974] Minimum Number Game
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for i in range(0, n, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
# @lc code=end



#
# @lcpr case=start
# [5,4,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n
# @lcpr case=end

#

