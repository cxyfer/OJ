#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            1. Merge Two Sorted Array
            Time: O(m+n)
        """
        # m, n = len(nums1), len(nums2)
        # mid = (m+n)//2
        # i, j = 0, 0
        # nums = []
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         nums.append(nums1[i])
        #         i+=1
        #     else:
        #         nums.append(nums2[j])
        #         j+=1
        # if i < m:
        #     nums.extend(nums1[i:])
        # if j < n:
        #     nums.extend(nums2[j:])
        # return (nums[mid-1]+nums[mid])/2 if (m+n)%2 == 0 else nums[mid]
        """
            2. Binary Search
            Time: O(log(min(m,n)))
        """
        m, n = len(nums1), len(nums2)
        def getKthElement(k):
            i, j = 0, 0
            while True:
                # 特殊情况
                if i == m:
                    return nums2[j + k - 1]
                if j == n:
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])
                
                ni = min(i + k // 2 - 1, m - 1)
                nj = min(j + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[ni], nums2[nj]
                if pivot1 <= pivot2:
                    k -= ni - i + 1
                    i = ni + 1
                else:
                    k -= nj - j + 1
                    j = nj + 1
        if (m + n) % 2 == 1:
            return getKthElement(((m + n) + 1) // 2)
        else:
            return (getKthElement((m + n) // 2) + getKthElement((m + n) // 2 + 1)) / 2
# @lc code=end
sol = Solution()
print(sol.findMedianSortedArrays([2,2,2,2],[2,2,2])) # 1
print(sol.findMedianSortedArrays([1,3],[2])) # 2.00000
print(sol.findMedianSortedArrays([1,2],[3,4])) # 2.50000
print(sol.findMedianSortedArrays([1,2,3,4,5],[6])) # 3.50000
print(sol.findMedianSortedArrays([1,2,3,4,5,6],[7])) # 4
print(sol.findMedianSortedArrays([7], [1,2,3,4,5,6])) # 4