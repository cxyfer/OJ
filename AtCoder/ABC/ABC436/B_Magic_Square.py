def solve():
    N = int(input())

    ans = [[0] * N for _ in range(N)]

    r, c = 0, (N - 1) // 2
    for k in range(1, N * N + 1):
        ans[r][c] = k
        
        nr, nc = (r - 1) % N, (c + 1) % N
        if ans[nr][nc] == 0:
            r, c = nr, nc
        else:
            r, c = (r + 1) % N, c

    for row in ans:
        print(*row)

if __name__ == "__main__":
    solve()