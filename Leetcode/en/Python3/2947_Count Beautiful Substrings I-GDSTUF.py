# @algorithm @lc id=3210 lang=python3 
# @title count-beautiful-substrings-i


from en.Python3.mod.preImport import *
# @test("baeyh",2)=2
# @test("abba",1)=3
# @test("bcdf",1)=0
class Solution:
    """
        Brute Force + Prefix Sum
    """
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        vowels = consonants = 0
        pre_v = [0] * (n+1)  
        pre_c = [0] * (n+1)
        for i in range(n):
            if s[i] in "aeiou":
                vowels += 1
            else:
                consonants += 1
            pre_v[i+1] = vowels
            pre_c[i+1] = consonants
        for i in range(n): # 枚舉起點
            for j in range(i + 1, n+1): # 枚舉終點
                vowels = pre_v[j] - pre_v[i]
                consonants = pre_c[j] - pre_c[i]
                if vowels == consonants and vowels * consonants % k == 0:
                    ans += 1
        return ans