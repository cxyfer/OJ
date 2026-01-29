def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N

    f = [False] * (K + 1)
    for j in range(K + 1):
        for x in A:
            if j < x:
                break
            f[j] |= not f[j - x]
    print("First" if f[K] else "Second")

if __name__ == "__main__":
    solve()