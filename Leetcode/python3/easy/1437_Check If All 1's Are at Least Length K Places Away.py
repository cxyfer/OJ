#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # return all(y - x > k for x, y in pairwise([i for i, x in enumerate(nums) if x == 1]))
        last = float('-inf')
        for i, x in enumerate(nums):
            if x == 1:
                if i - last <= k:
                    return False
                last = i
        return True
# @lc code=end

