#
# @lc app=leetcode id=75 lang=python3
# @lcpr version=30204
#
# [75] Sort Colors
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Two Pointer
把 0 放到前面、把 2 放到後面，這樣 1 自然就會在中間
這個思路與 3-Way QuickSort 相同
Reference:
- https://www.bilibili.com/video/BV1Q4421Z74Y/
"""
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        l, r = 0, n - 1
        while i <= r:
            if nums[i] == 0:  # 這裡交換過來的數字一定是 1
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:  # 這裡交換過來的數字可能是 0 或 2，因此還要檢查新的 nums[i]
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                continue
            i += 1
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

