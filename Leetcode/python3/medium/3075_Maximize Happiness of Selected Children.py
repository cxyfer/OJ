#
# @lc app=leetcode id=3075 lang=python3
# @lcpr version=30201
#
# [3075] Maximize Happiness of Selected Children
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy + Sort 優先選最大的
    """
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True) # 由大到小選擇
        ans = 0
        for i in range(k): # k round 
            cur = happiness[i] - i # 考慮遞減
            if cur <= 0:
                break
            ans += cur
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5]\n1\n
# @lcpr case=end

#

