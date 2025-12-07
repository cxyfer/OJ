"""
CSES-1638 Grid Paths I
https://cses.fi/problemset/task/1638
"""
MOD = int(1e9 + 7)

def solve():
    n = int(input())
    grid = [input() for _ in range(n)]

    f = [0] * (n + 1)
    f[1] = 1
    for i, row in enumerate(grid, start=1):
        nf = [0] * (n + 1)
        for j, cell in enumerate(row, start=1):
            if cell == '.':
                nf[j] = (nf[j - 1] + f[j]) % MOD
            else:
                nf[j] = 0
        f = nf
    print(f[n])

if __name__ == "__main__":
    solve()