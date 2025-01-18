# @algorithm @lc id=1746 lang=python3 
# @title largest-substring-between-two-equal-characters


from en.Python3.mod.preImport import *
# @test("aa")=0
# @test("abca")=2
# @test("cbzxy")=-1
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        pos = [[-1, -1] for _ in range(26)]
        for i, ch in enumerate(s):
            ch = ord(ch) - ord('a')
            if pos[ch][0] == -1:
                pos[ch][0] = i
            else:
                pos[ch][1] = i
                ans = max(ans, pos[ch][1] - pos[ch][0] - 1)
        return ans