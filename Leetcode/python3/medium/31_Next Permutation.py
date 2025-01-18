#
# @lc app=leetcode id=31 lang=python3
# @lcpr version=30204
#
# [31] Next Permutation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1): # find the first increasing element
            if nums[i] < nums[i+1]: # nums[i] < nums[i+1] >= nums[i+2] >= ... >= nums[n-1]
                for j in range(n-1, i, -1): # find the first element that is larger than nums[i]
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i] # swap nums[i] and nums[j]
                        break
                nums[i+1:] = nums[i+1:][::-1]
                return
        nums.reverse()
        return

class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 由後往前找到第一個滿足 nums[i] < nums[i+1] 的位置
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 此時 nums[i] < nums[i+1] >= nums[i+2] >= ... >= nums[n-1]
        # 如果 i < 0，則 nums 已經是最大排列，根據題意，其下個排列為最小排列，故翻轉 nums 即可
        if i >= 0:
            # 由後往前找到第一個大於 nums[i] 的元素 nums[j]，交換兩者
            # 此時 nums[j] < nums[i+1] >= ... >= nums[i] >= ... >= nums[n-1]
            # 翻轉 nums[i+1:] 即為答案
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 兩種情況的翻轉可以寫在一起
        nums[i+1:] = nums[i+1:][::-1]
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

"""
idx:    0, 1, 2, 3, 4, 5, 6, 7
val:    1, 3, 2, 3, 6, 5, 5, 2
                 ^

"""

sol = Solution()
sol.nextPermutation(arr := [1,2,3])
print(arr)
sol.nextPermutation(arr := [3,2,1])
print(arr)
sol.nextPermutation(arr := [1,3,2,3,6,5,5,2])
print(arr)
#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#

