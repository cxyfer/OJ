# @algorithm @lc id=2698 lang=python3 
# @title find-the-array-concatenation-value


from en.Python3.mod.preImport import *
# @test([7,52,2,4])=596
# @test([5,14,13,8,12])=673
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = 0
        while (left <= right):
            if left == right:
                ans += nums[left]
            else:
                ans += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        return ans