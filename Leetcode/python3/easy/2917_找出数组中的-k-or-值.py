#
# @lc app=leetcode.cn id=2917 lang=python3
#
# [2917] 找出数组中的 K-or 值
#
from preImport import *
# @lc code=start
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(31):
            mask = 1 << i
            cnt = 0
            for x in nums:
                if x & mask:
                    cnt += 1
            if cnt >= k:
                ans |= mask
        return ans
# @lc code=end

