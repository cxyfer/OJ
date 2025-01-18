# @algorithm @lc id=1342 lang=python3 
# @title queens-that-can-attack-the-king


from en.Python3.mod.preImport import *
# @test([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],[0,0])=[[0,1],[1,0],[3,3]]
# @test([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]],[3,3])=[[2,2],[3,4],[4,4]]
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        Graph = [[0]*8 for _ in range(8)]
        DIR = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
        for x, y in queens:
            Graph[x][y] = 1
        kx, ky = king
        for x, y in queens:
            for dx, dy in DIR:
                if (kx-x) * dy != (ky-y) * dx: # 試圖優化一下，斜率不同，不在同一條線上
                    continue
                nx, ny = x+dx, y+dy
                while 0<=nx<8 and 0<=ny<8:
                    if Graph[nx][ny] == 1:
                        break
                    elif nx == kx and ny == ky:
                        ans.append([x,y])
                        break
                    nx += dx
                    ny += dy
        return ans