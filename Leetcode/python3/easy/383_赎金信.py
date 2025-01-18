#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
from preImport import *
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        return all(cnt1[ch] <= cnt2[ch] for ch in cnt1)
# @lc code=end

