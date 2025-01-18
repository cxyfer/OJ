# @algorithm @lc id=1884 lang=python3 
# @title minimum-changes-to-make-alternating-binary-string


from en.Python3.mod.preImport import *
# @test("0100")=1
# @test("10")=0
# @test("1111")=2
class Solution:
    def minOperations(self, s: str) -> int:
        # return min(sum([(ch == '1') if i % 2 == 0 else (ch == '0') for i, ch in enumerate(s)]), sum([(ch == '0') if i % 2 == 0 else (ch == '1') for i, ch in enumerate(s)]))
        ans1 = ans2 = 0
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch == '1':
                    ans1 += 1
                else:
                    ans2 += 1
            else:
                if ch == '0':
                    ans1 += 1
                else:
                    ans2 += 1
        return min(ans1, ans2)