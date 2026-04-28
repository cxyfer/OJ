"""
P2004 领地选择
https://www.luogu.com.cn/problem/P2004
二維前綴和
"""


def solve():
    n, m, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i, row in enumerate(grid, start=1):
        for j, val in enumerate(row, start=1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val

    ans = (1, 1)
    max_val = float("-inf")
    for x1 in range(1, n - c + 2):
        for y1 in range(1, m - c + 2):
            x2, y2 = x1 + c - 1, y1 + c - 1
            val = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
            if val > max_val:
                max_val = val
                ans = (x1, y1)
    print(*ans)


if __name__ == "__main__":
    solve()
