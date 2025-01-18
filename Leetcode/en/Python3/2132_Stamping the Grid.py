# @algorithm @lc id=2200 lang=python3 
# @title stamping-the-grid


from en.Python3.mod.preImport import *
# @test([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],4,3)=true
# @test([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],2,2)=false
# @test([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 4, 3)=true
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        # 1. 對grid做二維前綴和，表示區域中有幾個1，即不能放置郵票的位置數量
        m, n = len(grid), len(grid[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + grid[i][j]
        # print(*pre_sum, sep='\n')

        # 2. 對所有可以放置郵票的位置，做二維差分，表示這個區域放置了郵票
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for c in range(stampHeight, m + 1):
            for d in range(stampWidth, n + 1):
                a, b = c - stampHeight + 1, d - stampWidth + 1 # 左上角
                if pre_sum[c][d] - pre_sum[a - 1][d] - pre_sum[c][b - 1] + pre_sum[a - 1][b - 1] == 0: # 如果中間的區域不可放置的位置數量為0，則可以放置郵票，
                    diff[a - 1][b - 1] += 1
                    diff[c][b - 1] -= 1
                    diff[a - 1][d] -= 1
                    diff[c][d] += 1
        # print(*diff, sep='\n')

        # 3. 對二維差分做前綴和，若有可放置郵票，但卻沒有放置郵票的位置，則不可行
        for i in range(m):
            for j in range(n):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1] # 二維差分前綴和
                if grid[i][j] == 0 and diff[i][j] == 0: # 有可放置郵票，但卻沒有放置郵票的位置
                    return False
        return True