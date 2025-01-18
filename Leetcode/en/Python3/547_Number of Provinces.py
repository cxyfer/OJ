# @algorithm @lc id=547 lang=python3 
# @title number-of-provinces


from en.Python3.mod.preImport import *
# @test([[1,1,0],[1,1,0],[0,0,1]])=2
# @test([[1,0,0],[0,1,0],[0,0,1]])=3
class Solution:
    """
        DFS
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        ans = 0
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                ans += 1
                visited[i] = True
                dfs(i)
        return ans