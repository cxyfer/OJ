#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Simulation
        # 從左上角開始，按照順時針方向依次填入數字，遇到邊界或已經填過的數字就轉向
        ans = [[0] * n for _ in range(n)]
        DIRETION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        st = (0, 0)
        cd = 0 # current direction
        for i in range(n*n):
            ans[st[0]][st[1]] = i+1
            nx, ny = st[0] + DIRETION[cd][0], st[1] + DIRETION[cd][1]
            # 模擬轉向，注意模擬到最後一個節點(中間點)後，就不用再轉向了
            while (nx < 0 or nx >= n or ny < 0 or ny >= n or ans[nx][ny] != 0) and i < n*n-1:
                cd = (cd + 1) % 4
                nx, ny = st[0] + DIRETION[cd][0], st[1] + DIRETION[cd][1]
            st = (nx, ny)
        return ans
# @lc code=end

sol = Solution()
for line in sol.generateMatrix(1):
    print("\t".join(map(str, line)))
for line in sol.generateMatrix(3):
    print("\t".join(map(str, line)))
for line in sol.generateMatrix(4):
    print("\t".join(map(str, line)))
for line in sol.generateMatrix(5):
    print("\t".join(map(str, line)))

