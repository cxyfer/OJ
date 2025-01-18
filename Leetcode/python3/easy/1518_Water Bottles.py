#
# @lc app=leetcode id=1518 lang=python3
# @lcpr version=30204
#
# [1518] Water Bottles
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            q, r = divmod(numBottles, numExchange)
            numBottles = q + r
            ans += q
        return ans
    
class Solution2:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 9\n3\n
# @lcpr case=end

# @lcpr case=start
# 15\n4\n
# @lcpr case=end

#

