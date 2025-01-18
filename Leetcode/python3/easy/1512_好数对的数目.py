#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#
from preImport import *
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for idx, num in enumerate(nums):
            ans += cnt[num]
            cnt[num] += 1
        return ans
# @lc code=end

