# @algorithm @lc id=1503 lang=python3 
# @title reducing-dishes


from en.Python3.mod.preImport import *
# @test([-1,-8,0,5,-9])=14
# @test([4,3,2])=20
# @test([-1,-4,-5])=0
class Solution:
    """
        Prefix sum
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        ans = 0
        for s in accumulate(satisfaction): # prefix sum
            if s < 0:
                break
            ans += s
        return ans