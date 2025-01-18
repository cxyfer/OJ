# @algorithm @lc id=3150 lang=python3 
# @title shortest-and-lexicographically-smallest-beautiful-string


from en.Python3.mod.preImport import *
# @test("100011001",3)="11001"
# @test("1011",2)="11"
# @test("000",1)=""
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = s
        n = len(s)
        pos = [i for i in range(n) if s[i] == '1']
        if len(pos) < k:
            return ""
        for i in range(len(pos)-k+1):
            cur = s[pos[i]:pos[i+k-1]+1]
            if len(cur) < len(ans):
                ans = cur
            elif len(cur) == len(ans):
                ans = min(ans, cur)
        return ans