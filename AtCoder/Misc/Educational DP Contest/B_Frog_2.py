def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    f = [float('inf')] * N
    f[0] = 0
    for i in range(1, N):
        for j in range(i - 1, max(i - K, 0) - 1, -1):
            f[i] = min(f[i], f[j] + abs(A[i] - A[j]))
    print(f[N - 1])

if __name__ == "__main__":
    solve()