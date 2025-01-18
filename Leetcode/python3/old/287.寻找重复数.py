#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
from en.Python3.mod.preImport import *
# @lc code=start
"""
    You must solve the problem without modifying the array nums and uses only constant extra space.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
            1. Hash Table
            顯然不符合題目的空間要求
        """
        # return Counter(nums).most_common(1)[0][0]
        """
            2. Binary Search
            計算小於等於 mid 的元素個數，如果個數小於等於 mid，則重複元素比mid大，否則比mid小
        """
        n = len(nums)
        left, right = 1, n-1 # 左閉右閉
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            cnt = sum(x <= mid for x in nums)
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
# @lc code=end
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))
print(sol.findDuplicate([3,1,3,4,2]))

