#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from preImport import *
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(v == 1 for v in Counter(Counter(arr).values()).values())
# @lc code=end

