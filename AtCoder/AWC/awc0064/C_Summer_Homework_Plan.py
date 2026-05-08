def solve():
    n, k = map(int, input().split())

    f = [0] * (k + 1)
    for _ in range(n):
        v, t = map(int, input().split())
        for j in range(k, t - 1, -1):
            f[j] = max(f[j], f[j - t] + v)

    print(max(f))


if __name__ == "__main__":
    solve()
