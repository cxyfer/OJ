#
# @lc app=leetcode id=506 lang=python3
# @lcpr version=30201
#
# [506] Relative Ranks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = sorted(range(n), key=lambda x: score[x], reverse=True)
        ans = [""] * n
        for rk, idx in enumerate(ranks):
            if rk == 0:
                ans[idx] = "Gold Medal"
            elif rk == 1:
                ans[idx] = "Silver Medal"
            elif rk == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rk + 1)
        return ans
# @lc code=end

sol = Solution()
print(sol.findRelativeRanks([5,4,3,2,1])) # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(sol.findRelativeRanks([10,3,8,9,4])) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

#
# @lcpr case=start
# [5,4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [10,3,8,9,4]\n
# @lcpr case=end

#

