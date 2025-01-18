# @algorithm @lc id=1850 lang=python3 
# @title minimum-length-of-string-after-deleting-similar-ends


from en.Python3.mod.preImport import *
# @test("ca")=2
# @test("cabaabac")=0
# @test("aabccabba")=3
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        while left < right and s[left] == s[right]: # 存在由相同字元構成的前綴和後綴
            ch = s[left]
            while left <= right and s[left] == ch: # 刪除由 ch 構成的前綴
                left += 1
            while left <= right and s[right] == ch: # 刪除由 ch 構成的後綴
                right -= 1
        return right - left + 1