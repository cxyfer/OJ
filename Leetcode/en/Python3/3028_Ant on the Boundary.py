# @algorithm @lc id=3311 lang=python3 
# @title ant-on-the-boundary


from en.Python3.mod.preImport import *
# @test([2,3,-5])=1
# @test([3,2,-3,-4])=0
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for x in nums:
            cur += x
            if cur == 0:
                ans += 1
        return ans
        