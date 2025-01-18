# @algorithm @lc id=125 lang=python3 
# @title valid-palindrome


from en.Python3.mod.preImport import *
# @test("A man, a plan, a canal: Panama")=true
# @test("race a car")=false
# @test(" ")=true
class Solution:
    """
        1. Stack
    """
    def isPalindrome(self, s: str) -> bool:
        ss = [ch for ch in s.lower() if ch.isalnum()]
        n = len(ss)
        st = []
        idx = 0
        while idx < n//2:
            st.append(ss[idx]) # push
            idx += 1
        if n%2 == 1:
            idx += 1
        while idx < n:
            if st.pop() != ss[idx]: # pop
                return False
            idx += 1
        return True