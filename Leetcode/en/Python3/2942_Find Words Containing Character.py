# @algorithm @lc id=3194 lang=python3 
# @title find-words-containing-character


from en.Python3.mod.preImport import *
# @test(["leet","code"],"e")=[0,1]
# @test(["abc","bcd","aaaa","cbc"],"a")=[0,2]
# @test(["abc","bcd","aaaa","cbc"],"z")=[]
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # return [idx for idx, word in enumerate(words) if x in word]
        ans = []
        for idx, word in enumerate(words):
            if x in word:
                ans.append(idx)
        return ans