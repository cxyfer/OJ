# @algorithm @lc id=2887 lang=python3 
# @title sort-vowels-in-a-string


from en.Python3.mod.preImport import *
# @test("lEetcOde")="lEOtcede"
# @test("lYmpH")="lYmpH"
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([ch for ch in s if ch in "AEIOUaeiou"], reverse = True)
        return ''.join(vowels.pop() if ch in "AEIOUaeiou" else ch for ch in s)
