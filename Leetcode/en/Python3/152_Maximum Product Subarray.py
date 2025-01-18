# @algorithm @lc id=152 lang=python3 
# @title maximum-product-subarray


from en.Python3.mod.preImport import *
# @test([2,3,-2,4])=6
# @test([-2,0,-1])=0
class Solution:
    """
        Dynamic Programming
        因為存在負數，所以要記錄最大值和最小值
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        ans = max_val = min_val = nums[0]
        for i in range(1, n):
            if nums[i] < 0: max_val, min_val = min_val, max_val # 遇到負數，最大值和最小值互換
            max_val = max(nums[i], max_val * nums[i]) 
            min_val = min(nums[i], min_val * nums[i])
            ans = max(ans, max_val)
        return ans