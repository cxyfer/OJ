#
# @lc app=leetcode.cn id=2942 lang=python3
#
# [2942] 查找包含给定字符的单词
#
from preImport import *
# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for idx, word in enumerate(words) if x in word]
        ans = []
        for idx, word in enumerate(words):
            if x in word:
                ans.append(idx)
        return ans
# @lc code=end

