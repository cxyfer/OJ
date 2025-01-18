# @algorithm @lc id=389 lang=python3 
# @title find-the-difference


from en.Python3.mod.preImport import *
# @test("abcd","abcde")="e"
# @test("","y")="y"
class Solution:
    """
        1. Counting
        2. Sum
        3. Bit Manipulation
            x ^ x = 0
            x ^ 0 = x
    """
    def findTheDifference(self, s: str, t: str) -> str:
        # return self.counting(s, t)
        # return self.sum(s, t)
        return self.bitManipulation(s, t)

    def counting(self, s: str, t: str) -> str:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        for k in cnt2:
            if cnt1[k] != cnt2[k]:
                return k
        return ""
    
    def sum(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
    
    def bitManipulation(self, s: str, t: str) -> str:
        res = 0
        for ch in s + t:
            res ^= ord(ch)
        return chr(res)