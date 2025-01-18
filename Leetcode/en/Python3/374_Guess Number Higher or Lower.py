# @algorithm @lc id=374 lang=python3 
# @title guess-number-higher-or-lower


from en.Python3.mod.preImport import *
# @test(10,6)=6
# @test(1,1)=1
# @test(2,1)=1
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid-1
            else:
                left = mid+1
        return -1