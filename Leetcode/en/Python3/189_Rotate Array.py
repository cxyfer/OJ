# @algorithm @lc id=189 lang=python3 
# @title rotate-array


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6,7],3)=[5,6,7,1,2,3,4]
# @test([-1,-100,3,99],2)=[3,99,-1,-100]
class Solution:
    """
        1. reverse all
        2. reverse first k elements
        3. reverse last n-k elements
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # k 可能大於 n
        if k == 0:
            return
        
        nums.reverse() # 1. reverse all
        nums[:k] = reversed(nums[:k]) # 2. reverse first k elements
        nums[k:] = reversed(nums[k:]) # 3. reverse last n-k elements
        