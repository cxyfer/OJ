# @algorithm @lc id=646 lang=python3 
# @title maximum-length-of-pair-chain


from en.Python3.mod.preImport import *
import math
# @test([[1,2],[2,3],[3,4]])=2
# @test([[1,2],[7,8],[4,5]])=3
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Greedy
        cur = -math.inf # current end
        ans = 0
        pairs.sort(key=lambda x: x[1])
        for x, y in pairs:
            if x > cur:
                cur = y
                ans += 1
        return ans