# @algorithm @lc id=1814 lang=python3 
# @title jump-game-vi


from en.Python3.mod.preImport import *
# @test([1,-1,-2,4,-7,3],2)=7
# @test([10,-5,-2,4,0,3],3)=17
# @test([1,-5,-20,4,-1,3,-6,-3],2)=0
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hp = [] # max heap
        ans = nums[0]
        heappush(hp, (-nums[0], 0)) # (value, index)
        for i in range(1, n):
            while hp and i - hp[0][1] > k: # index distance is too large
                heappop(hp)
            ans = -hp[0][0] + nums[i]
            heappush(hp, (-ans, i))
        return ans