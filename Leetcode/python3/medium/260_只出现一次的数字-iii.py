#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
from preImport import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [num for num in cnt if cnt[num] == 1]
# @lc code=end

