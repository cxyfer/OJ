# @algorithm @lc id=3346 lang=python3 
# @title lexicographically-smallest-string-after-operations-with-constraint


from en.Python3.mod.preImport import *
# @test("zbbz",3)="aaaz"
# @test("xaxcd",4)="aawcd"
# @test("lol",0)="lol"
class Solution:
    """
        Greedy
        盡可能讓前面的字串改成 'a'，這樣字典序會最小
        Time: O(n)
    """
    def getSmallestString(self, s: str, k: int) -> str:
        s = list(s)
        for i, ch in enumerate(s):
            dis = min(ord(ch) - ord('a'), ord('z') - ord(ch) + 1)
            if dis > k:
                s[i] = chr(ord(ch) - k)
                break
            s[i] = 'a'
            k -= dis
        return ''.join(s)