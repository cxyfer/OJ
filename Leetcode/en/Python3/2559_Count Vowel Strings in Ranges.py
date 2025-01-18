# @algorithm @lc id=2691 lang=python3 
# @title count-vowel-strings-in-ranges


from en.Python3.mod.preImport import *
# @test(["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]])=[2,3,0]
# @test(["a","e","i"],[[0,2],[0,1],[2,2]])=[3,2,1]
class Solution:
    """
        Prefix Sum
    """
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = [0] * (len(words)+1)
        vowels = "aeiou"
        for i, w in enumerate(words):
            s[i+1] = s[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)
        return [s[r+1] - s[l] for l, r in queries]