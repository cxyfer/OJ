#
# @lc app=leetcode id=27 lang=python3
# @lcpr version=30204
#
# [27] Remove Element
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        idx = 0
        while i < n:
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
            i += 1
        return idx
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

