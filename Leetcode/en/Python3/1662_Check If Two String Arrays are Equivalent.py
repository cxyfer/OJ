# @algorithm @lc id=1781 lang=python3 
# @title check-if-two-string-arrays-are-equivalent


from en.Python3.mod.preImport import *
# @test(["ab","c"],["a","bc"])=true
# @test(["a","cb"],["ab","c"])=false
# @test(["abc","d","defg"],["abcddefg"])=true
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)
        i = j = ii = jj = 0
        while i < len(word1) and j < len(word2):
            if word1[i][ii] != word2[j][jj]: # 檢查字元是否相等
                return False
            ii += 1
            jj += 1
            if ii == len(word1[i]): # 換word1的下一個字串
                ii = 0
                i += 1
            if jj == len(word2[j]): # 換word2的下一個字串
                jj = 0
                j += 1
        return i == len(word1) and j == len(word2) # 是否已經檢查完所有字串