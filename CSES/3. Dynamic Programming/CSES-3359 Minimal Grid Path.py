"""
CSES-3359 Minimal Grid Path
https://cses.fi/problemset/task/3359
"""
def solve():
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    ans = [grid[0][0]]
    f = [0]
    for d in range(2 * n - 2):  # 對角線
        nf = []
        vis = [False] * n
        min_ch = 'Z'
        for r in f:
            c = d - r
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if 0 <= nr < n and 0 <= nc < n and not vis[nr]:
                    vis[nr] = True
                    ch = grid[nr][nc]
                    if ch < min_ch:
                        min_ch = ch
                        nf = [nr]
                    elif ch == min_ch:
                        nf.append(nr)
        ans.append(min_ch)
        f = nf
    print("".join(ans))

if __name__ == "__main__":
    solve()