#
# @lc app=leetcode id=2960 lang=python3
# @lcpr version=30201
#
# [2960] Count Tested Devices After Test Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for x in batteryPercentages:
            if x - ans > 0:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n
# @lcpr case=end

#

