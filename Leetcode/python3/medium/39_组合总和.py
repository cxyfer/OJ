#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from preImport import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)
        # candidates.sort()
        if n == 0:
            return ans
        
        def dfs(i, target):
            if target < 0:
                return
            if target == 0:
                ans.append(path[:])
                return
            for j in range(i, n):
                path.append(candidates[j])
                dfs(j, target - candidates[j])
                path.pop()
        dfs(0, target)
        return ans
# @lc code=end
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(sol.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
