# @algorithm @lc id=2614 lang=python3 
# @title maximum-count-of-positive-integer-and-negative-integer


from en.Python3.mod.preImport import *
# @test([-2,-1,-1,1,2,3])=3
# @test([-3,-2,-1,0,0,1,2])=3
# @test([5,20,66,1314])=4
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_left(nums: List[int], target: int) -> int: # find the leftmost target
            n = len(nums)
            left, right = 0, n - 1 # [left, right]
            while left <= right: # 區間不為空
                # mid = left + (right - left) // 2
                mid = (left + right) // 2 
                if nums[mid] < target: # [mid+1, right]
                    left = mid + 1 
                else: # [left, mid-1]
                    right = mid - 1
            return left # or right+1
        neg = find_left(nums, 0)
        pos = len(nums) - find_left(nums, 1)
        return max(neg, pos)