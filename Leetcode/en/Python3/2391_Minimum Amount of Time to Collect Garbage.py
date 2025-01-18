# @algorithm @lc id=2471 lang=python3 
# @title minimum-amount-of-time-to-collect-garbage


from en.Python3.mod.preImport import *
# @test(["G","P","GP","GG"],[2,4,3])=21
# @test(["MMM","PGM","GP"],[3,10])=37
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        m, p, g = 0, 0, 0 # 三種垃圾車所需要行駛的距離
        pre = [0] + list(accumulate(travel)) # 前綴和
        for i, s in enumerate(garbage):
            ans += len(s) # 所有垃圾的收集時間都是1
            if "M" in s:
                m = i
            if "P" in s:
                p = i
            if "G" in s:
                g = i
        return ans + pre[m] + pre[p] + pre[g]