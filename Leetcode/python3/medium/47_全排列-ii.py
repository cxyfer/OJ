#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from preImport import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        nums.sort() # 保證相同的數字在一起，方便判斷重複

        ans = []
        path = []
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            for j in range(n):
                if visited[j]: # 已經選過
                    continue
                if (j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]): # 確保重複數字從左邊先選(1a1b先選la)
                    continue
                path.append(nums[j])
                visited[j] = True
                dfs(i + 1)
                visited[j] = False
                path.pop()
        dfs(0)
        return ans
# @lc code=end

