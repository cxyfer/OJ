# @algorithm @lc id=3104 lang=python3 
# @title happy-students


from en.Python3.mod.preImport import *
# @test([1,1])=2
# @test([6,0,3,3,6,7,2,7])=3
class Solution:
    """
        Greedy
        若要選k人，一定優先選nums[i]最小的k個人
    """
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 1 if nums[0] > 0 else 0 # 能不能全部都不選
        for k in range(1, n): 
            if nums[k-1] < k < nums[k]:
                ans += 1
        return ans + 1 # 加上全部都選

