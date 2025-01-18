#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
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
# @lc code=end
# @test("NES")=false
# @test("NESWW")=true
sol = Solution()
print(sol.isPathCrossing("NES")) # false
print(sol.isPathCrossing("NESWW")) # true
