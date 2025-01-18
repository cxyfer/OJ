#
# @lc app=leetcode.cn id=1462 lang=python3
#
# [1462] 课程表 IV
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [[False] * numCourses for _ in range(numCourses)]
        g = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            g[a].append(b)
            indegree[b] += 1
        q = deque(i for i, x in enumerate(indegree) if x == 0)
        while q:
            i = q.popleft()
            for j in g[i]:
                res[i][j] = True
                for h in range(numCourses):
                    res[h][j] = res[h][j] or res[h][i]
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        return [res[a][b] for a, b in queries]
# @lc code=end

