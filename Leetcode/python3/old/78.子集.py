#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Backtracking: 子集型回溯
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # 不選
            dfs(i+1)
            # 選
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
# @lc code=end

