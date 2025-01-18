#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#
from preImport import *
# @lc code=start
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
# @lc code=end
# @test("aa")=0
# @test("abca")=2
# @test("cbzxy")=-1
sol = Solution()
print(sol.maxLengthBetweenEqualCharacters("aa"))
print(sol.maxLengthBetweenEqualCharacters("abca"))
print(sol.maxLengthBetweenEqualCharacters("cbzxy"))
print(sol.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv")) # 18
