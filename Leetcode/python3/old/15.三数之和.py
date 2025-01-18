#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers
        # Extend from 167. Sum of Two Numbers II - Input Ordered Array
        nums.sort()
        n = len(nums)
        ans = []
        # i < left < right
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: # 不能有重複的 triplets 
                continue
            # Optimization
            if nums[i] + nums[i+1] + nums[i+2] > 0: # 後面不可能有等於 0 的 triplets
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0: # 後面不可能有等於 0 的 triplets
                continue
            # Two pointers
            left, right = i+1, n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0: # too large
                    right -= 1
                elif sum < 0: # too small
                    left += 1
                else: # find a triplet
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]: # 不能有重複的 triplets
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]: # 不能有重複的 triplets
                        right -= 1
                    if nums[right] == nums[right+1]: # 不能有重複的 triplets
                        right -= 1
        return ans
# @lc code=end

