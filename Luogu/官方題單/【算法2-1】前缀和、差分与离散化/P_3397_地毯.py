"""
P3397 地毯
https://www.luogu.com.cn/problem/P3397
二維差分
"""


def solve():
    n, m = map(int, input().split())

    grid = [[0] * (n + 2) for _ in range(n + 2)]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        grid[x1][y1] += 1
        grid[x1][y2 + 1] -= 1
        grid[x2 + 1][y1] -= 1
        grid[x2 + 1][y2 + 1] += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
            print(grid[i][j], end=" ")
        print()


if __name__ == "__main__":
    solve()
