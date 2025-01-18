# @algorithm @lc id=2723 lang=python3 
# @title find-the-longest-balanced-substring-of-a-binary-string


from en.Python3.mod.preImport import *
# @test("01000111")=6
# @test("00111")=4
# @test("111")=0
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        cnt0, cnt1 = 0, 0 # 0之後的連續0數量、連續1數量
        for ch in s:
            if ch == '0':
                if cnt1 > 0:
                    cnt0, cnt1 = 0, 0
                cnt0 += 1
            else:
                cnt1 += 1
            ans = max(ans, min(cnt0, cnt1) * 2)
        return ans