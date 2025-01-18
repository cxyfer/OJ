# @algorithm @lc id=3207 lang=python3 
# @title make-three-strings-equal


from en.Python3.mod.preImport import *
# @test("abc","abb","ab")=2
# @test("dac","bac","cac")=-1
# @test("a", "a", "a")=0
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        x, y, z = len(s1), len(s2), len(s3)
        n = min(x, y, z)
        # 枚舉剩下的字串
        ans = 0
        for i in range(n):
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break
            ans += 1
        return -1 if ans == 0 else  x+y+z-3*ans