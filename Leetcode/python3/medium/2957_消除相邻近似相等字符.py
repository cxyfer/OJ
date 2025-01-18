#
# @lc app=leetcode.cn id=2957 lang=python3
#
# [2957] 消除相邻近似相等字符
#

# @lc code=start
class Solution:
    """
        分組循環
    """
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 0
        while i < n:
            st = i
            while i + 1 < n and abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                i += 1
            i += 1
            ans += (i - st) // 2
        return ans
# @lc code=end

