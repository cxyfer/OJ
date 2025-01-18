#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from preImport import *
# @lc code=start
class Solution:
    """
        > 基础算法精讲 01
        # Two pointers
        Extend from 167. Sum of Two Numbers II - Input Ordered Array
        i < left < right < n
        滿足三個數字相加等於 0
        
        TS: O(n log n + n^2) = O(n^2)
        SC: O(1), ignore the space of sorting
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        nums.sort()
        # i < left < right < n
        for i in range(n-2): # 枚舉第一個數字 nums[i]
            if i > 0 and nums[i] == nums[i-1]: # 和前一個數字相同，由於題目要求不能有重複數字，跳過
                continue
            """
                一些優化：
                1. 如果 nums[i] > 0，後面的數字都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
                2. 如果 nums[i] 和 最小的兩個數字相加大於 0，則後面任三個數字相加都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
                3. 如果 nums[i] 和 最大的兩個數字相加小於 0，則可以跳過 nums[i] ，因為 nums[i] + nums[left] + nums[right] 只會更小
                   注意這種情況下，枚舉 i 後面的數字仍然有可能有答案，故只需要跳過 i 即可
            """
            if nums[i] > 0: # 1.
                break
            if nums[i] + nums[i+1] + nums[i+2] > 0: # 2.
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0: # 3. 
                continue
            left, right = i+1, n-1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur > 0: # 太大了，右邊的數字太大，往左移
                    right -= 1
                elif cur < 0: # 太小了，左邊的數字太小，往右移
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: # 避免重複答案，跳過
                        left += 1
                    while left < right and nums[right] == nums[right-1]: # 避免重複答案，跳過
                        right -= 1
                    # 找下一個答案
                    left += 1
                    right -= 1
        return ans
# @lc code=end

