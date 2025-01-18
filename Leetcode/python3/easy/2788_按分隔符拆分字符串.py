#
# @lc app=leetcode.cn id=2788 lang=python3
#
# [2788] 按分隔符拆分字符串
#
from typing import List
# @lc code=start
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [x for w in words for x in w.split(separator) if x != '']
# @lc code=end

