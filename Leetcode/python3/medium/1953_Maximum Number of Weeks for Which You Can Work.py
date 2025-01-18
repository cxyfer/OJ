#
# @lc app=leetcode id=1953 lang=python3
# @lcpr version=30202
#
# [1953] Maximum Number of Weeks for Which You Can Work
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy + Math
        首先想一下甚麼時候會無法完成所有項目：
            由於連續兩周必須要完成不同的項目，若有一個項目特別大，就算交錯該項目與所有其他項目，也會導致完成其他項目後，剩下該項目未完成。
       所以當最大的項目數量超過其餘項目數量的總和 + 1時，就無法完成所有項目
    """
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s = sum(milestones)
        mx = max(milestones)
        if mx > s - mx + 1: # 不能完成所有專案
            return 2*(s - mx) + 1
        else: # 可以完成所有專案
            return s
# @lc code=end
sol = Solution()
print(sol.numberOfWeeks([5,2,1])) # 7



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,1]\n
# @lcpr case=end

#

