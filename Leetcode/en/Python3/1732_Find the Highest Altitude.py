# @algorithm @lc id=1833 lang=python3 
# @title find-the-highest-altitude


from en.Python3.mod.preImport import *
# @test([-5,1,5,0,-7])=1
# @test([-4,-3,-2,-1,4,3,2])=0
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for i in gain:
            prefix.append(prefix[-1] + i)
        return max(prefix)