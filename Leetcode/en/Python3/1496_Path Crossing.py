# @algorithm @lc id=1619 lang=python3 
# @title path-crossing


from en.Python3.mod.preImport import *
# @test("NES")=false
# @test("NESWW")=true
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0,0)])
        x, y = 0, 0
        for ch in path:
            if ch == "N":
                y += 1
            elif ch == "S":
                y -= 1
            elif ch == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
        