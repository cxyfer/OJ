# @algorithm @lc id=2857 lang=python3 
# @title total-distance-traveled


from en.Python3.mod.preImport import *
# @test(5,10)=60
# @test(1,2)=10
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5 and additionalTank:
            q, r = divmod(mainTank, 5)
            ans += 5 * q * 10
            used = min(q, additionalTank)
            mainTank = r + used
            additionalTank -= used
        ans += mainTank * 10
        return ans