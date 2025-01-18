#
# @lc app=leetcode.cn id=2817 lang=python3
#
# [2817] 限制条件下元素之间的最小绝对差
#

# @lc code=start
# First Meet sortedcontainers
from sortedcontainers import SortedList
from math import inf

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        ans = inf
        sl = SortedList() # Sorted candidates
        sl.add(inf)
        sl.add(-inf)
        for v, y in zip(nums, nums[x:]):
            sl.add(v) # Add candidate
            # Find the index of y, if y is not in sl, return the index of the leftmost element greater than y
            j = sl.bisect_left(y) 
            # closest element to y is sl[j] or sl[j - 1]
            ans = min(ans, sl[j] - y, y - sl[j - 1])
            if ans == 0: return 0
        return ans



# @lc code=end

