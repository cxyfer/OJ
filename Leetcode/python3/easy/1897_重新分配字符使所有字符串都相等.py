#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#
from preImport import *
# @lc code=start
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = Counter([ch for word in words for ch in word])
        return all(v % n == 0 for v in cnt.values())
# @lc code=end

