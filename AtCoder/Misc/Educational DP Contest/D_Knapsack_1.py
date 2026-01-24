def solve():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    f = [0] * (W + 1)
    for w, v in items:
        for j in range(W, w - 1, -1):
            f[j] = max(f[j], f[j - w] + v)
    print(f[W])

if __name__ == "__main__":
    solve()