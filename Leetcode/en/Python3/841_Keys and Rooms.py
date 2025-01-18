# @algorithm @lc id=871 lang=python3 
# @title keys-and-rooms


from en.Python3.mod.preImport import *
# @test([[1],[2],[3],[]])=true
# @test([[1,3],[3,0,1],[2],[0]])=false
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