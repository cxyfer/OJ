# @algorithm @lc id=661 lang=python3 
# @title image-smoother


from en.Python3.mod.preImport import *
# @test([[1,1,1],[1,0,1],[1,1,1]])=[[0,0,0],[0,0,0],[0,0,0]]
# @test([[100,200,100],[200,50,200],[100,200,100]])=[[137,141,137],[141,138,141],[137,141,137]]
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # return self.solve1(img)
        return self.solve2(img)
    def solve1(self, img: List[List[int]]) -> List[List[int]]:
        DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        m, n = len(img), len(img[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt, s = 1, img[i][j]
                for di, dj in DIRS:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n:
                        cnt += 1
                        s += img[ni][nj]
                ans[i][j] = s // cnt
        return ans
    def solve2(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        s = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + img[i - 1][j - 1]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a, b = max(0, i - 1), max(0, j - 1) # 避免越界
                c, d = min(m - 1, i + 1), min(n - 1, j + 1) # 避免越界
                cnt = (c - a + 1) * (d - b + 1) # 有效單元格的數量
                tot = s[c + 1][d + 1] - s[a][d + 1] - s[c + 1][b] + s[a][b] # 二維前綴和
                ans[i][j] = tot // cnt
        return ans

