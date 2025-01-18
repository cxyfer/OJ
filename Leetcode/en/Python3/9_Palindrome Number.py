# @algorithm @lc id=9 lang=python3 
# @title palindrome-number


from en.Python3.mod.preImport import *
# @test(121)=true
# @test(-121)=false
# @test(10)=false
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # Reverse half of the number
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x //= 10
        return x == res or x == res // 10 # even or odd