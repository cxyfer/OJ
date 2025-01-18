# @algorithm @lc id=2049 lang=python3 
# @title eliminate-maximum-number-of-monsters


from en.Python3.mod.preImport import *
# @test([1,3,4],[1,1,1])=3
# @test([1,1,2,3],[1,1,1,1])=1
# @test([3,2,4],[5,3,2])=1
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivalTimes = sorted([math.ceil(d/s) for d, s in zip(dist, speed)])
        for attackTime, arrivalTime in enumerate(arrivalTimes):
            if arrivalTime <= attackTime: # 來不及消滅
                return attackTime
        return len(arrivalTimes)