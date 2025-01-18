# @algorithm @lc id=47 lang=python3 
# @title permutations-ii


from en.Python3.mod.preImport import *
# @test([1,1,2])=[[1,1,2],[1,2,1],[2,1,1]]
# @test([1,2,3])=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
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