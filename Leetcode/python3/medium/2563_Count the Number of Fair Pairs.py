#
# @lc app=leetcode id=2563 lang=python3
# @lcpr version=30204
#
# [2563] Count the Number of Fair Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Binary Search
    由於順序不影響 Fair Pairs 的對數，只需要確保不重複計算即可，因此可以先對nums進行排序。

    然後對於每個 i，找到有多少 j 可以使 lower <= nums[i] + nums[j] <= upper
    即 lower - nums[i] <= nums[j] <= upper - nums[i]，這可以透過二分搜尋來找到。

    但注意不能包含 (i, i) 這種情況，以及不能重複計算。
    這可以透過限制二分的範圍在 [0, i) 或 [i + 1, n) 來解決：
    或是也能先不管，但先扣掉 (i, i) 的情況後，最後再除以 2 即可。
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for idx, x in enumerate(nums):
            l = bisect_left(nums, lower - x, 0, idx) # [0, idx)
            r = bisect_right(nums, upper - x, 0, idx) - 1 # [0, idx)
            ans += r - l + 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,7,4,4,5]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,7,9,2,5]\n11\n11\n
# @lcpr case=end

#

