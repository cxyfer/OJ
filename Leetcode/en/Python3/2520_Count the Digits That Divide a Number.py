# @algorithm @lc id=2608 lang=python3 
# @title count-the-digits-that-divide-a-number


from en.Python3.mod.preImport import *
# @test(7)=1
# @test(121)=2
# @test(1248)=4
class Solution:
    def countDigits(self, num: int) -> int:
        nums = map(int, list(str(num)))
        return sum([1 for i in nums if i != 0 and num % i == 0])