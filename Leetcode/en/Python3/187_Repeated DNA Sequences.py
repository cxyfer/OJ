# @algorithm @lc id=187 lang=python3 
# @title repeated-dna-sequences


from en.Python3.mod.preImport import *
# @test("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")=["AAAAACCCCC","CCCCCAAAAA"]
# @test("AAAAAAAAAAAAA")=["AAAAAAAAAA"]
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        cnt = Counter()
        for i in range(n - 9):
            cnt[s[i:i+10]] += 1
        return [key for key in cnt if cnt[key] > 1]