# @algorithm @lc id=768 lang=python3 
# @title partition-labels


from en.Python3.mod.preImport import *
# @test("ababcbacadefegdehijhklij")=[9,7,8]
# @test("eccbbbbdec")=[10]
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, ch in enumerate(s):
            last[ch] = i
        
        ans = []
        st = ed = 0
        for i, ch in enumerate(s):
            ed = max(ed, last[ch])
            if i == ed:
                ans.append(ed - st + 1)
                st = ed + 1
        return ans

