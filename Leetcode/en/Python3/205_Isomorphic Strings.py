# @algorithm @lc id=205 lang=python3 
# @title isomorphic-strings


from en.Python3.mod.preImport import *
# @test("egg","add")=true
# @test("foo","bar")=false
# @test("paper","title")=true
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mp = defaultdict(str)
        used = set()
        for i in range(n):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                mp[s[i]] = t[i]
                used.add(t[i])
        return True