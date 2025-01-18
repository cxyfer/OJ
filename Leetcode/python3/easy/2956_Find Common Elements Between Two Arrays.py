#
# @lc app=leetcode id=2956 lang=python3
# @lcpr version=30204
#
# [2956] Find Common Elements Between Two Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = sum([1 for x in nums1 if x in set2])
        ans2 = sum([1 for x in nums2 if x in set1])
        return [ans1, ans2]
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,3,1]\n[2,2,5,2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,2,3]\n[1,5]\n
# @lcpr case=end

#

