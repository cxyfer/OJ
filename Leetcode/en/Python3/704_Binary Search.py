# @algorithm @lc id=792 lang=python3 
# @title binary-search


from en.Python3.mod.preImport import *
# @test([-1,0,3,5,9,12],9)=4
# @test([-1,0,3,5,9,12],2)=-1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid
            else: left = mid + 1
        return -1