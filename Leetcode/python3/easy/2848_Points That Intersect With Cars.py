#
# @lc app=leetcode id=2848 lang=python3
# @lcpr version=30204
#
# [2848] Points That Intersect With Cars
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    """
        Similar to 56. Merge Intervals
    """
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        intervals = []
        for x, y in nums:
            if not intervals or x > intervals[-1][1]: # not overlap
                intervals.append([x, y])
            else:
                intervals[-1][1] = max(intervals[-1][1], y) # overlap, update interval
        return sum([y - x + 1 for x, y in intervals])
    
class Solution2:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        ans = 0
        st, ed = 0, -1
        for x, y in nums:
            if x > ed:
                ans += ed - st + 1
                st, ed = x, y
            else:
                ed = max(ed, y)
        ans += ed - st + 1
        return ans

class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [[3,6],[1,5],[4,7]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,8]]\n
# @lcpr case=end

#

