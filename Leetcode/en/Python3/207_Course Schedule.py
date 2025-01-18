# @algorithm @lc id=207 lang=python3 
# @title course-schedule


from en.Python3.mod.preImport import *
# @test(2,[[1,0]])=true
# @test(2,[[1,0],[0,1]])=false
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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