#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in s.split(" ")[::-1] if word])
# @lc code=end

