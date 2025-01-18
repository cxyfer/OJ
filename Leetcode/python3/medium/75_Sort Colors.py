#
# @lc app=leetcode id=75 lang=python3
# @lcpr version=30204
#
# [75] Sort Colors
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Two Pointer
        把 0 放到前面，2 放到後面，1 就會在中間
        這個思路與 3-Way QuickSort 相同
        Reference:
        - https://www.bilibili.com/video/BV1Q4421Z74Y/
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r, idx = 0, n-1, 0
        while idx <= r:  # 小於 l 的位置都是 0，大於 r 的位置都是 2
            if nums[idx] == 0:  # 把 0 放到前面
                nums[l], nums[idx] = nums[idx], nums[l]
                l += 1
                idx += 1
            elif nums[idx] == 2:  # 把 2 放到後面，這裡要注意交換來的數字可能是 2，因此 idx 不能 +1
                nums[r], nums[idx] = nums[idx], nums[r]
                r -= 1
            else:
                idx += 1
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

