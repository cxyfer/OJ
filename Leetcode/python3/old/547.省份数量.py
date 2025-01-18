#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
from typing import *
# @lc code=start
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
# @lc code=end

