# @algorithm @lc id=292 lang=python3 
# @title nim-game


from en.Python3.mod.preImport import *
# @test(4)=false
# @test(1)=true
# @test(2)=true
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0