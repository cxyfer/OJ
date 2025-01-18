#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
from typing import *
# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        def dfs(room):
            if not visited[room]:
                visited[room] = True
                for key in rooms[room]:
                    dfs(key)
        dfs(0)
        return all(visited)
# @lc code=end

sol = Solution()
rooms = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))

