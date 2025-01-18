#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return word[:idx+1][::-1] + word[idx+1:]
# @lc code=end

