# @algorithm @lc id=2519 lang=python3 
# @title find-the-original-array-of-prefix-xor


from en.Python3.mod.preImport import *
# @test([5,2,0,3,1])=[5,7,2,3,2]
# @test([13])=[13]
class Solution:
    """
        a ^ a = 0
        b ^ 0 = b
    """
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]