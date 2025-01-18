# @algorithm @lc id=2231 lang=python3 
# @title find-first-palindromic-string-in-the-array


from en.Python3.mod.preImport import *
# @test(["abc","car","ada","racecar","cool"])="ada"
# @test(["notapalindrome","racecar"])="racecar"
# @test(["def","ghi"])=""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-1-i]:
                    return False
            return True
        for word in words:
            if isPalindrome(word):
                return word
        return ""
        