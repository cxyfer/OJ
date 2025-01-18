#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def DFS(i):
            if self.flags[i] == 2: return True
            if self.flags[i] == 1: return False
            self.flags[i] = 1
            for j in self.Mtrx[i]:
                if not DFS(j): return False
            self.flags[i] = 2
            return True
            
        # 0: WHITE, 1: GRAY, 2: BLACK
        self.flags = [0 for _ in range(numCourses)]
        self.Mtrx = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            self.Mtrx[pre].append(cur)
        # DFS
        for i in range(numCourses):
            if not DFS(i): return False
        return True
# @lc code=end

