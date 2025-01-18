#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from preImport import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.solve1(numCourses, prerequisites)
        return self.solve2(numCourses, prerequisites)
    def solve1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses # 0: WHITE, 1: GRAY, 2: BLACK
        g = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            g[pre].append(cur)
        def dfs(i):
            if visited[i] == 1: return False
            if visited[i] == 2: return True
            visited[i] = 1
            for j in g[i]:
                if not dfs(j): return False
            visited[i] = 2
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
    def hasCycle(n: int, edges: List[List[int]]) -> bool:
        g = [[] for _ in range(n)] # adjacency list

        for u, v in edges: # undirected graph
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n

        def dfs(u, fa):
            visited[u] = True
            for v in g[u]:
                if v == fa: continue
                if visited[v]: return False
                if not dfs(v, u): return False
            return True

        for u in range(n):
            if not visited[u]:
                if not dfs(u, -1): return True # has cycle
        return False
# @lc code=end

