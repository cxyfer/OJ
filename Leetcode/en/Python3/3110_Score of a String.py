# @algorithm @lc id=3379 lang=python3 
# @title score-of-a-string


from en.Python3.mod.preImport import *
# @test("hello")=13
# @test("zaz")=50
class Solution:
    def scoreOfString(self, s: str) -> int:
        # return sum(abs(x - y) for x, y in pairwise(map(ord, s)))
        n = len(s)
        ans = 0
        for i in range(1, n):
            ans += abs(ord(s[i]) - ord(s[i - 1]))
        return ans