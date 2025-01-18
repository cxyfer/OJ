#
# @lc app=leetcode id=1701 lang=python3
# @lcpr version=30204
#
# [1701] Average Waiting Time
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        tot = 0 # total waiting time
        cur = 0 # current time
        for a, t in customers:
            cur = max(cur, a) + t
            tot += cur - a
        return tot / n
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,5],[4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,2],[5,4],[10,3],[20,1]]\n
# @lcpr case=end

#

