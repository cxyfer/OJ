# @algorithm @lc id=3220 lang=python3 
# @title count-tested-devices-after-test-operations


from en.Python3.mod.preImport import *
# @test([1,1,2,1,3])=3
# @test([0,1,2])=2
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i, x in enumerate(batteryPercentages):
            if x - ans > 0:
                ans += 1
        return ans