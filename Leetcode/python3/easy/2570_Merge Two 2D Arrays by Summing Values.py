#
# @lc app=leetcode id=2570 lang=python3
# @lcpr version=30204
#
# [2570] Merge Two 2D Arrays by Summing Values
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        i = j = 0
        ans = []
        while i < n or j < m:
            if j == m or (i < n and nums1[i][0] < nums2[j][0]):
                ans.append((nums1[i][0], nums1[i][1]))
                i += 1
            elif i == n or (j < m and nums1[i][0] > nums2[j][0]):
                ans.append((nums2[j][0], nums2[j][1]))
                j += 1
            else:
                ans.append((nums1[i][0], nums1[i][1] + nums2[j][1]))
                i += 1
                j += 1
        return ans
# @lc code=end

#
# @lcpr case=start
# [[1,2],[2,3],[4,5]]\n[[1,4],[3,2],[4,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,6],[5,5]]\n[[1,3],[4,3]]\n
# @lcpr case=end

#

