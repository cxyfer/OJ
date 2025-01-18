#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#
from preImport import *
# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        visited = set()
        for x in nums:
            if -x in visited:
                ans = max(ans, abs(x))
            visited.add(x)
        return ans
# @lc code=end
sol = Solution()
print(sol.findMaxK([-1,2,-3,3])) # 3
print(sol.findMaxK([-1,10,6,7,-7,1])) # 7
print(sol.findMaxK([-10,8,6,7,-2,-3])) # -1

