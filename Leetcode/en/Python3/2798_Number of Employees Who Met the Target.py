# @algorithm @lc id=2876 lang=python3 
# @title number-of-employees-who-met-the-target


from en.Python3.mod.preImport import *
# @test([0,1,2,3,4],2)=3
# @test([5,1,4,2,2],6)=0
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([h >= target for h in hours])