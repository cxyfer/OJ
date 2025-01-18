# @algorithm @lc id=345 lang=python3 
# @title reverse-vowels-of-a-string


from en.Python3.mod.preImport import *
# @test("hello")="holle"
# @test("leetcode")="leotcede"
class Solution:
    """
        Two pointers
    """
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        lst = list(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and lst[left] not in "aeiouAEIOU":
                left += 1
            while left < right and lst[right] not in "aeiouAEIOU":
                right -= 1
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return "".join(lst)