def solve1():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = mx = float("-inf")
    pre_a = pre_b = 0
    suf_c = sum(C)
    for i in range(n - 1):
        a, b, c = A[i], B[i], C[i]
        pre_a += a
        pre_b += b
        suf_c -= c
        ans = max(ans, suf_c + pre_b + mx)
        mx = max(mx, pre_a - pre_b)
    print(ans)


def solve2():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    f = [[0] * 3 for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(zip(A, B, C), start=1):
        f[i][0] = f[i - 1][0] + a
        if i >= 2:
            f[i][1] = max(f[i - 1][0], f[i - 1][1]) + b
        if i >= 3:
            f[i][2] = max(f[i - 1][1], f[i - 1][2]) + c
    print(f[n][2])


solve = solve1
# solve = solve2


if __name__ == "__main__":
    solve()
