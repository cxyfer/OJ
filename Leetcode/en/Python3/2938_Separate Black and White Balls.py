# @algorithm @lc id=3195 lang=python3 
# @title separate-black-and-white-balls


from en.Python3.mod.preImport import *
# @test("101")=1
# @test("100")=2
# @test("0111")=0
class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            while left < n and s[left] == '0':
                left += 1
            while right >= 0 and s[right] == '1':
                right -= 1
            if left < right:
                ans += right - left
            left += 1
            right -= 1
        return ans
        