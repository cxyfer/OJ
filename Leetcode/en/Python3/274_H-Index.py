# @algorithm @lc id=274 lang=python3 
# @title h-index


from en.Python3.mod.preImport import *
# @test([3,0,6,1,5])=3
# @test([1,3,1])=1
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = Counter([min(n, x) for x in citations])
        s = 0
        for i in range(n, -1, -1):
            s += cnt[i]
            if s >= i:
                return i