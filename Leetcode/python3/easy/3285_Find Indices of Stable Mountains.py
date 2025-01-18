#
# @lc app=leetcode id=3285 lang=python3
# @lcpr version=30204
#
# [3285] Find Indices of Stable Mountains
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        ans = []
        for i in range(1, n):
            if height[i - 1] > threshold:
                ans.append(i)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,1,10,1,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [10,1,10,1,10]\n10\n
# @lcpr case=end

#

