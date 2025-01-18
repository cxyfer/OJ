# @algorithm @lc id=1319 lang=python3 
# @title unique-number-of-occurrences


from en.Python3.mod.preImport import *
# @test([1,2,2,1,1,3])=true
# @test([1,2])=false
# @test([-3,0,1,-3,1,1,1,-3,10,0])=true
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(v == 1 for v in Counter(Counter(arr).values()).values())