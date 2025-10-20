#
# @lc app=leetcode id=3346 lang=python3
#
# [3346] Maximum Frequency of an Element After Performing Operations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
max = lambda a, b: a if a > b else b
min = lambda a, b: a if a < b else b

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cnt = Counter(nums)
        ans = 0
        for v in range(nums[0], nums[-1] + 1):
            l = bisect_left(nums, v - k)
            r = bisect_right(nums, v + k)
            ans = max(ans, min(r - l, cnt[v] + numOperations))
        return ans
# @lc code=end

