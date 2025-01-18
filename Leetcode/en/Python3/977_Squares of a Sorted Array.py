# @algorithm @lc id=1019 lang=python3 
# @title squares-of-a-sorted-array


from en.Python3.mod.preImport import *
# @test([-4,-1,0,3,10])=[0,1,9,16,100]
# @test([-7,-3,2,3,11])=[4,9,9,49,121]
class Solution:
    """
        Two pointers
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        left, right = 0, n - 1
        # idx = n - 1
        while (left <= right):
            if abs(nums[left]) < abs(nums[right]):
                ans[right - left] = nums[right] ** 2
                right -= 1
            else:
                ans[right - left] = nums[left] ** 2
                left += 1
            # idx -= 1
        return ans