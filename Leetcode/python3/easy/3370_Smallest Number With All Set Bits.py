#
# @lc app=leetcode id=3370 lang=python3
# @lcpr version=30204
#
# [3370] Smallest Number With All Set Bits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

