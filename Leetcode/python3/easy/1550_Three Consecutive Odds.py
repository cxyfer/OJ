#
# @lc app=leetcode id=1550 lang=python3
# @lcpr version=30204
#
# [1550] Three Consecutive Odds
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for x in arr:
            if x & 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
# @lc code=end



#
# @lcpr case=start
# [2,6,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,34,3,4,5,7,23,12]\n
# @lcpr case=end

#

