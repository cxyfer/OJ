#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
from preImport import *
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        cnt = Counter()
        for i in range(n - 9):
            cnt[s[i:i+10]] += 1
        return [key for key in cnt if cnt[key] > 1]
# @lc code=end

