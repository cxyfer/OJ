# @algorithm @lc id=238 lang=python3 
# @title product-of-array-except-self


from en.Python3.mod.preImport import *
# @test([1,2,3,4])=[24,12,8,6]
# @test([-1,1,0,-3,3])=[0,0,9,0,0]
class Solution:
    """
        不能使用除法，所以先把左邊的乘起來，再把右邊的乘起來
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left, right = 1, 1 # left, right 分別代表左邊的乘積、右邊的乘積
        for i in range(n): 
            ans[i] *= left 
            left *= nums[i] # update left product
            j = n - 1 - i # 也可以再用一個for loop，for j in range(n - 1, -1, -1):
            ans[j] *= right
            right *= nums[j] # update right product
        return ans