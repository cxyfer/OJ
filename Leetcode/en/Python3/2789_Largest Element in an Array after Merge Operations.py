# @algorithm @lc id=2872 lang=python3 
# @title largest-element-in-an-array-after-merge-operations


from en.Python3.mod.preImport import *
# @test([2,3,7,9,3])=21
# @test([5,3,3])=11
class Solution:
    """
        Greedy，由後往前合併
    """
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] <= s: # 可以合併
                s += nums[i]
            else:
                s = nums[i]
        return s