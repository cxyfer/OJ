#
# @lc app=leetcode id=3137 lang=python3
#
# [3137] Minimum Number of Operations to Make Word K-Periodic
#
from preImport import *
# @lc code=start
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter()
        for i in range(0, n, k):
            cnt[word[i:i+k]] += 1
        ans = n // k - max(cnt.values()) # 保留出現次數最多的那段，其他的都要改掉
        return ans
# @lc code=end

