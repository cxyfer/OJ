#
# @lc app=leetcode id=2961 lang=python3
# @lcpr version=30204
#
# [2961] Double Modular Exponentiation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[2,3,3,10],[3,3,3,1],[6,1,1,4]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[39,3,1000,1000]]\n17\n
# @lcpr case=end

#

