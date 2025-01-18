# @algorithm @lc id=392 lang=python3 
# @title is-subsequence


from en.Python3.mod.preImport import *
# @test("abc","ahbgdc")=true
# @test("axc","ahbgdc")=false
class Solution:
    """
        Two pointers
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        slow, fast = 0, 0
        while slow < m and fast < n:
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        return slow == m