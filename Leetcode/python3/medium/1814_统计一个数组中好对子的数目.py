#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#
from preImport import *
# @lc code=start
class Solution:
    """
        0 <= i < j < nums.length
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    """
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        cnt = Counter()
        for x in nums:
            rev_x = int(str(x)[::-1])
            ans += cnt[x - rev_x]
            cnt[x - rev_x] += 1
        return ans % MOD
# @lc code=end

