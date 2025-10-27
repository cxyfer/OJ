#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        cnt1[0] = 1
        for r, x in enumerate(nums):
            if r > 0 and nums[r - 1] != x:
                cnt2.clear()
            s = (s + x) % k
            ans += cnt1[s]
            ans -= cnt2[s]
            cnt1[s] += 1
            cnt2[s] += 1
        return ans
# @lc code=end

