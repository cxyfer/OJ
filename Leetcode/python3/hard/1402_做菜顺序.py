#
# @lc app=leetcode.cn id=1402 lang=python3
#
# [1402] 做菜顺序
#
from preImport import *
# @lc code=start
class Solution:
    """
        Prefix sum
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        ans = 0
        for s in accumulate(satisfaction): # prefix sum
            if s < 0:
                break
            ans += s
        return ans
# @lc code=end
sol = Solution()
print(sol.maxSatisfaction([-1,-8,0,5,-9])) #14
print(sol.maxSatisfaction([4,3,2])) #20
print(sol.maxSatisfaction([-1,-4,-5])) #0
