MOD = int(1e9 + 7)

def solve():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    f = [[0] * (m + 1) for _ in range(n + 1)]
    f[0][1] = 1
    for i, row in enumerate(grid, start=1):
        for j, c in enumerate(row, start=1):
            if c == '#':
                continue
            f[i][j] = (f[i - 1][j] + f[i][j - 1]) % MOD
    print(f[n][m])

if __name__ == "__main__":
    solve()