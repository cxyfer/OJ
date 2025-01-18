# @algorithm @lc id=2456 lang=python3 
# @title construct-smallest-number-from-di-string


from en.Python3.mod.preImport import *
# @test("IIIDIDDD")="123549876"
# @test("DDD")="4321"
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = list("123456789")[:n+1]
        idx = 0
        while (idx < n):
            if pattern[idx] == "I":
                idx += 1
            else:
                i = idx # Start of the D
                while (idx < n and pattern[idx] == "D"):
                    idx += 1
                # pattern[i:idx+1] are all D
                # So we need to reverse ans[i:idx+1]
                ans[i:idx+1] = reversed(ans[i:idx+1])
        return "".join(ans)