# @algorithm @lc id=2977 lang=python3 
# @title check-if-a-string-is-an-acronym-of-words


from en.Python3.mod.preImport import *
# @test(["alice","bob","charlie"],"abc")=true
# @test(["an","apple"],"a")=false
# @test(["never","gonna","give","up","on","you"],"ngguoy")=true
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        idx = 0
        n = len(s)
        if len(words) != n:
            return False
        for word in words:
            if word[0] != s[idx]:
                return False
            idx += 1
        return True

        # if len(words) != len(s):
        #     return False
        # return all(w[0] == c for w, c in zip(words, s))