#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
max = lambda x, y: x if x > y else y
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = s = left = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            s += x
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[nums[left]] -= 1
                s -= nums[left]
                left += 1
            ans = max(ans, s)
        return ans
# @lc code=end

