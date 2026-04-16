def solve():
    N, M = map(int, input().split())
    groups = [[] for _ in range(M)]
    for _ in range(N):
        a, b = map(int, input().split())
        groups[a - 1].append(b)

    for g in groups:
        print(f"{sum(g) / len(g):.10f}")


if __name__ == "__main__":
    solve()
