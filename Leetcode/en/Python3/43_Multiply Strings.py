# @algorithm @lc id=43 lang=python3 
# @title multiply-strings


from en.Python3.mod.preImport import *
# @test("2","3")="6"
# @test("123","456")="56088"
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
        