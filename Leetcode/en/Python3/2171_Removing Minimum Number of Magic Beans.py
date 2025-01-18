# @algorithm @lc id=2290 lang=python3 
# @title removing-minimum-number-of-magic-beans


from en.Python3.mod.preImport import *
# @test([4,1,6,5])=4
# @test([2,10,3,2])=7
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        s = list(accumulate(beans, initial=0))
        ans = s[n]
        for i, b in enumerate(beans):
            p1 = s[i] # < b 的全部拿出
            p2 = s[n] - s[i+1] - b * (n - i - 1) # > b 的減到 b
            ans = min(ans, p1 + p2)
        return ans