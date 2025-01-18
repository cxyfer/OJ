#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
from preImport import *
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        s = 0
        cnt[0] = -1
        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1
            if s in cnt:
                ans = max(ans, i - cnt[s])
            else:
                cnt[s] = i
        return ans
# @lc code=end

