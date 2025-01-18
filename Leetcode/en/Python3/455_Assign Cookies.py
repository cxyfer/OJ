# @algorithm @lc id=455 lang=python3 
# @title assign-cookies


from en.Python3.mod.preImport import *
# @test([1,2,3],[1,1])=1
# @test([1,2],[1,2,3])=2
class Solution:
    """
        Greedy
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        g.sort()
        s.sort()
        ans = 0
        i = j = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
                ans += 1
            j += 1
        return ans