def solve():
    n = int(input())
    A = [0] + list(map(int, input().split()))

    pos = [-1] * (n + 1)
    for i, x in enumerate(A):
        pos[x] = i

    def query(x, y):
        print(f"? {x} {y}", flush=True)
        u, v = map(int, input().split())
        A[u], A[v] = A[v], A[u]
        pos[A[u]], pos[A[v]] = u, v

    for l in range(1, n // 2 + 1):
        r = n + 1 - l
        while pos[l] != l or pos[r] != r:
            if pos[l] != l:
                query(pos[l], l)
            else:
                query(pos[r], r)
    print('!', flush=True)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()