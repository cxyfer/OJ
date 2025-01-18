#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from typing import List
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        # Build adjacency List
        flags = [0 for _ in range(numCourses)] # 0: WHITE, 1: GRAY, 2: BLACK
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[cur].append(pre)
        # DFS
        def DFS(i):
            if flags[i] == 2: return True 
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adj[i]:
                if not DFS(j): return False
            flags[i] = 2
            ans.append(i) # append to ans after all its children are visited
            return True

        for i in range(numCourses):
            if not DFS(i):
                return []
        return ans

# @lc code=end

