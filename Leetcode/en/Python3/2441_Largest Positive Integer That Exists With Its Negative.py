# @algorithm @lc id=2524 lang=python3 
# @title largest-positive-integer-that-exists-with-its-negative


from en.Python3.mod.preImport import *
# @test([-1,2,-3,3])=3
# @test([-1,10,6,7,-7,1])=7
# @test([-10,8,6,7,-2,-3])=-1
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        visited = set()
        for x in nums:
            if -x in visited:
                ans = max(ans, abs(x))
            visited.add(x)
        return ans