#
# @lc app=leetcode id=2683 lang=python3
# @lcpr version=30204
#
# [2683] Neighboring Bitwise XOR
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0
# @lc code=end



#
# @lcpr case=start
# [1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0]\n
# @lcpr case=end

#

