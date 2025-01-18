#
# @lc app=leetcode id=88 lang=python3
# @lcpr version=30204
#
# [88] Merge Sorted Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
逆序双指针，由大到小避免覆蓋 nums1 的元素
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        idx = m + n - 1
        # while idx >= 0:
        #     if i >= 0 and j >= 0 and nums1[i] > nums2[j] or j < 0:
        #         nums1[idx] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[idx] = nums2[j]
        #         j -= 1
        #     idx -= 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#

