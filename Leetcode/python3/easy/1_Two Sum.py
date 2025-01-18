#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30201
#
# [1] Two Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tbl = dict()
        for idx, num in enumerate(nums):
            if target - num in tbl:
                return [tbl[target - num], idx]
            tbl[num] = idx
        return []
# @lc code=end

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

