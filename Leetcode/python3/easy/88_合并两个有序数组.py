#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from preImport import *
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        i, j = 0, 0
        while i < m or j < n:
            if i == m:
                ans.append(nums2[j])
                j += 1
            elif j == n or nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        nums1[:] = ans
# @lc code=end
sol = Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3)) # [1,2,2,3,5,6]
print(sol.merge([1],1,[],0)) # [1]
print(sol.merge([0],0,[1],1)) # [1]