#
# @lc app=leetcode.cn id=2073 lang=python3
#
# [2073] 买票需要的时间
#
from preImport import *
# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        res1 = sum([min(target, t) for t in tickets[:k]])
        res2 = sum([min(target-1, t) for t in tickets[k+1:]])
        return res1 + target + res2
# @lc code=end
sol = Solution()
print(sol.timeRequiredToBuy([84,49,5,24,70,77,87,8], 3)) # 154