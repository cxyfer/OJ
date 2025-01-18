# @algorithm @lc id=2032 lang=python3 
# @title largest-odd-number-in-string


from en.Python3.mod.preImport import *
# @test("52")="5"
# @test("4206")=""
# @test("35427")="35427"
class Solution:
    """
        找到最後一個奇數，返回前面的數字
    """
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""