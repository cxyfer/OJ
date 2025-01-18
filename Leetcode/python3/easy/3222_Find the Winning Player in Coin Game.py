#
# @lc app=leetcode id=3222 lang=python3
# @lcpr version=30204
#
# [3222] Find the Winning Player in Coin Game
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) & 1 else "Bob"
# @lc code=end



#
# @lcpr case=start
# 2\n7\n
# @lcpr case=end

# @lcpr case=start
# 4\n11\n
# @lcpr case=end

#

