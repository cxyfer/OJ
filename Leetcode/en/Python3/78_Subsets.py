# @algorithm @lc id=78 lang=python3 
# @title subsets


from en.Python3.mod.preImport import *
# @test([1,2,3])=[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# @test([0])=[[],[0]]
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