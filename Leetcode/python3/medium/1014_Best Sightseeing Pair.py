#
# @lc app=leetcode id=1014 lang=python3
# @lcpr version=30204
#
# [1014] Best Sightseeing Pair
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        mx = values[0] + 0
        for j in range(1, n): # 枚舉右邊的點
            ans = max(ans, mx + values[j] - j)
            # i = j
            mx = max(mx, values[j] + j) # 維護左邊的最大值
        return ans
# @lc code=end



#
# @lcpr case=start
# [8,1,5,2,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

