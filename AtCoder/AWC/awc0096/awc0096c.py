def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = [b - a for a, b in zip(A, B)]
    if any(c < 0 for c in C):
        print(-1)
        return

    ans = s = 0
    diff = [0] * (N + 1)
    for i, c in enumerate(C):
        s += diff[i]
        need = c - s
        if need < 0 or need > 0 and i + K > N:
            print(-1)
            return
        if need > 0:
            ans += need
            s += need
            diff[i + K] -= need
    print(ans)


if __name__ == "__main__":
    solve()
