# @algorithm @lc id=2916 lang=python3 
# @title check-if-it-is-possible-to-split-array


from en.Python3.mod.preImport import *
# @test([2,2,1],4)=true
# @test([2,1,3],5)=false
# @test([2,3,3,2,3],6)=true
# @test([4, 1, 3, 2, 4],6)=true
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        # Check if it is possible to split array
        # 只要中間有兩個數字相加大於等於m，就一定可以向左右拆分
        for i in range(n-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return False