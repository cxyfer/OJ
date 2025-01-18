#
# @lc app=leetcode id=2028 lang=python3
# @lcpr version=30202
#
# [2028] Find Missing Observations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Math + Simulation
    """
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = mean * (m + n) - sum(rolls) # 缺失值的總和
        if s < n or s > 6 * n: # 無法滿足條件
            return []
        q, r = divmod(s, n)
        return [q+1] * r + [q] * (n - r)
# @lc code=end



#
# @lcpr case=start
# [3,2,4,3]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,5,6]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n6\n4\n
# @lcpr case=end

#

