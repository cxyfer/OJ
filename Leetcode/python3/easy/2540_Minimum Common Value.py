#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1)
# @lc code=end

nums1 = [1,2,3]
nums2 = [4]

sol = Solution()
print(sol.getCommon(nums1, nums2))