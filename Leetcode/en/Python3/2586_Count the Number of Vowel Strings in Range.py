# @algorithm @lc id=2654 lang=python3 
# @title count-the-number-of-vowel-strings-in-range


from en.Python3.mod.preImport import *
# @test(["are","amy","u"],0,2)=2
# @test(["hey","aeo","mu","ooo","artro"],1,4)=3
class Solution:
    VOWEL = ['a','e','i','o','u']
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum([word[0] in self.VOWEL and word[-1] in self.VOWEL for word in words[left:right+1]])
        