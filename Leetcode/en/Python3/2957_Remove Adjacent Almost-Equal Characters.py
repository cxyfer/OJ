# @algorithm @lc id=3230 lang=python3 
# @title remove-adjacent-almost-equal-characters


from en.Python3.mod.preImport import *
# @test("aaaaa")=2
# @test("abddez")=2
# @test("zyxyxyz")=3
class Solution:
    """
        分組循環
    """
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            st = i
            while i + 1 < n and abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                i += 1
            i += 1
            ans += (i - st) // 2
        return ans