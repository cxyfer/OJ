def solve():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    # f[v] 表示當購買的價值為 v 時，所需的最小重量
    V = sum(v for _, v in items)
    f = [float("inf")] * (V + 1)
    f[0] = 0
    for w, v in items:
        for j in range(V, v - 1, -1):
            f[j] = min(f[j], f[j - v] + w)
    print(max(i for i, w in enumerate(f) if w <= W))

if __name__ == "__main__":
    solve()